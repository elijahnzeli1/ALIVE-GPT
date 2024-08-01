from api import app
from config.logging_config import setup_logging

if __name__ == '__main__':
    setup_logging()
    app.run(debug=True)