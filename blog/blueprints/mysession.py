from blog.blueprints.blog import blog_bp
from flask import Flask, render_template, request, redirect, url_for, flash, make_response, session

@blog_bp.route('/visit-counter/')
def visits():
    if 'visit' in session:
        session['visits'] = session.get('visits') + 1
    else:
        session['visits'] = 1
    return "Total visits:{}",format(session.get('visits'))

@blog_bp.route('/delete-visits')
def delete_visits():
    session.pop('visit', None)
    return 'visits deleted'

