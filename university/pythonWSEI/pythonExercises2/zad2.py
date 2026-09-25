import smtplib

def read_config(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        return [line.strip() for line in lines]

def read_message(file_name):
    with open(file_name, 'r') as file:
        text = file.read()
        return text

def send_email(sender, receiver, subject, message, password, smtp_server, smtp_port):
    body = f"From: {sender}\nTo: {receiver}\nSubject: {subject}\n\n{message}"
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender, password)
        server.sendmail(sender, receiver, body)
        server.quit()
        print("E-mail został wysłany.")
    except Exception as e:
        print(f"Wystąpił błąd podczas wysyłania e-maila: {e}")

config_data = read_config('config.txt')
email_message = read_message('email_message.txt')

if len(config_data) == 4:
    sender_email, password, smtp_server, smtp_port = config_data
    receiver_email = '527e24de-f5e4-448b-8e65-7f915618225d@mailslurp.mx'
    email_subject = 'Topic Test'
    send_email(sender_email, receiver_email, email_subject, email_message, password, smtp_server, int(smtp_port))
else:
    print("Nie udało się odczytać wszystkich danych z pliku konfiguracyjnego.")