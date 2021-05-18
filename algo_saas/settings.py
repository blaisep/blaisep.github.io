# settings.py
## importing the load_dotenv from the python-dotenv module
from dotenv import load_dotenv

from pathlib import Path
import os

## using existing module to specify location of the .env file
load_dotenv()
env_path = Path('..') / '.env'
load_dotenv(dotenv_path=env_path)

app_id = os.getenv('APP_ID')
admin_api_key = os.getenv('ADMIN_API_KEY')

