# FLASK INTRO

Flask is a microframework
Used for creating light web applications.

### Django

is a much older framework: full stack application (e.g., authentication included)
Follows design patterns

## COMPARISON:

Django ss like a fixed menu meal while flask is like a buffet where we can eat anything we want to

## INSTALLING FLASK AND START OF SIMPLE APPLICATION (WINDOWS)

- CREATE A FOLDER: root directory
- Create an environment inside the root. And activate

```
$ python -m virtualenv “file-name”
$ cd env/scripts
$ activate.bat
```

Back to root directory

```
$ python -m pip install flask
```

- Create a app.py file in the root directory
- Create a folder “templates” in root directory -> will hold the html files.
  -  syntax to use data passes to templates (\_ex): {{ dt.username}}
  - Loops: {% for n in data %} //html {{% data %}} {% endfor %}
  - IF: {% if condition %} /// html + code {% endif %}
-
- Inside app.py

```
from flask import Flask, render_template
app = Flask(__name__)
@app.route(“/user/<username>”)
Def user(username):
	data = { “username”: username, “isActive”: False}
	return render_template(“profile.html”, dt=data)

app.run(debug=True) # debug so we don’t have to quit and reload application
```
