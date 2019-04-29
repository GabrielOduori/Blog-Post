#auth/views.py
from flask import render_template, redirect, url_for, flash, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from .. import db
from ..models import User, Blog
from .forms import RegistrationForm, LoginForm, UpdateUserForm
# from .picture_processor import add_profile_pic
from app.auth import  auth


#register
@auth.route('/register',methods = ["GET","POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email = form.email.data, 
                    username = form.username.data,
                    password = form.password.data)
        db.session.add(user)
        db.session.commit()

        flash('Thanks for registering')

        return redirect(url_for('auth.login'))
        title = "New Account"
    return render_template('auth/register.html',form = form)
    
    
#login
@auth.route('/login', methods = ['GET', 'POST'])
def login():
    '''
    login function
    '''
    form  = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.check_password(form.password.data):
            login_user(user, form.remember_me.data)
            flash('Log in Success!')
            # Otherwise if a user was trying to visit a page that requires a login
            # flask saves that URL as 'next', checks if the page exists anf if not,
            # goes back to homepage.
            return redirect(request.args.get('next') or url_for('main.index'))
    title = "Log in Page"
    return render_template('auth/login.html',form = form,title=title)

#logout

@auth.route('/logout')
def logout():
    '''
    logout user
    '''
    logout_user()
    return redirect(url_for("main.index"))
    
    

#account(update UserForm)

@auth.route('/account', methods=['GET','POST'])
@login_required
def account():
    form  = UpdateUserForm()
    if form.validate_on_submit():
        if form.picture.data:
            username = current_user.username
            pic = add_profile_pic(form.picture.data, username)
            current_user.profile_image = pic
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash("User account updated")
        return redirect(url_for('auth.account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    
    profile_image = url_for('static',file_name ='profile_pics/'+curent_user.profile_image)
    return render_template('auth/account.html', profile_image = profile_image, form=form)
    

#lists of blogs
@auth.route('/<username>')
def user_post(username):
    page = request.args.get('page', 1, type = int)
    user = User.query.filter_by(username = username).first_or_404()
    blog_posts = Blog.query.filter_by(author=user).order_by(Blog.timestamp.desc()).pagenate(page=page, per_page=10)
    return render_template('user_posts.html', blog_posts = blog_posts, user = user)