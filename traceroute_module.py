import subprocess
from datetime import datetime

def run_traceroute(host="8.8.8.8"):
    try:
        output = subprocess.check_output(["traceroute", host], stderr=subprocess.STDOUT).decode()
        hops = output.strip().split("\n")[1:]
        return {
            "timestamp": datetime.now(),
            "host": host,
            "hops": len(hops),
            "output": output,
            "status": "OK"
        }
    except subprocess.CalledProcessError as e:
        return {
            "timestamp": datetime.now(),
            "host": host,
            "error": str(e),
            "status": "FAIL"
        }