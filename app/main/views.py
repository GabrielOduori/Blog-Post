
#main/views.py

from flask import render_template, request, redirect, Blueprint
from app.main import main
from app.auth import auth
from app.request import get_quote

@main.route('/')
def index():
    '''
    Homepage 

    '''
    quotes = get_quote()

    return render_template('index.html', quotes = quotes)


@main.route('/info')
def info():
    '''
    Infor page
    '''
    return render_template('info.html')