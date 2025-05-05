import time
from datetime import datetime
from modules import speedtest_module
from config import LIMIAR_ANACOM
from db import guardar_resultado, init_db
from alert import alerta_email, alerta_telegram

def esta_em_horario_ponta(dt):
    return "PONTA" if 19 <= dt.hour <= 23 else "FORA DE PONTA"

def verificar_conformidade(dl, ul, download_ref, upload_ref):
    limiar = LIMIAR_ANACOM["min100"] if download_ref >= 100 else LIMIAR_ANACOM["baixo100"]
    conforme = dl >= download_ref * limiar and ul >= upload_ref * limiar
    return conforme, int(limiar * 100)

def loop_monitor(download_ref, upload_ref, intervalo_segundos=3600):
    init_db()
    while True:
        print(f"🕒 Executando teste em {datetime.now().strftime('%H:%M:%S')}")
        resultado = speedtest_module.run_speedtest()
        ts = datetime.now().isoformat()
        horario = esta_em_horario_ponta(datetime.now())

        if resultado["status"] == "OK":
            conforme, limiar = verificar_conformidade(resultado['download'], resultado['upload'], download_ref, upload_ref)
            status = "✅" if conforme else "❌"
            print(f"📡 {status} DL: {resultado['download']} | UL: {resultado['upload']} (limiar {limiar}%)")

            guardar_resultado(ts, "download", resultado["download"], status, horario)
            guardar_resultado(ts, "upload", resultado["upload"], status, horario)
            guardar_resultado(ts, "ping", resultado["ping"], "-", horario)

            if not conforme:
                msg = f"⚠️ Conformidade abaixo do limiar {limiar}%\nDL: {resultado['download']} | UL: {resultado['upload']}"
                alerta_email(msg)
                alerta_telegram(msg)
        else:
            print("❌ Speedtest falhou")

        time.sleep(intervalo_segundos)
