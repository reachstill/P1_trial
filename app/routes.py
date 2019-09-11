from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    '''
    view functions
    :return: html code
    '''
    user = {'username': 'Vick'}
    return render_template('index.html', title='Home', user=user)

