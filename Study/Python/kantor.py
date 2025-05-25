# Wymagania:
# requests, beautifulsoup4 – do pobrania kursów.
# smtplib i email – do wysyłki e-maila.
# Konto e-mail (np. Gmail) z hasłem aplikacji.

# import requests
# import smtplib
# from email.mime.text import MIMEText
#
# # Dane logowania do wysyłki e-maila
# EMAIL_OD = "fhdyskretnaona@gmail.com"
# HASLO = "Cisco@2020"
# EMAIL_DO = "pdza60284@gmal.com"
#
# # Funkcja pobierająca kurs danej waluty z API NBP
# def pobierz_kurs(waluta):
#     url = f"https://api.nbp.pl/api/exchangerates/rates/c/{waluta}/?format=json"
#     try:
#         response = requests.get(url)
#         dane = response.json()
#         return dane['rates'][0]['bid']  # cena kupna
#     except Exception as e:
#         print(f"Błąd podczas pobierania kursu {waluta}: {e}")
#         return None
#
# # Wysyłka powiadomienia
# def wyslij_powiadomienie(kurs_usd, kurs_eur):
#     temat = "Alert walutowy: tani USD/EUR!"
#     tresc = f"Kurs USD (kupno): {kurs_usd:.2f} PLN\nKurs EUR (kupno): {kurs_eur:.2f} PLN"
#     msg = MIMEText(tresc)
#     msg["Subject"] = temat
#     msg["From"] = EMAIL_OD
#     msg["To"] = EMAIL_DO
#
#     with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
#         server.login(EMAIL_OD, HASLO)
#         server.sendmail(EMAIL_OD, EMAIL_DO, msg.as_string())
#
# # Główna logika
# kurs_usd = pobierz_kurs("USD")
# kurs_eur = pobierz_kurs("EUR")
#
# print(f"Aktualny kurs USD (kupno): {kurs_usd}")
# print(f"Aktualny kurs EUR (kupno): {kurs_eur}")
#
# if (kurs_usd is not None and kurs_usd <= 3.80) or (kurs_eur is not None and kurs_eur <= 4.30):
#     wyslij_powiadomienie(kurs_usd or 0.0, kurs_eur or 0.0)
#     print("Wysłano powiadomienie e-mail.")
# else:
#     print("Kursy nie spełniają warunków.")
# ___________________________________________________________________________________________________

import requests

# Token i chat_id z Telegrama
TELEGRAM_TOKEN = "7902109590:AAGpHkumZ7PvIFPNKIIvo3eJP8kGookq9Zk"
CHAT_ID = "8094942977"

def pobierz_kurs(waluta):
    url = f"https://api.nbp.pl/api/exchangerates/rates/c/{waluta}/?format=json"
    try:
        response = requests.get(url)
        dane = response.json()
        return dane['rates'][0]['bid']
    except Exception as e:
        print(f"Błąd podczas pobierania kursu {waluta}: {e}")
        return None

def wyslij_telegram(kurs_usd, kurs_eur):
    tresc = f"💱 Alert Walutowy:\nUSD: {kurs_usd:.2f} PLN\nEUR: {kurs_eur:.2f} PLN"
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": tresc
    }
    r = requests.post(url, data=payload)
    if r.status_code == 200:
        print("Wiadomość Telegram wysłana!")
    else:
        print("Błąd wysyłania wiadomości Telegram.")

# Główna logika
kurs_usd = pobierz_kurs("USD")
kurs_eur = pobierz_kurs("EUR")

print(f"Aktualny kurs USD (kupno): {kurs_usd}")
print(f"Aktualny kurs EUR (kupno): {kurs_eur}")

if (kurs_usd is not None and kurs_usd <= 3.80) or (kurs_eur is not None and kurs_eur <= 4.30):
    wyslij_telegram(kurs_usd or 0.0, kurs_eur or 0.0)
else:
    print("Kursy nie spełniają warunków.")
