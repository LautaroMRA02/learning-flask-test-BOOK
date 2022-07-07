from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')




def create_app(config):
    app.config.from_object(config)
    return app





# @app.route('/')
# def index():
#     return render_template('index.html')

# def iniciar_app3(config):
#     app.config.from_object(config)
#     return app