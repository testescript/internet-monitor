# 🛰️ Internet Monitor Modular (Portugal - ANACOM Compliance)

![Python](https://img.shields.io/badge/python-3.7%2B-blue)
![Status](https://img.shields.io/badge/status-Em%20Desenvolvimento-yellow)
![License](https://img.shields.io/badge/license-MIT-green)

Sistema de monitorização de internet com foco em:
- 🏛️ Conformidade com regulamentos da ANACOM
- ⚙️ Testes rápidos e automatizados (speedtest, ping, DNS, traceroute, fast)
- 📊 Relatórios detalhados (HTML / JSON / SQLite)
- 📦 Pronto para integração com Grafana ou dashboards web

---

## 🚀 Funcionalidades

| Modo         | Descrição                                                           |
|--------------|----------------------------------------------------------------------|
| **ANACOM**   | Executa plano regulamentado: 24h / 7d, 96 testes ou +20 testes       |
| **Rápido**   | Escolhe tempo total, nº de testes e tipos (1-5)                      |
| **Headless** | Loop automático (`monitor_loop.py`) com logs em SQLite              |
| **Alertas**  | Integração com Email e Telegram para notificações                   |
| **Relatórios** | Geração de HTML com gráfico + conformidade ANACOM                 |

---

## 📂 Estrutura do Projeto

internet_monitor/
├── main.py # CLI interativo
├── monitor_loop.py # Execução automática
├── config.py # Configurações e limites ANACOM
├── db.py # Base de dados SQLite
├── alert.py # Envio de alertas (email / Telegram)
├── setup.py # Criação automática de módulos faltantes
│
├── modules/ # Testes de conectividade
│ ├── speedtest_module.py
│ ├── ping_module.py
│ ├── dns_module.py
│ ├── traceroute_module.py
│ └── fast_module.py
│
├── core/ # Lógica de cronograma e análise
│ ├── scheduler.py
│ ├── analyzer.py
│ └── report_generator.py
│
├── utils/ # Logger e helpers
│ └── logger.py
│
├── relatorios/ # Relatórios e gráficos
└── logs/ # Logs JSON brutos

---

## ⚙️ Instalação

```bash
git clone https://github.com/seu-usuario/internet-monitor.git
cd internet-monitor

# Cria ambiente virtual (recomendado)
python3 -m venv venv
source venv/bin/activate

# Instala dependências
pip install -r requirements.txt

# Gera módulos faltantes (opcional)
python3 setup.py

▶️ Como Usar
🖥️ Modo Interativo
bash
Copiar
Editar
python3 main.py
Escolhe:

Modo ANACOM (24h ou 7d)

Ou modo rápido (tempo total, nº de testes, tipos)

🔁 Modo Automático (sem interação)

python3 monitor_loop.py

Executa testes programados, salva resultados em internet_data.db, e alerta se velocidades não estiverem conformes.

📈 Integração com Grafana
Todos os dados são salvos em SQLite: internet_data.db

Usa plugin SQLite para Grafana

Cria dashboards com base em:

Conformidade ANACOM

Download/Upload ao longo do tempo

Testes fora dos limites em horários de ponta

📬 Alertas
Configura em config.py

EMAIL_ALERT = {
    "ativo": True,
    "destinatario": "teu@email.com",
    ...
}
TELEGRAM_ALERT = {
    "ativo": True,
    "bot_token": "TEU_BOT_TOKEN",
    "chat_id": "12345678"
}

🔮 Roadmap
 Modo CLI com agendamento

 Relatório HTML

 Modo automático (headless)

 SQLite export

 Alertas (Telegram/Email)

 Painel web com Flask/Dash

 Exportação CSV para Data Studio

 Comparação entre ISPs e horários

🧑‍💻 Autor
Diogo & Jake (GPT personalizado)
Made with 💻 + ☕ in Portugal 🇵🇹


