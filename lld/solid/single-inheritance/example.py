"""
The file for the single inheritance 
"""

"""

If a Class has many responsibilities, it increases the possibility of bugs because making changes to one of its responsibilities, could affect the other ones without you knowing.

Goal

This principle aims to separate behaviours so that if bugs arise as a result of your change, it wont affect other unrelated behaviours.
"""

class UserManager():
    
    """
    The problem here is has both method have send and create user
    """

    def create_user(self,name):

        print(f"User has been created {name}")

    def send_email(self,messgae):

        print(f"The email has been sent {messgae}")



class CreateUser():

    def create_user(self,name):

        print(f"User has been created {name}")

class EmailSender():

    def send_email(self,message):

        print(f"Send the email -- {message}")

