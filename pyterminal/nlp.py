def parse_nlp(command: str) -> str:
    """
    Convert natural language into terminal commands.
    """
    text = command.lower().strip()

    if text.startswith("create folder"):
        folder = text.replace("create folder", "").strip()
        return f"mkdir {folder}" if folder else "mkdir"

    elif text.startswith("make directory"):
        folder = text.replace("make directory", "").strip()
        return f"mkdir {folder}" if folder else "mkdir"

    elif text.startswith("delete file"):
        target = text.replace("delete file", "").strip()
        return f"rm {target}" if target else "rm"

    elif text.startswith("delete folder"):
        target = text.replace("delete folder", "").strip()
        return f"rm {target}" if target else "rm"

    elif text in ["show cpu", "cpu usage"]:
        return "cpu"

    elif text in ["show memory", "memory usage"]:
        return "mem"

    elif text in ["show processes", "list processes"]:
        return "ps"

    elif text == "current directory":
        return "pwd"

    elif text.startswith("go to"):
        folder = text.replace("go to", "").strip()
        return f"cd {folder}" if folder else "cd"

    # fallback → return original command
    return command
