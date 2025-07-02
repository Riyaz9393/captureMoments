from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify

# Step 1: Create the Flask app instance
app = Flask(__name__)
app.secret_key = 'Riyaz012'  # ✅ Fixed typo

# Dummy user data
users = {
    "admin": "pass",
    "demo": "tusa"
}

# Step 2: Dummy data for photographers (simulating database)
photographers = [
    {"id": "p1", "name": "Amit Lensman", "skills": ["Wedding", "Portrait"], "image": "amit.jpg"},
    {"id": "p2", "name": "Sana Clickz", "skills": ["Fashion", "Event"], "image": "sana.jpg"},
    {"id": "p3", "name": "shaiks Clickz", "skills": ["Fashion", "Event"], "image": "shaiks.jpg"},
    {"id": "p4", "name": "Bhavs Clickz", "skills": ["Fashion", "Event"], "image": "Bhavs.jpg"}
   
]

# Availability data
availability_data = {
    "p1": ["2025-06-20", "2025-06-23"],
    "p2": ["2025-06-19", "2025-06-22"],
    "p3": ["2025-07-06", "2025-07-22"],
    "p4": ["2025-07-06", "2025-07-22"],
}

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username in users and users[username] == password:
            session['user'] = username
            flash('Login successful!', 'success')  # ✅ Fixed typo
            return redirect(url_for('home'))
        else:
            flash('Invalid username or password.', 'error')
            return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/logout', methods=['POST'])  # ✅ Capitalized 'POST'
def logout():
    session.pop('user', None)
    flash('Logged out successfully.', 'success')
    return redirect(url_for('login'))

@app.route('/home')
def home():
    if 'user' not in session:
        flash("Please login first", "error")
        return redirect(url_for('login'))
    return render_template('home.html', username=session['user'])

@app.route('/show-photographers')
def show_photographers():
    if 'user' not in session:
        flash("Please login first", "error")
        return redirect(url_for('login'))
    return render_template('photographers.html', photographers=photographers, availability_data=availability_data)

@app.route('/book', methods=['GET', 'POST'])
def book():
    if 'user' not in session:
        flash("Please login first", "error")
        return redirect(url_for('login'))

    if request.method == 'POST':
        photographer_id = request.form.get('photographer_id')
        date = request.form.get('date')  # ✅ Cleaned up
        return f"<h2 style='color:green'>Booking Confirmed! For {photographer_id} on {date}.</h2>"
    return render_template('book.html', photographers=photographers)

if __name__ == '__main__':
    app.run(debug=True)