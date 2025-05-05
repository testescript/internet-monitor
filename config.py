DB_PATH = "internet_data.db"

LIMIAR_ANACOM = {
    "min100": 0.8,
    "baixo100": 0.7
}

EMAIL_ALERT = {
    "ativo": False,
    "destinatario": "teu@email.com",
    "remetente": "monitor@local",
    "servidor": "smtp.teudominio.com",
    "porta": 587,
    "login": "monitor@local",
    "senha": "password"
}

TELEGRAM_ALERT = {
    "ativo": True,
    "bot_token": "TOKEN_DO_BOT",
    "chat_id": "123456789"
}
