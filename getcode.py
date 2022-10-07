from imap_tools import MailBox
import re

def get_msg(email_name: str, email_password: str) -> str:
    email_url = 'imap.<some_email_service'
    regex= "\d{5}"

    with MailBox(email_url).login(email_name, email_password, '<some_email_folder') as mailbox:
        for msg in mailbox.fetch(limit=1, reverse=True):
            code = re.findall(regex, msg.subject)[0]
            return code
            
def main():
    
    email_name = '<some_login>@some_mail.com'
    email_password = '<some_password'
    
    print(get_msg(email_name, email_password))

if __name__ == '__main__':
    main()
