"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

from app import app
from flask import render_template, request, redirect, url_for, flash
from app import app, db, login_manager
from flask_login import login_user, logout_user, current_user, login_required
from app.forms import LoginForm
from app.models import Users
from werkzeug.security import check_password_hash

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')

@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html')

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    """
    Because we use HTML5 history mode in vue-router we need to configure our
    web server to redirect all routes to index.html. Hence the additional route
    "/<path:path".

    Also we will render the initial webpage and then let VueJS take control.
    """
    return app.send_static_file('index.html')

@app.route("/login", methods=["POST"]) #This route must change to /api/auth/login
def login():
    form = LoginForm()
    if request.method == "POST" and form.validate_on_submit():
        if form.username.data:
            username = form.username.data
            password = form.password.data
            user = Users.query.filter_by(username=username).first()

            if user is not None and check_password_hash(user.password, password):
                remember = False

            if 'remember' in request.form:
                remember = True

            login_user(user, remember = remember)

            flash('Logged in successfully.', 'success')
            return redirect(url_for("home"))
    return render_template("login.html", form=form)

@app.route("/register", methods=["POST"]) 
def register():

    return render_template('register.html')

@app.route("/api/cars", methods=["GET", "POST"])    
def cars():

    render_template("cars.html")
    render_template("addcars.html")

@app.route("/api/cars/{car_id}", methods=["GET"])
def car_details(id):
    render_template("car_details.html")    

app.route("/api/cars/{car_id}/favourites")
def add_favourites(id):
    render_template("favourites.html")

app.route("/api/search")
def search():
    render_template("search.html")

app.route("/api/user/{user_id")
def profile():
    render_template("profile.html")

app.route("/api/user/{user_id}/favourites")
def favourites():
    render_template("favourites.html")




@app.route("/api/auth/logout", methods=["POST"])
@login_required
def logout():
    logout_user()

    flash('You have been logged out.', 'danger')
    return redirect(url_for('home'))

@login_manager.user_loader
def load_user(id):
    return Users.query.get(int(id))


@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")
