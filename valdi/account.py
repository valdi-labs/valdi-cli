import getpass
from dotenv import load_dotenv
import os


def configure(args):
    load_dotenv()

    email = input('Account email: ')
    pswd = getpass.getpass()

    print(f"Your email and password are: {email}, {pswd}")
    print(f"The Base URL is: {os.getenv('BASE_URL')}")
