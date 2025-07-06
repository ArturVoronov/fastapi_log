import os
from dotenv import load_dotenv

load_dotenv()

HOST=os.environ.get("MAIL_HOST")
USERNAME=os.environ.get("MAIL_USERNAME")
PASSWORD=os.getenv("MAILPASSWORD")
PORT=os.environ.get("MAIL_PORT",465)

print(PASSWORD)
import os
from dotenv import load_dotenv


load_dotenv()
mypassword = os.getenv("MYPASSWORD2")
print(mypassword)