from flask import render_template, url_for, flash, redirect
from boot_flask import app,db
from boot_flask.forms import Contact_Us, Newsletter
from boot_flask.models import Queries, Subscriber




@app.route('/query', methods=['POST'])
def queries():
    qform = Contact_Us()
    if qform.validate_on_submit():
        user = Queries(name = qform.name.data, email = qform.email.data, subject = qform.subject.data, message = qform.message.data)
        db.session.add(user)
        db.session.commit()
        flash(f'Thanks, {qform.name.data}! Will get in touch soon.','success')
        return redirect(url_for('home'))
    return render_template('index.html', qform=qform, sform=Newsletter())

@app.route('/subscribe', methods=['POST'])
def subs():
    sform= Newsletter()
    if sform.validate_on_submit():
        user = Subscriber(email = sform.email.data)
        db.session.add(user)
        db.session.commit()
        flash(f'Thank you for Subscribing!','success')
        return redirect(url_for('home'))
    return render_template('index.html', sform=sform, qform=Contact_Us())


@app.route("/",methods=['GET'])
def home():
    return render_template('index.html',qform=Contact_Us(), sform=Newsletter())




