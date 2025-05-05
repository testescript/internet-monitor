from datetime import datetime
import random

def run_fast():
    try:
        velocidade = round(random.uniform(100, 900), 2)
        return {
            "timestamp": datetime.now(),
            "speed": velocidade,
            "status": "OK"
        }
    except Exception as e:
        return {
            "timestamp": datetime.now(),
            "error": str(e),
            "status": "FAIL"
        }