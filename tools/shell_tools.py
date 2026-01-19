import subprocess
from typing import List

# Commands that are explicitly allowed
ALLOWED_COMMANDS = {
    "ls",
    "pwd",
    "whoami",
    "python",
    "pip",
    "git",
    "echo"
}

def run_command(command: List[str], timeout: int = 10) -> str:
    """
    Safely run a shell command.

    - Only allows whitelisted base commands
    - No shell=True
    - Timeout enforced
    """

    if not command:
        return "Error: Empty command."

    base_cmd = command[0]

    if base_cmd not in ALLOWED_COMMANDS:
        return f"Blocked command: '{base_cmd}' is not allowed."

    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=timeout
        )
        if result.returncode != 0:
            return f"Error:\n{result.stderr.strip()}"

        return result.stdout.strip()

    except subprocess.TimeoutExpired:
        return "Error: Command timed out."
    except Exception as e:
        return f"Error: {str(e)}"
