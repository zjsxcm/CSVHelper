import os
import poplib
import email
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr

class BaseDownloader():
    def Connect(self, linkInfo):
        pass  
    
    def GetMailList(self, num):
        self.mailList = []
        return -1, "发生错误"
    
    def DownloadMailAttachment(self, fileName, data):
        pass

    def Disconnect(self):
        pass

    def __init__(self):
        self.connection = None
        self.mailList = []

class Pop3Downloader(BaseDownloader):
    def Connect(self, linkInfo):
        try:
            connection = poplib.POP3(linkInfo["address"])
            # connect.set_debuglevel(1)
            connection.user(linkInfo["account"])
            connection.pass_(linkInfo["password"])
            self.connection = connection
        except Exception as err:
            return -1, "登录失败: " + str(err)
        else:
            return 1, "登录成功"

    def _decode_str(self, s):
        if s:
            value, charset = decode_header(s)[0]
            if charset:
                value = value.decode(charset)
            return value
        else:
            return ""

    def _parseMsg(self, msg):
        mail = {}
        try:
            for header in ['From', 'To', 'Subject']:
                value = msg.get(header, '')
                if value:
                    if header=='Subject':
                        value = self._decode_str(value)
                    else:
                        hdr, addr = parseaddr(value)
                        name = self._decode_str(hdr)
                        value = u'%s <%s>' % (name, addr)
                mail[header] = value
            attachments = []
            mail["Attachments"] = attachments
            i = 1
            for part in msg.walk():
                fileName = part.get_filename()
                if fileName and str.endswith(fileName, ".csv"):
                    data = part.get_payload(None, True)
                    attachments.append((i, fileName, data))
        except Exception as err:
            mail["Parsed"] = False
            mail["Err"] = "邮件解析失败:" + str(err)
        else:
            mail["Parsed"] = True
        finally:
            mail["Msg"] = msg
            mail["Read"] = False    # pop3 不支持邮件状态
            return mail

    def GetMailList(self, num):
        mailList = []
        try:
            if self.connection:
                resp, mails, octets = self.connection.list()
                mailLen = len(mails)
                num = num if mailLen > num else mailLen
                for i in range(mailLen - num + 1, mailLen + 1):
                    resp, lines, octets = self.connection.retr(i)
                    rowMsg = b'\r\n'.join(lines).decode('utf-8')
                    msg = self.parser.parsestr(rowMsg)
                    mail = self._parseMsg(msg)
                    mailList.append(mail)
            else:
                raise Exception("connection error")
        except Exception as err:
            return -1, "发生错误:" + str(err)
        else:
            self.mailList = mailList
            return 1, mailList

    def DownloadMailAttachment(self, fileName, data):
        if not os.path.exists("_temp"):
            os.mkdir("_temp")
        fEx = open("_temp/%s"%(fileName), 'wb')
        fEx.write(data)
        fEx.close()

    def Disconnect(self):
        if self.connection:
            self.connection.quit()
            self.connection = None

    def __init__(self):
        self.parser = Parser()

class ImapDownloader(BaseDownloader):
    

    def __init__(self):
        pass