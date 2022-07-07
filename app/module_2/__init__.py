from flask import Flask, request

app = Flask(import_name=__name__)

@app.route('/')
def index():
    return 'ok'

@app.route('/echo')
def echo():
    to_echo = request.args.get("echo", "")
    response = "{}".format(to_echo)
    res= f"{response} \n {request.args}"
    return res
            
@app.route("/echoo", methods=["POST","GET"])
def echoo():
    name = request.values.get("name", "")
    to_echo = request.values.get("echo", "")
    response = "Hey there {}! You said {}".format(name, to_echo)
    return response   



def iniciar_app2(config):
    """
    Cuando se trabaja con una aplicación web, a veces es importante acceder a los datos incluidos
    en la solicitud, más allá de la URL.

    esto se almacena en el objeto de solicitud global, al que puede acceder en su código
    a través. 

    from flask import request 
    """
    app.config.from_object(config)
    return app