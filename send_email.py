from email.mime.text import MIMEText
import smtplib

def send_email(email, height, average_height, count):

    from_email = "pigeonisyourdad@gmail.com"
    from_password = "Pigeon@1969"
    to_email = email

    subject = "Height Data"

    message = "Hey , How you doin? <br><br> &nbsp; &nbsp; your height is <strong>%s</strong>. With the data of %s peoples, we have average height: <strong>%s</strong>. <br> &nbsp; &nbsp; Seems like you have a great height and you doing so good✌️. <br><br> Regards <br> <i>Pigeon</i>"%(height, count, average_height)

    msg = MIMEText(message, 'html')
    msg['Subject'] = subject
    msg['To'] = to_email
    msg['From'] = from_email

    gmail=smtplib.SMTP('smtp.gmail.com', 587)
    gmail.starttls()
    gmail.ehlo()
    gmail.login(from_email, from_password)
    gmail.send_message(msg)
