from flask import Flask, render_template

from view.Admin.account_view import AccountView
from view.Admin.blog_view import BlogView

app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    return render_template('client/index.html')


@app.route('/donate')
def donate():  # put application's code here
    return render_template('client/donate.html')


@app.route('/aboutus')
def aboutus():  # put application's code here
    return render_template('client/aboutus.html')


@app.route('/contact')
def contact():  # put application's code here
    return render_template('client/contact_index.html')


@app.route('/blog')
def blog():  # put application's code here
    return render_template('client/ex.html')



from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView


USERNAME_DB = 'root'
PASSWORD_DB = '123456'
NAME_DB = 'dean'
IP_DB = 'localhost'

app.config["SQLALCHEMY_DATABASE_URI"] = \
    str.format(f"mysql+pymysql://{USERNAME_DB}:{PASSWORD_DB}@{IP_DB}/{NAME_DB}?charset=utf8mb4")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["FLASK_ADMIN_FLUID_LAYOUT"] = True
app.secret_key = b'21137afa59a4dd08b708dcf106c724f9'
db = SQLAlchemy(app=app)


class AdminModel(db.Model):
    __tablename__ = 'adminn'

    admin_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(50), nullable=False)
    phonenumber = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    birthdate = db.Column(db.DateTime)
    status = db.Column(db.String(50), default=None)

    def __str__(self):
        return self.name


# class BlogModel(db.Model):
#     __tablename__ = 'blog'
#
#     blog_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     admin_id = db.Column(db.Integer, db.ForeignKey('adminn.admin_id'), nullable=False)
#     title = db.Column(db.String(50), nullable=False)
#     datecre = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)
#     image = db.Column(db.String(200), nullable=False)
#     content = db.Column(db.Text, nullable=False)
#     cateblog_id = db.Column(db.Integer, db.ForeignKey('cateblog.cateblog_id'), nullable=False)
#
#     admin = db.relationship('AdminModel', backref=db.backref('blogs', lazy=True))
#     cateblog = db.relationship('CateblogModel', backref=db.backref('blogs', lazy=True))
#
#     def __str__(self):
#         return self.title


admin = Admin(app, name='IGO')
admin.add_view(AccountView(AdminModel, db.session, name='Tài khoản'))
# admin.add_view(BlogView(BlogModel, db.session, name='Blog'))

if __name__ == '__main__':
    app.run(port=5002)

