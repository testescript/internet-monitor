from config import EMAIL_ALERT, TELEGRAM_ALERT
import smtplib
import requests

def alerta_email(mensagem):
    if not EMAIL_ALERT["ativo"]:
        return
    try:
        with smtplib.SMTP(EMAIL_ALERT["servidor"], EMAIL_ALERT["porta"]) as server:
            server.starttls()
            server.login(EMAIL_ALERT["login"], EMAIL_ALERT["senha"])
            msg = f"Subject: ALERTA DE CONFORMIDADE\n\n{mensagem}"
            server.sendmail(EMAIL_ALERT["remetente"], EMAIL_ALERT["destinatario"], msg)
    except Exception as e:
        print(f"Erro email: {e}")

def alerta_telegram(mensagem):
    if not TELEGRAM_ALERT["ativo"]:
        return
    try:
        url = f"https://api.telegram.org/bot{TELEGRAM_ALERT['bot_token']}/sendMessage"
        requests.post(url, data={"chat_id": TELEGRAM_ALERT["chat_id"], "text": mensagem})
    except Exception as e:
        print(f"Erro Telegram: {e}")
