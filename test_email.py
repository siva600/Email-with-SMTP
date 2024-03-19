import smtplib
import email.message


def html_content():
    with open('message.html') as read_html_content:
        data = read_html_content.read()
    return data


def main():
    try:
        msg = email.message.Message()
        msg['Subject'] = 'SMTP Test email'

        # Login credentials
        msg['From'] = 'email'
        msg['To'] = 'email'
        password = "password of From email"

        msg.add_header('Content-Type', 'text/html')
        msg.set_payload(html_content())

        # create server
        s = smtplib.SMTP('smtp.gmail.com: 587')
        s.starttls()
        s.login(msg['From'], password)

        # sending message via the server
        s.sendmail(msg['From'], [msg['To']], msg.as_string())
        print("Email sent")
        s.quit()
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
