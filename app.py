from flask import Flask
from config import Config
from database import db
from flask_migrate import Migrate

# import blueprints
from routes.auth import auth_bp
from routes.blog import blog_bp

app = Flask(__name__)
app.config.from_object(Config)

# init extensions
db.init_app(app)
migrate = Migrate(app, db)

# register blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(blog_bp)

if __name__ == '__main__':
    app.run(debug=True)
    print("Hello")
    print("Goodbye From Justas PC")
