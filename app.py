from flask import Flask, render_template

app = Flask(__name__)  # File name.

@app.route('/')
def index():
    name = 'Jiawei Liu'
    movies = [
        {'title': 'My Neighbor Totoro', 'year': '1988'},
        {'title': 'Dead Poets Society', 'year': '1989'},
        {'title': 'A Perfect World', 'year': '1993'},
        {'title': 'Leon', 'year': '1994'},
        {'title': 'Mahjong', 'year': '1996'},
        {'title': 'Swallowtail Butterfly', 'year': '1996'},
        {'title': 'King of Comedy', 'year': '1999'},
        {'title': 'Devils on the Doorstep', 'year': '1999'},
        {'title': 'WALL-E', 'year': '2008'},
        {'title': 'The Pork of Music', 'year': '2012'},
    ]
    return render_template('index.html', name=name, movies=movies)

"""
* `flask run` to run the app (w/o the __main__ function scope).
* Program discovering: flask by default assume that your app file is `[app|wsgi].py`.
 | So we may say the env var: `FLASK_APP` to tell flask which file is the app file.
 | Another env var: `FLASK_ENV` is to determine the runtime mode: 'production'/'development'.
 | Or we may leverage `python-dotenv` to determine the above two.
* You may do a template `@app.route('user/<name>')` ==> where the name var is input of the routed func.
"""

"""
{% TEMPLATE %}: Flask leverages the Jinja 2 engine.
* {{ ... }} -> variable
* {% ... %} -> keyword: if|else|endif for|endfor
* {# ... #} -> comments
* FILTER: {{ var|length }} means len(var): 
| Check more: https://jinja.palletsprojects.com/en/2.10.x/templates/#list-of-builtin-filters
* MAP: {{ var.title }} -> var['title']
--------------------------------------
Specify the template & vars by `render_template('index.html', name=name, movies=movies)`.
"""

"""
Static files
You put static files in `static` & write your template:
<img src="{{ url_for('static', filename='foo.jpg') }}">
Other than images, you can have your `.css` files written in `static` folder:
1. You want to load the .css file like:
  <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}" type="text/css">
2. Set your styles via `class="xxx"`;
"""

"""
Database
"""

if __name__ == '__main__':
    app.run(debug=True)  # Debug = True -> Print the errow in the web page.
