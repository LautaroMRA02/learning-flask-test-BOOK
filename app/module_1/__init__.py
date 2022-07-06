from flask import Flask

app = Flask(__name__)

def _my_function(my_arg, my_other_arg):
    """blah blah blah

    :meta public:
    """


@app.route("/")
def hello():
    return "Hello World!"


def iniciar_app(config):
    app.config.from_object(config)
    return app