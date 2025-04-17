from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/quiz')
def quiz():
    return render_template('quiz.html')  # this is your renamed quiz.html
@app.route('/listen')

def listen():
    return render_template('listen.html')

# You can later add:
# @app.route('/recite') for audio features

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
