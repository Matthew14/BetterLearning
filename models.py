from app import db

ROLE_TEACHER = 0
ROLE_STUDENT = 1

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(64), index = True, unique = True)
    passwordHash = db.Column(db.String(64))
    role = db.Column(db.SmallInteger, default = ROLE_STUDENT)

    quizes   = db.relationship('Quiz', backref = 'author', lazy = 'dynamic')
    grades   = db.relationship('Grade', backref = 'student', lazy = 'dynamic')

    def __repr__(self):
        return 'User: {} ({})'.format(self.username, self.role)

class Quiz(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return 'Quiz: {}'.format(self.body)

class Grade(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    subject = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime)
    grade = db.Column(db.Integer)
    comment = db.Column(db.String(256))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return 'Grade: {}'.format(self.grade)
