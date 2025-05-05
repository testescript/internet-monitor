from modules import speedtest_module, ping_module, dns_module
from core.scheduler import (
    gerar_cronograma_24h,
    gerar_cronograma_7dias,
    gerar_cronograma_rapido,
    esta_em_horario_ponta
)
from utils.logger import guardar_resultados
from core.analyzer import analisar_resultados
from core.report_generator import gerar_grafico, gerar_html
from datetime import datetime
import time as t

def executar_monitoramento(agenda, testes, download_contratado, upload_contratado):
    resultados = []
    for i, momento in enumerate(agenda, 1):
        espera = (momento - datetime.now()).total_seconds()
        if espera > 0:
            print(f"\n🕒 A aguardar para Teste {i}/{len(agenda)} às {momento.strftime('%H:%M')}")
            t.sleep(espera)

        print(f"▶️ Teste {i}: {datetime.now().strftime('%H:%M:%S')}")
        res = {}

        # Speedtest
        if 1 in testes:
            spd = speedtest_module.run_speedtest()
            res.update(spd)

            if spd.get("status") == "OK":
                dl = spd['download']
                ul = spd['upload']
                limiar = 0.8 if download_contratado >= 100 else 0.7
                conforme = dl >= download_contratado * limiar and ul >= upload_contratado * limiar
                status = "✅ CONFORME" if conforme else "❌ NÃO CONFORME"
                print(f"  📡 Speedtest → Download: {dl} Mbps | Upload: {ul} Mbps | Ping: {spd['ping']} ms")
                print(f"     📜 Verificação ANACOM: {status} (limiar {int(limiar*100)}%)")
                res['conforme'] = status
            else:
                print(f"  ❌ Speedtest falhou → {spd.get('error')} (tentativas: {spd.get('tentativa')})")

        # Ping
        if 2 in testes:
            ping_res = ping_module.run_ping()
            res["ping_custom"] = ping_res
            status = "✅ Sucesso" if "output" in ping_res else "❌ Erro"
            print(f"  🛰️ Ping para {ping_res['host']} → {status}")

        # DNS
        if 3 in testes:
            dns_res = dns_module.run_dns()
            res["dns"] = dns_res
            status = f"{dns_res['ip']} ({dns_res['resolution_ms']} ms)" if "ip" in dns_res else f"❌ Erro: {dns_res['error']}"
            print(f"  🌐 DNS → {dns_res['domain']} → {status}")

        # Traceroute
        if 4 in testes:
            from modules import traceroute_module
            trace = traceroute_module.run_traceroute()
            res["traceroute"] = trace
            print(f"  🧭 Traceroute para {trace['host']} → Hops: {trace.get('hops', 'Erro')}")

        # Fast
        if 5 in testes:
            from modules import fast_module
            fast = fast_module.run_fast()
            res["fast"] = fast
            print(f"  ⚡ Fast.com → {fast['speed']} Mbps")

        # Timestamp e hora
        res['timestamp'] = datetime.now()
        res['horario'] = "PONTA" if esta_em_horario_ponta(res['timestamp']) else "FORA DE PONTA"
        resultados.append(res)

    # Pós testes: guardar, analisar, relatar
    guardar_resultados(resultados)
    analise = analisar_resultados(resultados, download_contratado, upload_contratado)
    grafico = gerar_grafico(resultados)
    relatorio = gerar_html(analise, grafico)
    print(f"\n✅ Relatório gerado: {relatorio}")

def escolher_testes():
    print("1 - Speedtest")
    print("2 - Ping")
    print("3 - DNS")
    print("4 - Traceroute")
    print("5 - Fast.com")
    escolhas = input("Testes a executar (ex: 1,3,5): ")
    return [int(t.strip()) for t in escolhas.split(",") if t.strip().isdigit()]

def main():
    print("=== Internet Monitor Modular ===")
    print("1 - Modo ANACOM (Regulamentado)")
    print("2 - Modo RÁPIDO (Personalizado)")
    modo = input("Escolha o modo [1/2]: ").strip()

    download = float(input("Velocidade DOWNLOAD contratada (Mbps): "))
    upload = float(input("Velocidade UPLOAD contratada (Mbps): "))

    testes = escolher_testes()

    if modo == "1":
        tipo = input("Tipo [24h / 7d]: ").strip().lower()
        if tipo == "24h":
            agenda = gerar_cronograma_24h()
        else:
            total = int(input("Total de testes (mín. 20): "))
            agenda = gerar_cronograma_7dias(total_testes=total)
    elif modo == "2":
        duracao = int(input("Tempo total em minutos: "))
        total = int(input("Número total de testes: "))
        agenda = gerar_cronograma_rapido(duracao, total)
    else:
        print("Modo inválido.")
        return

    executar_monitoramento(agenda, testes, download, upload)

if __name__ == "__main__":
    main()
