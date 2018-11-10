from flask import Flask, redirect, url_for, request, render_template, make_response, session, escape, flash
from werkzeug import secure_filename
from flask_mail import Mail, Message

app = Flask(__name__)

# # mail function in flask
# mail = Mail(app)

# app.config['MAIL_SERVER']='smtp.gmail.com'
# app.config['MAIL_PORT'] = 465
# app.config['MAIL_USERNAME'] = 'endoumamoru007@gmail.com'
# app.config['MAIL_PASSWORD'] = '*****'
# app.config['MAIL_USE_TLS'] = False
# app.config['MAIL_USE_SSL'] = True
# mail = Mail(app)

# @app.route("/")
# def index():
#         msg = Message('Hello', sender = 'adityammehs@rediff.com', recipients = ['adityammehs@rediff.com'])
#         msg.body = "Hello Flask messgae sent from Flask-Mail"
#         mail.send(msg)
#         return "Sent"

# # file uploading by flask
# @app.route('/upload')
# def upload_file():
#     return render_template('upload.html')

# @app.route('/uploader', methods = ['GET', 'POST'])
# def upload_files():
#     if request.method == 'POST':
#         f = request.files['file']
#         f.save(secure_filename(f.filename))
#         return 'File uploaded Successfully'

# # flashing message in flask
# app.secret_key = 'adi'
# @app.route('/')
# def index():
#     return render_template('index2.html')
#
# @app.route('/login', methods = ['GET', 'POST'])
# def login():
#    error = None
#  
#    if request.method == 'POST':
#       if request.form['username'] != 'admin' or request.form['password'] != 'admin':
#          error = 'Invalid username or password. Please try again!'
#       else:
#          flash('You were successfully logged in')
#          return redirect(url_for('index'))
#   
#    return render_template('login2.html', error = error)


# # session example in flask
# app.secret_key = 'adi'
# @app.route('/')
# def index():
#     if 'username' in session:
#         username = session['username']
#         return 'Logged in as ' + username + '<br>' + \
#         "<b><a href = '/logout'>click here to log out</a></b>"
#     return "You are not logged in <br><a href = '/login'></b>" + \
#       "click here to log in</b></a>"
#
# @app.route('/login', methods = ['GET', 'POST'])
# def login():
#    if request.method == 'POST':
#       session['username'] = request.form['username']
#       return redirect(url_for('index'))
#    return '''
#	
#    <form action = "" method = "post">
#       <p><input type = "text" name = "username"/></p>
#       <p<<input type = "submit" value = "Login"/></p>
#    </form>
#	
#    '''
#
# @app.route('/logout')
# def logout():
#    # remove the username from the session if it is there
#    session.pop('username', None)
#    return redirect(url_for('index'))


# # Using Cookie in Flask
# @app.route('/')
# def cookie():
#     return render_template('cookie.html')
#
# @app.route('/setcookie', methods = ['POST', 'GET'])
# def setcookie():
#    if request.method == 'POST':
#        user = request.form['nm']
#        resp = make_response(render_template('readcookie.html'))
#        resp.set_cookie('userID', user)
#        return resp
#
# @app.route('/getcookie')
# def getcookie():
#    name = request.cookies.get('userID')
#    return '<h1>welcome '+name+'</h1>'


# # Form Data to Template
# @app.route('/')
# def student():
#    return render_template('student.html')
#
# @app.route('/result',methods = ['POST', 'GET'])
# def result():
#    if request.method == 'POST':
#       result = request.form
#       return render_template("result.html",result = result)


# # Using js script in Flask
# @app.route("/")
# def index():
#    return render_template("index.html")


# # Using Jinja2 Template Engine
# @app.route('/hello/<user>')
# def hello_name(user):
#    return render_template('hello.html', name = user)
#
# @app.route('/result/<int:score>')
# def hello_name(score):
#    return render_template('hello.html', marks = score)
#
# @app.route('/result')
# def result():
#    dict = {'phy':50,'che':60,'maths':70}
#    return render_template('result.html', result = dict)


# # Checking post & get Method
# @app.route('/success/<name>')
# def success(name):
#     return 'Welcome %s ' % name
#
# @app.route('/login', methods = ['POST', 'GET'])
# def login():
#     if request.method == 'POST':
#         user = request.form['nm']
#         return redirect(url_for('success', name = user))
#     else:
#         user = request.args.get('nm')
#         return redirect(url_for('success', name = user))


# # Login as Admin or Guest
# @app.route('/admin')
# def admin():
#     return 'Hello Admin'
#
# @app.route('/guest/<guest>')
# def guest(guest):
#     return 'Hello %s as Guest' % guest
#
# @app.route('/user/<name>')
# def user(name):
#     if name == 'admin':
#         return redirect(url_for('admin'))
#     else:
#         return redirect(url_for('guest', guest=name))



# # Creating Pages
# @app.route('/home')
# def helloworld():
#     return 'Welcome to Home Page'
#
# @app.route('/about')
# def aboutus():
#     return 'Welcome to About Us'
#
# @app.route('/service')
# def service():
#     return 'Welcome to Service Page'

if __name__ == '__main__':
    app.debug = True
    app.run()
