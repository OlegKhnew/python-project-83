from flask import Flask, render_template
import os
from dotenv import load_dotenv


load_dotenv()

app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')


@app.route('/')
def index():
    title = 'АНАЛИЗАТОР СТРАНИЦ'
    return render_template('index.html', title=title)


if __name__ == '__main__':
    app.run()
