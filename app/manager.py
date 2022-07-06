from module_1 import iniciar_app
from config import config


configuracion = config['development']
app = iniciar_app(configuracion)

if __name__ == "__main__":
    app.run()