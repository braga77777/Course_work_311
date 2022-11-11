from flask import Flask, request, render_template, send_from_directory, jsonify
from utils import get_posts_all, get_posts_by_user, get_comments_by_post_id, search_for_posts, get_post_by_pk
import logging

app = Flask(__name__)

logging.basicConfig(filename='logs/api.log',
                    filemode='a',
                    format='%(asctime)s [%(levelname)s] %(message)s',
                    level=logging.INFO)
 

@app.errorhandler(404)
def page_not_found(e):
    return '<h1> Такой страницы не существует </h1>', 404

@app.errorhandler(500)
def page_server_error(e):
    return '<h1> Ошибка на стороне сервера </h1>', 500


@app.route('/')
def index():
    posts = get_posts_all()
    return render_template('index.html', posts=posts)


@app.route('/posts/<int:postid>')
def check_post(postid):
    post = get_post_by_pk(postid)
    if post:
        comments = get_comments_by_post_id(postid)
        return render_template('post.html', post=post, comments=comments)
    else:
        return '<h1> Поста с таким id нет.</h1>'


@app.route('/search/')
def search():
    s = request.args['s']
    posts = search_for_posts(s)
    return render_template('search.html', s=s.lower(), posts=posts)


@app.route('/users/<username>')
def user_posts(username):
    posts = get_posts_by_user(username)
    if posts:
        return render_template('user-feed.html', posts=posts)
    else:
        return '<h1> У данного пользователя нет постов </h1>'

@app.route('/api/posts')
def api_posts():
    logging.info("/api/posts")
    posts = get_posts_all()
    return jsonify(posts)

@app.route('/api/posts/<int:post_id>')
def api_post_by_id(post_id):
    logging.info("/api/posts/post_id")
    post = get_post_by_pk(post_id)
    if post:
        return jsonify(post)
    else:
        return jsonify({})


app.config['JSON_AS_ASCII'] = False
if __name__ == "__main__":
	app.run()


