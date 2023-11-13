from application import app
from application.config import CONFIG

server = CONFIG["SERVER"]

if __name__ == '__main__':
    app.run(host=server["host"], port=server["port"], debug=True)