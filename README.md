BetterLearning
==============

An online education web application created for my 3rd year Business and Enterprise module
using the <a href="http://flask.pocoo.org/">Flask</a> framework and twitter <a href="http://www.getbootstrap.com">Bootstrap</a>.

How To Run
----------

* Install flask, flask-wtf and flask-sqlalchemy

* Edit <code>config.py</code> and change the <code>SECRET_KEY</code> value to something secret

* Add an initial user:

<pre><code>
    db.create_all()
    db.session.add(models.User(username='admin', role=0, passwordHash=hashlib.sha256('yourAdminPasswordHere').hexdigest()))
    db.session.commit()
</code></pre>

* Run the <code>run.py</code> file

* Visit <code>http://localhost:5000</code> in your browser and log in with your user

Licences
--------
<a href="http://flask.pocoo.org/docs/license/">Flask</a>

<a href="http://www.apache.org/licenses/LICENSE-2.0">Bootstrap</a>
