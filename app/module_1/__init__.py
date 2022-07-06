from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


def iniciar_app(config):
    app.config.from_object(config)
    return app