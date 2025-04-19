from flask import Flask, render_template

app = Flask(__name__)

# English pages
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/quiz')
def quiz():
    return render_template('quiz.html')

@app.route('/listen')
def listen():
    return render_template('listen.html')

# Arabic pages
@app.route('/ar/')
def ar_home():
    return render_template('ar/index.html')

@app.route('/ar/quiz')
def ar_quiz():
    return render_template('ar/quiz.html')

@app.route('/ar/listen')
def ar_listen():
    return render_template('ar/listen.html')



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
