import os
import shutil
import psutil

def run_command(command, current_dir):
    """
    Execute a command and return output + updated directory.
    """
    parts = command.strip().split()
    if not parts:
        return "No command entered", current_dir

    cmd = parts[0]
    args = parts[1:]

    try:
        # List files
        if cmd == "ls":
            items = os.listdir(current_dir)
            return "\n".join(items) if items else "Directory is empty", current_dir

        # Change directory
        elif cmd == "cd":
            if not args:
                return "Usage: cd <directory>", current_dir
            new_dir = os.path.join(current_dir, args[0])
            if os.path.isdir(new_dir):
                return f"Changed directory to {new_dir}", new_dir
            return "No such directory", current_dir

        # Print working directory
        elif cmd == "pwd":
            return current_dir, current_dir

        # Make directory
        elif cmd == "mkdir":
            if not args:
                return "Usage: mkdir <foldername>", current_dir
            os.mkdir(os.path.join(current_dir, args[0]))
            return f"Folder '{args[0]}' created", current_dir

        # Remove file/folder
        elif cmd == "rm":
            if not args:
                return "Usage: rm <file/folder>", current_dir
            target = os.path.join(current_dir, args[0])
            if os.path.isfile(target):
                os.remove(target)
                return f"File '{args[0]}' removed", current_dir
            elif os.path.isdir(target):
                shutil.rmtree(target)
                return f"Folder '{args[0]}' removed", current_dir
            else:
                return "No such file or folder", current_dir

        # CPU usage
        elif cmd == "cpu":
            return f"CPU Usage: {psutil.cpu_percent()}%", current_dir

        # Memory usage
        elif cmd == "mem":
            mem = psutil.virtual_memory()
            return f"Memory Usage: {mem.percent}% ({mem.used // (1024**2)}MB / {mem.total // (1024**2)}MB)", current_dir

        # Running processes
        elif cmd == "ps":
            processes = []
            for p in psutil.process_iter(['pid', 'name']):
                processes.append(f"{p.info['pid']} - {p.info['name']}")
            return "\n".join(processes[:15]), current_dir  # show top 15

        # Exit
        elif cmd == "exit":
            return "exit", current_dir

        # Unknown command
        else:
            return f"Unknown command: {cmd}", current_dir

    except Exception as e:
        return f"Error: {str(e)}", current_dir
