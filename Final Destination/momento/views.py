from flask import Blueprint, redirect, render_template, request, Flask, session, url_for

views = Blueprint('views', __name__)

@views.route('/')
def index_page(): 
     return render_template('index.html')


