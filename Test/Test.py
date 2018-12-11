import email, os, sys, re
import imaplib, struct, datetime

connect = imaplib.IMAP4("imap.163.com")
connect.login("zjsxcm@163.com", "Zaq123456")

connect.select("INBOX")
unseen = connect.search(None, "UnSeen")




# import poplib
# import email
# from email.parser import Parser
# from email.header import decode_header
# from email.utils import parseaddr
# import os

# def decode_str(s):
#     if s:
#         value, charset = decode_header(s)[0]
#         if charset:
#             value = value.decode(charset)
#         return value
#     else:
#         return ""
# def guess_charset(msg):
#     charset = msg.get_charset()
#     if charset is None:
#         content_type = msg.get('Content-Type', '').lower()
#         pos = content_type.find('charset=')
#         if pos >= 0:
#             charset = content_type[pos + 8:].strip()
#     return charset
 
# # indent用于缩进显示:
# def find_attachment(msg, tail):
#     attachments = []
#     for part in msg.walk():
#         fileName = part.get_filename()
#         if fileName and str.endswith(fileName, tail):
#             attachments.append(fileName)
#             data = part.get_payload(None, True)
#             fEx = open("_temp/%s"%(fileName), 'wb')
#             fEx.write(data)
#             fEx.close()
#     return attachments

# try:
#     # mail pop3 service host
#     connect = poplib.POP3("pop.163.com")
#     # set debug
#     # connect.set_debuglevel(1)
#     # identify
#     connect.user("zhengdu0303@163.com")
#     connect.pass_("Zaq123456")
#     # get all mail
#     resp, mails, octets = connect.list()

#     parser = Parser()

#     if not os.path.exists("_temp"):
#         os.mkdir("_temp")

#     print("----------------------------\nfind csv")
#     for i in range(1, len(mails) + 1):
#         resp, lines, octets = connect.retr(i)
#         rowLetter = b'\r\n'.join(lines).decode('utf-8')
#         msg = parser.parsestr(rowLetter)
        
#         attachments = find_attachment(msg, ".csv")
#         if len(attachments) > 0:
#             for header in ['From', 'To', 'Subject']:
#                 value = msg.get(header, '')
#                 if value:
#                     if header=='Subject':
#                         value = decode_str(value)
#                     else:
#                         hdr, addr = parseaddr(value)
#                         name = decode_str(hdr)
#                         value = u'%s <%s>' % (name, addr)
#                 print('%s: %s' % (header, value))
#             print("attachments:", attachments)
#     print("----------------------------\nfind png")
#     for i in range(1, len(mails) + 1):
#         resp, lines, octets = connect.retr(i)
#         rowLetter = b'\r\n'.join(lines).decode('utf-8')
#         msg = parser.parsestr(rowLetter)
        
#         attachments = find_attachment(msg, ".png")
#         if len(attachments) > 0:
#             for header in ['From', 'To', 'Subject']:
#                 value = msg.get(header, '')
#                 if value:
#                     if header=='Subject':
#                         value = decode_str(value)
#                     else:
#                         hdr, addr = parseaddr(value)
#                         name = decode_str(hdr)
#                         value = u'%s <%s>' % (name, addr)
#                 print('%s: %s' % (header, value))
#             print("attachments:", attachments)

#     connect.quit()
# except Exception as err:
#     print("failed:", str(err))