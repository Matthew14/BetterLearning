from flask import render_template, redirect, session, request, flash, url_for
from forms import LoginForm
from app import app
import control as controller

@app.route('/')
@app.route('/index')
def index():
    return render_template('home.html')

@app.route('/grades')
@controller.login_required
@controller.student_required
def grades():
    return render_template('grades.html', grades=controller.getGrades())


@app.route('/grade')
@app.route('/grade/<int:gradeNo>')
@controller.login_required
@controller.student_required
def grade(gradeNo=None):
    if gradeNo:
        grade=controller.getGrade(gradeNo)
        if grade and grade.user_id == session['userId']:
            return render_template('grade.html', grade=grade)

    return redirect(url_for('grades'))


@app.route('/dashboard')
@controller.login_required
def dash():
    title = 'Welcome {}'.format(session['username'].capitalize())
    return render_template('dashTeacher.html', title=title, usertype="teacher") if session['usertype'] == 0 \
        else render_template('dashStudent.html', title=title, usertype="student", grades=controller.getNumberOfGrades(5))

@app.route('/login', methods = ['GET', 'POST'])
def login():
    error = None
    form = LoginForm()
    if form.validate_on_submit():
        if controller.login(form.nameField.data, form.pwordField.data):
            return redirect('dashboard')
        else:
            error = 'Incorrect username or password'
    elif request.method =='POST':
        error = 'All fields are required.'
    return render_template('login.html',
        title = 'Sign In',
        form = form,
        error = error)

@app.route('/logout')
@controller.login_required
def logout():
    name = session['username']
    controller.logout()
    flash('Successfully Logged Out. Goodbye, {}.'.format(name.capitalize()))
    return redirect(url_for('index'))

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html', title='Uh Oh'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run()
