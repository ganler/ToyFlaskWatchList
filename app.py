import os

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

import click

app = Flask(__name__)  # File name.

app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(app.root_path, "app.sqlite")}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # 关闭对模型修改的监控
db = SQLAlchemy(app)  # Remember to do `python mkdb.py`.


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # 主键
    name = db.Column(db.String(20))  # 名字


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # 主键
    title = db.Column(db.String(60))  # 电影标题
    year = db.Column(db.String(4))  # 电影年份


@app.cli.command()  # 注册为命令
@click.option('--drop', is_flag=True, help='Create after drop.')  # 设置选项
def initdb(drop):
    """Initialize the database."""
    if drop:  # 判断是否输入了选项
        db.drop_all()
        click.echo('Old DB destroyed.')
    db.create_all()
    click.echo('New DB created.')  # 输出提示信息


@app.cli.command()
def forge():
    db.create_all()
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

    user = User(name=name)
    db.session.add(user)  # Add first, and then commit.
    for m in movies:
        movie = Movie(title=m['title'], year=m['year'])
        db.session.add(movie)

    db.session.commit()
    click.echo('Forge complete.')



@app.route('/')
def index():
    User.query.first()
    return render_template('index.html', user=User.query.first(), movies=Movie.query.all())

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
