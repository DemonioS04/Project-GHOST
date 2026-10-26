import subprocess

def run_command(command):
    try:
        result=subprocess.Popen("start cmd /k wsl -d kali-linux", shell=True)
        return result
    except Exception as e:
        return "None"