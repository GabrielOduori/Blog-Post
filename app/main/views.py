
#main/views.py

from flask import render_template, request, redirect, Blueprint
from app.main import main
from app.auth import auth
from app.request import get_quote
from app.models import Blog

@main.route('/')
def index():
    '''
    Homepage 

    '''

    quotes = get_quote()

    page = request.args.get('page', 1, type=int)
    posts = Blog.query.order_by(Blog.timestamp.desc()).all()
    return render_template('index.html',quotes = quotes, posts=posts)



@main.route('/info')
def info():
    '''
    Information page
    '''
    return render_template('info.html')



# Comenst view

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)
    posts = user.posts.order_by(Post.timestamp.desc()).all()
    return render_template("profile/profile.html", user = user, posts = posts)


@main.route('/post/<int:id>', methods = ['GET','POST'])
def post(id):
    post = Post.query.get_or_404
    form_comment = CommentForm()

    if form_comment.validate_on_submit():
        comment = Comment(body = form_comment.body.data,
                          post = post,
                          author = current_user)
        db.session.add(comment)
        db.session.commit()
        flash('You comments has been added.')
        return redirect(url_for('.post', id=post.id))
    return render_template('post.html',posts = post, form_comment=form_comment, comment = comment)