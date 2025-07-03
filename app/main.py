from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_migrate import Migrate
from .config.config import config
from .database.database import db
from .routes import all_blueprints


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = config["DATABASE_URL"]
CORS(app, origins=config["CORS_ORIGINS"])

db.init_app(app)
migrate = Migrate(app, db)

for bp in all_blueprints:
    app.register_blueprint(bp)

if __name__ == "__main__":
     app.run(host="0.0.0.0", port=5000)
