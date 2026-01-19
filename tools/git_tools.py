import subprocess

def git_status():
    try:
        return subprocess.check_output(
            ["git", "status", "--short"],
            stderr=subprocess.STDOUT,
            text=True
        )
    except subprocess.CalledProcessError as e:
        return e.output
