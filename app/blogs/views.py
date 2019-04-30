from flask import render_template, url_for, request, redirect, flash
from flask_login import current_user, login_required
from app import db
from app.models import Blog, User
from app.blogs.forms import PostForm
from app.blogs import blogs



# CREATE A BLOG

@blogs.route('/create', methods = ['GET', 'POST'])
@login_required
def create_post():
    post_form = PostForm()
    if post_form.validate_on_submit():
        post = Blog(title = post_form.title.data,
                    body = post_form.body.data,
                    user_id = current_user.id)
        db.session.add(post)
        db.session.commit()
        flash('Post saved')
        return redirect(url_for('main.index'))
    return render_template('blog/create_post.html', post_form=post_form)


# VIEW A POST
@blogs.route('blog/<int:post_id>')
def post(post_id):
    post = Blog.query.get_or_404(post_id)
    return render_template('user_post.html', title =post.title, date = post.timestamp, post = post)

# UPDATE


@blogs.route('blog/<int:post_id>/update', methods = ['GET', 'POST'])
@login_required
def update(post_id):
    post = Blog.query.get_or_404(post_id)
    if post.author!=current_user:
        #403 error is forbidden
        abort(403)
    form  = PostForm()

    if form.validate_on_submit():
        post.title = form.title.data
        post.body = form.body.data
        db.session.commit()
        flash('Post Updated')
        return render_template('blog/posts.post', post_id = post.id)

    elif request.method == 'GET':
        form.title.data = post.title
        form.body.data = post.body

    return render_template('blog/create_post.html',title = 'Updating', form = form)


@blogs.route('blog/<int:post_id>/delete', methods = ['GET', 'POST'])
@login_required
def delete_post(post_id):
    post = Blog.query.get_or_404(post_id)
    if post.author!=current_user:
        abort(403)

    db.session.delete(post)
    db.session.commit()

    flash('Post deleted.')
    return redirect(url_for('main.index'))
