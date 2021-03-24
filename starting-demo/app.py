from flask import Flask, redirect, url_for, request, render_template

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
    books = [
        {
            "name": "book1",
            "author": "author1",
            "description": "first description",
            "img": "https://images.unsplash.com/photo-1589998059171-988d887df646?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1055&q=80"
        },
        {
            "name": "book2",
            "author": "author2",
            "description": "second description",
            "img": "https://images.unsplash.com/photo-1589998059171-988d887df646?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1055&q=80"
        },
        {
            "name": "book3",
            "author": "author3",
            "description": "third description",
            "img": "https://images.unsplash.com/photo-1589998059171-988d887df646?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1055&q=80"
        }
        ]
    return render_template('books.html', books=books)
app.run(debug=True)