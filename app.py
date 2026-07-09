import os
from security.validation import Validator

from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    flash
)

from flask_login import (
    login_user,
    logout_user,
    login_required,
    current_user
)


from extensions import (
    db,
    bcrypt,
    login_manager
)


from models.user import User



app = Flask(__name__)


# ---------------------------
# Configuration
# ---------------------------

app.config["SECRET_KEY"] = "change-this-secret-key"

basedir = os.path.abspath(os.path.dirname(__file__))

db_dir = os.path.join(basedir, "database")

if not os.path.exists(db_dir):
    os.makedirs(db_dir)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(db_dir, "users.db")

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False



# Initialize Extensions

db.init_app(app)

bcrypt.init_app(app)

login_manager.init_app(app)


login_manager.login_view = "login"



# ---------------------------
# User Loader
# ---------------------------

@login_manager.user_loader
def load_user(user_id):

    return User.query.get(
        int(user_id)
    )



# ---------------------------
# Home Page
# ---------------------------

@app.route("/")
def home():

    return render_template(
        "index.html"
    )



# ---------------------------
# Register
# ---------------------------

@app.route(
    "/register",
    methods=["GET", "POST"]
)

def register():


    if request.method == "POST":

        username = Validator.sanitize_input(
            request.form["username"]
        )

        email = Validator.sanitize_input(
            request.form["email"]
        )

        password = request.form["password"]



        existing_user = User.query.filter_by(
            email=email
        ).first()



        if existing_user:

            flash(
                "Email already registered!",
                "danger"
            )

            return redirect(
                url_for("register")
            )



        hashed_password = bcrypt.generate_password_hash(
            password
        ).decode(
            "utf-8"
        )

        if not Validator.validate_username(username):
            flash(
                "Invalid username format",
                "danger"
            )

            return redirect(
                url_for("register")
            )

        if not Validator.validate_email(email):
            flash(
                "Invalid email address",
                "danger"
            )

            return redirect(
                url_for("register")
            )

        if not Validator.validate_password(password):
            flash(
                "Password must contain uppercase, lowercase, number and special character",
                "danger"
            )

            return redirect(
                url_for("register")
            )

        user = User(
            username=username,
            email=email,
            password=hashed_password
        )


        db.session.add(user)

        db.session.commit()



        flash(
            "Account created successfully!",
            "success"
        )


        return redirect(
            url_for("login")
        )


    return render_template(
        "register.html"
    )



# ---------------------------
# Login
# ---------------------------

@app.route(
    "/login",
    methods=["GET", "POST"]
)

def login():


    if request.method == "POST":


        email = request.form["email"]

        password = request.form["password"]



        user = User.query.filter_by(
            email=email
        ).first()



        if user and bcrypt.check_password_hash(
            user.password,
            password
        ):


            login_user(user)


            flash(
                "Login successful!",
                "success"
            )


            return redirect(
                url_for("dashboard")
            )



        else:


            flash(
                "Invalid credentials!",
                "danger"
            )



    return render_template(
        "login.html"
    )



# ---------------------------
# Dashboard
# ---------------------------

@app.route("/dashboard")

@login_required

def dashboard():

    return render_template(
        "dashboard.html",
        user=current_user
    )



# ---------------------------
# Logout
# ---------------------------

@app.route("/logout")

@login_required

def logout():

    logout_user()


    flash(
        "Logged out successfully",
        "success"
    )


    return redirect(
        url_for("login")
    )



# ---------------------------
# Create Database
# ---------------------------

with app.app_context():

    db.create_all()



# ---------------------------
# Run Application
# ---------------------------

if __name__ == "__main__":

    app.run(
        debug=True
    )