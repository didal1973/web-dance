import os

from flask import Flask, render_template, request  # , make_response, session, redirect, abort
# from flask_login import LoginManager, login_user, login_required, current_user, logout_user
# models
from data import db_session

# from forms.register_form import RegisterForm
# from forms.login_form import LoginForm

# flask init
from data.classes import Hall
from data.comments import Comments
from data.days import Day
from data.direction import Direction
from data.groups import Group
from data.level import Level
from data.mail import Mail
from data.news import News
from data.statement import Statement
from data.time import Time
from data.timetable import Timetable

app = Flask(__name__)


# home page
@app.route("/")
@app.route("/index")
def index():
    news_list = []
    level_list = []
    direction_list = []
    db_sess = db_session.create_session()
    for new in db_sess.query(News).all():
        news_list.append({"title": new.title,
                          "text": new.text})
    for level in db_sess.query(Level).all():
        level_list.append({"name": level.name,
                           "text": level.text,
                           "price": level.price,
                           "image": level.image})
    for direction in db_sess.query(Direction).all():
        direction_list.append({"name": direction.name,
                               "text": direction.text,
                               "image": direction.image})
    db_sess.close()
    return render_template('index.html', news=news_list,
                           level=level_list, direction=direction_list)


@app.route("/timetable")
def timetable():
    timetable_dict = dict()
    time_dict = dict()
    classes_dict = dict()
    days_list = []
    time_list = []
    classes_list = []
    db_sess = db_session.create_session()
    for item in db_sess.query(Hall).all():
        classes_dict[item.name] = ''
        classes_list.append(item.name)
    for item in db_sess.query(Time).all():
        time_dict[item.time] = classes_dict.copy()
        time_list.append(item.time)
    for item in db_sess.query(Day).all():
        timetable_dict[item.name] = time_dict.copy()
        days_list.append(item.name)
    for item in db_sess.query(Timetable).all():
        timetable_dict[item.day.name][item.time.time][item.hall.name] = item.group.name
    db_sess.close()
    return render_template("timetable.html", days=days_list, time=time_list,
                           classes=classes_list, timetable=timetable_dict)


@app.route("/zayavka", methods=['POST', 'GET'])
def zayavka():
    if request.method == 'GET':
        return render_template("zayavka.html")
    elif request.method == 'POST':
        statement = Statement()
        statement.name = request.form['firstname']
        statement.lastname = request.form['lastname']
        statement.email = request.form['email']
        statement.day = request.form['day']
        statement.country = request.form['country']
        statement.level = request.form['level']
        db_sess = db_session.create_session()
        db_sess.add(statement)
        db_sess.commit()
        db_sess.close()
        return render_template("zayavka.html")

@app.route("/comment", methods=['POST', 'GET'])
def comment():
    if request.method == 'GET':
        db_sess = db_session.create_session()
        comments_list = []
        for comment in db_sess.query(Comments).all():
            comments_list.append({"name": comment.name + " " + comment.lastname,
                                  "date": comment.date,
                                  "text": comment.text})
        db_sess.close()
        return render_template("comment.html", comments=comments_list)
    elif request.method == 'POST':
        comment = Comments()
        comment.name = request.form['name']
        comment.text = request.form['message']
        comment.lastname = ''
        comment.date = ''
        db_sess = db_session.create_session()
        db_sess.add(comment)
        db_sess.commit()
        comments_list = []
        for comment in db_sess.query(Comments).all():
            comments_list.append({"name": comment.name + " " + comment.lastname,
                                  "date": comment.date,
                                  "text": comment.text})
        db_sess.close()
        return render_template("comment.html", comments=comments_list)


@app.route("/napysat", methods=['POST', 'GET'])
def napysat():
    if request.method == 'GET':
        return render_template("napysat.html")
    elif request.method == 'POST':
        mail = Mail()
        mail.email = request.form['email']
        mail.text = request.form['comment']
        db_sess = db_session.create_session()
        db_sess.add(mail)
        db_sess.commit()
        db_sess.close()
        return render_template("napysat.html")


@app.route("/auth")
def auth():
    return render_template("auth.html")


@app.route("/reg")
def reg():
    return render_template("reg.html")


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
    # инициализация базы данных
    db_session.global_init("db/dance_studio.db")
    # Heroku
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)


if __name__ == '__main__':
    main()
