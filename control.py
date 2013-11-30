from flask import session, flash, redirect, url_for
from functools import wraps
from app import db, models
import hashlib

def login(username, password):
    res = db.session.query(models.User).filter(models.User.username==username)
    user = res.all()

    if user and user[0].passwordHash == hashlib.sha256(password).hexdigest():
        user = user[0]
        session['logged_in'] = True
        session['username'] = user.username
        session['usertype'] = user.role
        session['userId'] = user.id
        return True

    return False

def logout():
    session.pop('logged_in', None)
    session.pop('username', None)
    session.pop('usertype', None)
    session.pop('userId', None)

def getGrades():
    return models.User.query.get(session['userId']).grades

def getQuizes():
    return models.Quiz.query.all()

def getQuestion(questionNo):
    return models.Question.query.get(questionNo)
def questionInQuiz(quizNo, questionNo):
    quiz = models.Quiz.query.get(quizNo)
    if quiz:
        for ans in quiz.questions:
            if ans.id == questionNo:
                return True
    return False
def getNumberOfGrades(num):
    #TODO: make less hacky
    res = getGrades()
    theList = []
    i = 0
    for r in res:
        if i > num - 1:
            break
        i+=1
        theList.append(r)
    return theList

def getGrade(number):
    return models.Grade.query.get(number)

def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            flash('You need to log in to view that.')
            return redirect(url_for('login'))
    return wrap

def student_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'usertype' in session and session['usertype'] == 1:
            return test(*args, **kwargs)
        else:
            flash('You need to be a student to view that.')
            return redirect(url_for('dash'))
    return wrap
