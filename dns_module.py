import socket
from datetime import datetime
import time

def run_dns(domain="www.google.com"):
    start = time.time()
    try:
        ip = socket.gethostbyname(domain)
        duration = round((time.time() - start) * 1000, 2)
        return {"timestamp": datetime.now(), "domain": domain, "ip": ip, "resolution_ms": duration}
    except Exception as e:
        return {"timestamp": datetime.now(), "domain": domain, "error": str(e)}
