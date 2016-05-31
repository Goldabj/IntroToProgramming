import MySQLdb
from flask import Flask, request, session, g, redirect, url_for, \
        abort, render_template, flash, _app_ctx_stack

# configure the database
DATABASE = '<ADD IN OUR DATABASE>'
DEBUG = True  # FIX : set this to false once program is finished
SECRET_KEY = 'evil secret key'  # FIX: Do not show this in git
USERNAME = '<one of our users>'  # FIX: Do not show this in git
PASSWORD = '<db user password>'  # FIX: Do not show this in git

# create application
app = Flask(__name__)
app.config.from_object(__name__)  # configures values from above
app.config.from_envvar('SUBBASS_SETTINGS', silent=True)
'''this would configure the variable from the enviormental variable \
which points to a configuration file '''

def connect_db():
    """connect to the databse"""
    return MySQLdb.connect(app.config['DATABASE'])


@app.berfore_request
def before_request():
    g.user = None
    if 'user_id' in session:
        g.user = query_db('select * from user where user_id = %s',
                          [session['user_id']], one=True)

# FIX: change to mysql db
@app.teardown_request
def teardown_request(exceptoin):
    """Closes the database again at the end of the request."""
    top = _app_ctx_stack.top
    if hasattr(top, 'MySQLdb'):
        top.MySQLdb.close()


@app.route('/login', methods=['GET', 'POST'])
def login():
    if g.user:
        return redirect(url_for('user_page'))
    error = None
    if request.method == 'POST':
        user = query_db('''select * from user where
            username = %s''', [request.form['username']], one=True)
        if user is None:
            error = 'Invalid username'
        elif not check_password_hash(user['PWHash'],
                                     request.form['password']):
            error = 'Invalid password'
        else:
            flash('You were logged in')
            session['user_id'] = user['Uname']
            return redirect(url_for('user_page'))
    return render_template('login.html', error=error)


@app.route('/register', methods=['POST', 'GET'])
def register():
    """registers a new user - adds him to 
        the databse"""
    if g.user:
        return redirect(url_for('user_page'))
    error = None
    if request.method == 'POST':
        if not request.form['username']:
            error = 'You have to enter a username'
        elif not request.form['email'] or \
                '@' not in request.form['email']:
            error = 'You have to enter a valid email address'
        elif not request.form['password']:
            error = 'You have to enter a password'
        elif request.form['password'] != request.form['password2']:
            error = 'The two passwords do not match'
        elif get_user_id(request.form['username']) is not None:
            error = 'The username is already taken'
        else:
            db = get_db()
            db.execute('''insert into user (
              username, email, pw_hash) values (%s, %s, %s)''',
              [request.form['username'], request.form['email'],
                hash_password(request.form['password'])])
            db.commit()
            flash('You were successfully registered and can login now')
            return redirect(url_for('login'))
    return render_template('register.html', error=error)


@app.route('/logout')
def logout():
    """logs the user out"""
    session.pop('user_id', None)
    flash('Your were logged out')
    return redirect(url_for('login'))

def get_user_id(username):
    """Convenience method to look up the id for a username."""
    rv = query_db('select user_id from user where username = %s',
                  [username], one=True)
    return rv[0] if rv else None

def query_db(query, args=(), one=False):
    """Queries the database and returns a list of dictionaries."""
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    return (rv[0] if rv else None) if one else rv

def hash_password(password):
    hash = query_db('exec HASHBYTES(''SHA2_512'', %s)', password, one=True)
    return hash['password']

def check_password_hash(hash, password):
    return hash == hash_password(password)

# FIX: change to mySQLdatabase
def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    top = _app_ctx_stack.top
    if not hasattr(top, 'MySQLdb'):
        top.MySQLdb = MySQLdb.connect(app.config['DATABASE'])
        top.MySQLdb.row_factory = MySQLdb.Row
    return top.MySQLdb

# before requests check for session and username/password

# run program
if __name__ == '__main__':
    app.run()  # change host='ipaddr' for public access to server
