from flask import Blueprint, render_template, request, redirect, url_for, flash
from database import db
from classes.user import User

auth_bp = Blueprint('auth', __name__, url_prefix='/auth', template_folder='../templates')

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        pwd      = request.form['password']
        if User.query.filter_by(username=username).first():
            flash('Username already taken.', 'danger')
            return redirect(url_for('auth.register'))

        user = User(username, pwd)
        db.session.add(user)
        db.session.commit()
        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('auth.login'))
    return render_template('register.html')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        pwd      = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(pwd):
            flash(f'Welcome back, {user.username}!', 'success')
            return redirect(url_for('blog.index'))
        flash('Invalid credentials.', 'danger')
        return redirect(url_for('auth.login'))
    return render_template('login.html')
