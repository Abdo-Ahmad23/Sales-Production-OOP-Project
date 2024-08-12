import re
class Email:

    def is_valid_email(email):
        # Define the regex pattern for a valid email address
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        
        # Match the email against the pattern
        if re.match(pattern, email):
            return True
        else:
            return False
    def check(email):
        if Email.is_valid_email(email):
            print('True')
        else:
            print('False')

# email=Email
# email.check('kjkj')
