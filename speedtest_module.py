import speedtest
from datetime import datetime
import time

def run_speedtest(max_retentativas=3, espera_segundos=5):
    tentativa = 0
    while tentativa < max_retentativas:
        try:
            st = speedtest.Speedtest()
            servers = st.get_servers([])
            best = st.get_best_server()
            print(f"Usando servidor: {best['sponsor']} em {best['name']}")
            result = {
                "timestamp": datetime.now(),
                "download": round(st.download() / 1_000_000, 2),
                "upload": round(st.upload() / 1_000_000, 2),
                "ping": round(st.results.ping, 2),
                "server": st.results.server['host'],
                "status": "OK"
            }
            return result
        except Exception as e:
            tentativa += 1
            if tentativa >= max_retentativas:
                return {
                    "timestamp": datetime.now(),
                    "error": str(e),
                    "tentativa": tentativa,
                    "status": "FAIL"
                }
            time.sleep(espera_segundos)
