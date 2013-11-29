from app import db
import datetime

ROLE_TEACHER = 0
ROLE_STUDENT = 1

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(64), index = True, unique = True)
    passwordHash = db.Column(db.String(64))
    role = db.Column(db.SmallInteger, default = ROLE_STUDENT)
    quizes = db.relationship('Quiz', backref = 'author', lazy = 'dynamic')
    grades = db.relationship('Grade', backref = 'student', lazy = 'dynamic')

    def __repr__(self):
        return 'User: {} ({})'.format(self.username, self.role)

class Quiz(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    timestamp = db.Column(db.DateTime, default=datetime.datetime.now())
    questions = db.relationship('Question', backref = 'quiz', lazy = 'dynamic')
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return 'Quiz: {}'.format(self.id)

class Question(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    question = db.Column(db.String(256))
    answers = db.relationship('Answer', backref = 'question', lazy = 'dynamic')
    quiz_id = db.Column(db.Integer, db.ForeignKey('quiz.id'))

    def __repr__(self):
        return 'Question: {}'.format(self.question)

class Answer(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    isCorrect = db.Column(db.Boolean, default=False)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'))

    def __repr__(self):
        return 'Answer: {} to {}'.format(self.id, self.question_id)

class Grade(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    subject = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, default=datetime.datetime.now())
    grade = db.Column(db.Integer, default=0)
    comment = db.Column(db.String(256), default="No Comment.")
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return 'Grade: {}'.format(self.grade)
