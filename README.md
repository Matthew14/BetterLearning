BetterLearning
==============

An online education web application created for my 3rd year Business and Enterprise module
using the <a href="http://flask.pocoo.org/">flask</a> framework and twitter <a href="http://www.getbootstrap.com">Bootstrap</a>.

To run:
install flask, flask-wtf and flask-sqlalchemy
edit config.py and change the <code>SECRET_KEY</code> value to something secret
add an initial user

<pre><code>
    db.session.add(models.User(    username='admin', role=0, passwordHash=hashlib.sha256('yourAdminPasswordHere').hexdigest()))
    db.session.commit()
</code></pre>
