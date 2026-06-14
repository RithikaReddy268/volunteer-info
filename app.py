from flask import Flask, render_template, request, redirect, flash, session
import sqlite3

app = Flask(__name__)
app.secret_key = 'volunteer123'

# Create database table
def init_db():
    conn = sqlite3.connect('volunteers.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS volunteers(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT,
        phone TEXT,
        skills TEXT,
        city TEXT
    )
    ''')

    conn.commit()
    conn.close()

init_db()

@app.route('/')
def root():

    if 'admin' in session:
        return redirect('/home')

    return redirect('/login')

@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']

        if username == "admin" and password == "admin@pass":

            session['admin'] = True

            return redirect('/view')

        else:

            flash("Invalid Credentials")

    return render_template('login.html')

@app.route('/home')
def home():

    if 'admin' not in session:
        return redirect('/login')

    return render_template('index.html')


@app.route('/add', methods=['GET', 'POST'])
def add_volunteer():

    if 'admin' not in session:
        return redirect('/login')
    if request.method == 'POST':

        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        skills = request.form['skills']
        city = request.form['city']

        conn = sqlite3.connect('volunteers.db')
        cursor = conn.cursor()

        cursor.execute('''
        SELECT * FROM volunteers
        WHERE name=? AND email=? AND phone=? AND skills=? AND city=?
        ''', (name, email, phone, skills, city))

        existing_volunteer = cursor.fetchone()

        if existing_volunteer:
            conn.close()
            flash("Volunteer already exists in the system!")
            return redirect('/add')

        cursor.execute('''
        INSERT INTO volunteers(name,email,phone,skills,city)
        VALUES(?,?,?,?,?)
        ''',(name,email,phone,skills,city))

        conn.commit()
        conn.close()

        flash("Volunteer added successfully!")
        return redirect('/add')

    return render_template('add_volunteer.html')

@app.route('/view')
def view_volunteers():

    if 'admin' not in session:
        return redirect('/login')

    conn = sqlite3.connect('volunteers.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM volunteers")
    volunteers = cursor.fetchall()

    conn.close()

    return render_template(
        'view_volunteers.html',
        volunteers=volunteers
    )

@app.route('/logout')
def logout():

    session.pop('admin', None)

    return redirect('/login')

@app.route('/delete/<int:id>')
def delete_volunteer(id):

    if 'admin' not in session:
        return redirect('/login')
    conn = sqlite3.connect('volunteers.db')
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM volunteers WHERE id=?",
        (id,)
    )

    conn.commit()
    conn.close()

    return redirect('/view')

if __name__ == '__main__':
    app.run(debug=True)