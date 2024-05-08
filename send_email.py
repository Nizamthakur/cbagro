import smtplib
import ssl
import certifi


def send_email(massage):
    host = "smtp.gmail.com"
    port = 465

    username = "saklainnizam@gmail.com"
    password = "coniqxhjtwtmytbx"
    receiver = "waxknk1@gmail.com"

    # Create an SSL context with the path to the CA certificates
    context = ssl.create_default_context(cafile=certifi.where())
    try:
        with smtplib.SMTP_SSL(host, port, context=context) as server:
            server.login(username, password)
            server.sendmail(username, receiver, massage)
            print("Email sent successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")