from flask import (
    Flask,
    g,
    redirect,
    render_template,
    request,
    session,
    url_for
)

class user:
    def __init__(self, id, username, password): 
        self.id = id
        self.username = username
        self.password = password


    def __repr__(self):
        return f'<User: {self.username}>'


users = []
users.append(user(id = 1, username = 'Atharva', password = 'password'))
users.append(user(id = 2, username = 'Pranit', password = 'yolo'))
users.append(user(id = 3, username = 'Shikha', password = 'Beleive'))

print(users)


app = Flask(__name__)
app.secret_key = 'somesecretkeyonlyishouldknow'

@app.before_request
def before_request():
    g.user = None

    if 'user_id' in session:
        user = [x for x in users if x.id == session['user_id']][0]
        g.user = user
     


@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        session.pop('user_id', None)
        username = request.fom['username']
        password = request.fom['password']

        user = [x for x in users if x.username == username][0]
        if user and user.password == password:
            session['user_id'] = user.id
            return redirect(url_for('profile'))

        return redirect(url_for('login'))


    return render_template('login.html')

@app.route('/profile')
def profile():
    if not g.user:
        return redirect(url_for('login'))
         

    return render_template('profile.html')


