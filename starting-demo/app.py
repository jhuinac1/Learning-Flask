from flask import Flask, redirect, url_for, request, render_template
from data.books import books as books_data
app = Flask(__name__) #name determines the name of the application, this is the main file of the application

# @app.route('/profile/<int:id>')
# def profile(id):
#     return '<h1>This is an profile page for %d</h1>' %(id)


# function to welcome the admin
# @app.route('/admin')
# def welcome_admin():
#     return "welcome admin"

# function to welcome the guest user
# @app.route('/guest/<guest>')
# def welcome_guest(guest):
#     return "welcome %s" % guest

# @app.route('/user/<name>')
# def welcome_user(name):
#     if name == 'admin':
#         return redirect(url_for('welcome_admin'))
#     else:
#         return redirect(url_for('welcome_guest', guest=name))
        
        
@app.route('/')
# def index():
#     return "this is the request made by the client <br/> %s" %request.headers

def index():
    return render_template('index.html')


@app.route('/profile/<username>')
def profile(username):
    data = {
        "username":username,
        "isActive": False
    }
    return render_template('profile.html', dt=data)

@app.route('/books')
def books():
    return render_template('books.html', books=books_data)
app.run(debug=True)