import imaplib
import email


def test_if_target_mail_had_received():
    imap_host = 'imap.gmail.com'
    imap_user = 'vuvandai2024'
    imap_pass = 'vlytbunwcukedemv'


    M = imaplib.IMAP4_SSL(imap_host)
    M.login(imap_user, imap_pass)
    M.select('INBOX')

    data = M.uid('search', None, '(SUBJECT "this is test from demo project")')
    print(data)
    assert "OK" == data[0]