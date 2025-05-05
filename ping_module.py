import subprocess
from datetime import datetime

def run_ping(host="8.8.8.8"):
    cmd = ["ping", "-c", "4", host]
    try:
        output = subprocess.check_output(cmd).decode()
        return {"timestamp": datetime.now(), "host": host, "output": output}
    except subprocess.CalledProcessError:
        return {"timestamp": datetime.now(), "host": host, "error": "Ping failed"}
