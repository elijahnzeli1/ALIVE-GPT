import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from api import app
from config.logging_config import setup_logging

if __name__ == '__main__':
    setup_logging()
    app.run(debug=True)