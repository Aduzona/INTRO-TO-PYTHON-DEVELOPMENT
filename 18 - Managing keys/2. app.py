# this is for my local purposes only.
# .env file
# DATABASE = Sample_Connection_String

from dotenv import  load_dotenv
load_dotenv()
import os
password = os.getenv('PASSWORD')
print(password)