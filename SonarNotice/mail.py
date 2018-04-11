import smtplib
import email.mime.multipart
import email.mime.text


class Mail:
    def __init__(self):
        self.sender = 'sonar@xxxx.com'
        self.username = 'sonar'
        self.password = '******'
        self.smtp = smtplib.SMTP()
        self.smtp.connect('mail.xxxx.com')
        self.smtp.login(self.username, self.password)

    def send(self, name, to, cc, notice):
        To = ';'.join(to)
        Cc = ';'.join(cc)
        project = name

        msg = email.mime.multipart.MIMEMultipart()
        msg['From'] = '<%s>' % self.sender
        msg['To'] = To
        msg['Cc'] = Cc
        msg['Subject'] = '提醒：<%s>代码检查状态: %s' % (project, notice['status'])

        txt = email.mime.text.MIMEText(notice['body'])
        msg.attach(txt)

        # 构造附件
        # att = email.mime.text.MIMEText(open('result.xlsx', 'rb').read(), 'base64', 'utf-8')
        # att["Content-Type"] = 'application/octet-stream'
        # att["Content-Disposition"] = 'attachment; filename="result.xlsx"'
        # msg.attach(att)

        self.smtp.sendmail(self.sender, [To, Cc], msg.as_string())

    def __del__(self):
        self.smtp.quit()


if __name__ == '__main__':
    mail = Mail()
    mail.send('koss', ['saikm3@xxxx.com'], ['tongl@xxxx.com'], {
              'status': '正常', 'body': 'This is a test'})
