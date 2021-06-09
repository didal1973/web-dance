import os

from flask import Flask, render_template, request, make_response, session, redirect, abort
from flask_login import LoginManager, login_user, login_required, current_user, logout_user
# models
from data import db_session
from data.users import User
# sqlite
# import sqlite3
# forms
from forms.register_form import RegisterForm
from forms.login_form import LoginForm
# random
import random
# datetime
import datetime

# flask init
app = Flask(__name__)


# home page
@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/timetable")
def timetable():
    return render_template("timetable.html")


@app.route("/zayavka")
def zayavka():
    return render_template("zayavka.html")


@app.route("/otzev")
def otzev():
    return render_template("otzev.html")


@app.route("/napysat")
def napysat():
    return render_template("napysat.html")


@app.route("/auth")
def auth():
    return render_template("auth.html")


@app.route("/reg")
def reg():
    return render_template("reg.html")


@app.route("/raspisanie")
def raspisanie():
    return render_template("raspisanie.html")


@app.route("/adminka")
def adminka():
    return render_template("adminka.html")


@app.route("/admin-pisma")
def admin_pisma():
    return render_template("admin-pisma.html")


@app.route("/admin-otzev")
def admin_otzev():
    return render_template("admin-otzev.html")


# главная функция
def main():
    # initilize database
    # db_session.global_init("db/data.db")
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)


if __name__ == '__main__':
    main()
