from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/hello',methods=['GET','POST'])
def hello():
    if request.method=="POST":
        name = request.form['name']
        email = request.form['email']
        site = request.form['site_url']
        comments = request.form['comments']
        return render_template(
            'done.html',
            name=name,
            email=email,
            site=site,
            comments=comments)
    return render_template('hello.html')
app.run()

