from flask import render_template, url_for, request, redirect, flash
from flask_login import current_user, login_required
from app import db
from app.models import Blog, User, Comment
from app.blogs.forms import PostForm, CommentForm
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
    return render_template('blog/post.html', title =post.title, date = post.timestamp, post = post)



@blogs.route('blog/<int:post_id>/update', methods = ['GET', 'POST'])
@login_required
def update(post_id):
    '''
    function to update post
    '''
    post = Blog.query.get_or_404(post_id)
    if post.author!=current_user:
        #403 error is forbidden
        abort(403)
    post_form  = PostForm()

    if post_form.validate_on_submit():
        post.title = post_form.title.data
        post.body = post_form.body.data
        db.session.commit()
        flash('Post Updated')
        return redirect(url_for('blogs.post', post_id=post.id))

    elif request.method == 'GET':
        post_form.title.data = post.title
        post_form.body.data = post.body

    return render_template('blog/create_post.html',title = 'Updating', post_form = post_form)


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



@blogs.route('/blog/<int:id>/comment', methods = ['GET','POST'])
@login_required
def comment(id):
    post = Blog.query.get_or_404(id)
    form_comment = CommentForm()

    if form_comment.validate_on_submit():
        comment = Comment(body = form_comment.body.data,
                            blog_id = post.id,
                          author_id= current_user.id)
        db.session.add(comment)
        db.session.commit()
        flash('Comments added successfuly!')
        return redirect(url_for('.post', id=post.id))

    from pprint import pprint
    pprint(post)
    return render_template('blog/post.html',post =post, form_comment=form_comment)
    