from flask import Flask, send_from_directory

app = Flask(__name__, static_folder='frontend')

@app.route('/')
def home():
    return send_from_directory('frontend', 'login.html')

@app.route('/login')
def login():
    return send_from_directory('frontend', 'login.html')

@app.route('/signup')
def signup():
    return send_from_directory('frontend', 'signup.html')

if __name__ == '__main__':
    app.run(debug=True)

