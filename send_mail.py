

ef send_mail(text="Email Body Text", subject = "Subject of Email", to_emails = None):
    assert isinstance(to_emails, list)