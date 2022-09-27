from flask_app import app 

#importar controlador 

from flask_app.controllers import users_controller, citas_controller

if __name__=="__main__":
    app.run(debug=True)