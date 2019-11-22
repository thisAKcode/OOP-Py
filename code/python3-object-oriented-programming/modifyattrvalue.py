# moidifying attr based on some behaviour
class Email:
    def __init__(self):
        self.is_sent = False
    def send_email(self): # method that updates the is_sent var to True
        self.is_sent = True
        
my_email = Email()
my_email.is_sent # False 
my_email.send_email()
my_email.is_sent # True 
