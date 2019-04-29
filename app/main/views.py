
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


        form_post = PostForm()
    if form_post.validate_on_submit():
        post = Post(body =form_post.body.data,
                    author = current_user,
                    category = form_post.category.data)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('.index'))
    posts = Post.query.order_by(Post.timestamp.desc()).all()
    return render_template('index.html', form_post = form_post, posts = posts, quotes = quotes)



@main.route('/info')
def info():
    '''
    Infor page
    '''
    return render_template('info.html')