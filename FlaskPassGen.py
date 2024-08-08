from flask import Flask, render_template, request
import random
import string
import os

app = Flask(__name__)

def generate_random_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

@app.route('/', methods=['GET', 'POST'])
def index():
    password = ''
    if request.method == 'POST':
        length = int(request.form['length'])
        password = generate_random_password(length)
    return render_template('index.html', password=password)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Get the port from the environment, default to 5000
    app.run(debug=True, host='0.0.0.0', port=port)
