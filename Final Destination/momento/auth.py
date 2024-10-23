from flask import Blueprint, render_template, redirect, request

auth = Blueprint('auth', __name__)

@auth.route('/login',  methods = ['POST', 'GET'])
def login():
    
     return render_template('home_page.html')
     
@auth.route('/signup',  methods = ['POST', 'GET'])
def signup():

     return render_template('home_page.html')