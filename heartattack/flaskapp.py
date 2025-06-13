from flask import Flask, request, render_template, redirect, url_for, session, flash
from sklearn.tree import DecisionTreeClassifier
import pickle
from datetime import datetime
from flask import request  # make sure request is imported if not already

app = Flask(__name__)
app.secret_key = "your_secret_key"

USERS = {
    'admin': '1234'
}

# In-memory user prediction history store (reset on server restart)
user_predictions = {}

model = pickle.load(open("heart_model.pkl", "rb"))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username'].strip()
        password = request.form['password'].strip()

        if username in USERS and USERS[username] == password:
            session['user'] = username
            flash('Login successful!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Invalid username or password', 'error')
            return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username'].strip()
        password = request.form['password'].strip()

        if username in USERS:
            flash('Username already exists!', 'error')
        else:
            USERS[username] = password
            flash('Registration successful! Please log in.', 'success')
            return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/logout')
def logout():
    session.pop("user", None)
    flash('Logged out successfully.', 'info')
    return redirect(url_for("login"))

@app.route('/')
def index():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template("index.html")

@app.route('/predict', methods=["POST"])
def predict():
    if 'user' not in session:
        return redirect(url_for('login'))
    try:
        data = []
        for key in request.form:
            val = request.form.get(key)
            if val is None or val.strip() == '':
                flash(f"Missing value for {key}", 'error')
                return redirect(url_for('index'))
            data.append(float(val))

        prediction = model.predict([data])[0]

        # Save prediction to user's history
        username = session['user']
        record = {
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'input': data,
            'prediction': prediction
        }
        user_predictions.setdefault(username, []).append(record)

        return render_template("result.html", prediction=prediction)
    except Exception as e:
        flash(f"Prediction error: {str(e)}", 'error')
        return redirect(url_for('index'))

@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        flash('Please login first.', 'error')
        return redirect(url_for('login'))
    return render_template('dashboard.html')

@app.route("/predict-form")
def predict_form():
    return render_template("index.html")

@app.route("/history")
def history():
    if 'user' not in session:
        flash('Please login first.', 'error')
        return redirect(url_for('login'))

    username = session['user']
    predictions = user_predictions.get(username, [])
    current_date = datetime.now().strftime("%B %d, %Y")
    return render_template("history.html", current_date=current_date, predictions=predictions)


@app.route('/clear-history', methods=['POST'])
def clear_history():
    if 'user' not in session:
        flash('Please login first.', 'error')
        return redirect(url_for('login'))
    
    username = session['user']
    if username in user_predictions:
        user_predictions[username] = []
        flash('Prediction history cleared.', 'success')
    else:
        flash('No history to clear.', 'info')
    return redirect(url_for('history'))

@app.route("/settings")
def settings():
    return render_template("settings.html")

if __name__ == "__main__":
    app.run(debug=True)

