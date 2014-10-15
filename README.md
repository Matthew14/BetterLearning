BetterLearning
==============

An online education web application created for my 3rd year Business and Enterprise module
using the [Flask] ("http://flask.pocoo.org/") framework and twitter [Bootstrap]("http://www.getbootstrap.com").

A live version is running [here](http://betterlearning.matthewoneill.com).

Screenshots
-----------
![grades](http://www.matthewoneill.com/uploads/grades.png)
![quiz](http://www.matthewoneill.com/uploads/quiz.png)
![mobile](http://www.matthewoneill.com/uploads/mobileView.png)

How To Run
----------

* Create a virtualenv and install from requirements.txt

* Edit <code>config.py</code> and change the <code>SECRET_KEY</code> value to something secret

* Add an initial user:

<pre><code>
    db.create_all()
    db.session.add(models.User(username='admin', role=0, passwordHash=hashlib.sha256('yourAdminPasswordHere').hexdigest()))
    db.session.commit()
</code></pre>

* Run the <code>app.py</code> file

* Visit <code>http://localhost:5000</code> in your browser and log in with your user

Licences
--------
[Flask]("http://flask.pocoo.org/docs/license/")

[Bootstrap]("http://www.apache.org/licenses/LICENSE-2.0")
