from flask import Flask
from flask_cors import CORS
from persistence.db_config import get_session

from controller.memory_controller import memory_bp
from controller.cpu_controller import cpu_bp
from controller.cpu_cooler_controller import cpu_cooler_bp
from controller.gpu_controller import gpu_bp
from controller.storage_controller import storage_bp
from controller.psu_controller import psu_bp
from controller.tower_case_controller import tower_case_bp
from controller.mobo_controller import mobo_bp
from controller.auth_controller import auth_bp

from models.account import Account

app = Flask(__name__)
CORS(app)

app.register_blueprint(memory_bp)
app.register_blueprint(cpu_bp)
app.register_blueprint(cpu_cooler_bp)
app.register_blueprint(gpu_bp)
app.register_blueprint(storage_bp)
app.register_blueprint(psu_bp)
app.register_blueprint(tower_case_bp)
app.register_blueprint(mobo_bp)
app.register_blueprint(auth_bp)

if __name__ == "__main__":
    app.run(debug = True, port = 5000)

    

    #get test
    # test = component_repository.get_by_attribute(session, Memory, filters = {"form_factor" : "DDR4"})

    
