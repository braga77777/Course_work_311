import json

def get_posts_all():
    with open('data/posts.json', 'r', encoding='utf-8') as f:
        return json.load(f)


def get_posts_by_user(user_name):
    with open('data/comments.json', 'r', encoding='utf-8') as f:
        comments =  json.load(f)   
    users_c = set([user['commenter_name'] for user in comments])
    users_p = [post['poster_name'] for post in get_posts_all()]
    users = users_c.union(users_p)
    if user_name not in users:
        raise ValueError
    else:
        user_posts = [post for post in get_posts_all() if post["poster_name"] == user_name]
        return user_posts


def get_comments_by_post_id(post_id):
    with open('data/comments.json', 'r', encoding='utf-8') as f:
        all_comm = json.load(f)
    if get_post_by_pk(post_id):
        post_comm = [comm for comm in all_comm  if comm["post_id"] == post_id]
        return post_comm
    else:
        raise ValueError

def search_for_posts(query):
    return [p for p in get_posts_all() if query.lower() in p['content'].lower()]


def get_post_by_pk(pk):
    post = [p for p in get_posts_all() if pk == p['pk']]
    if post:
        return post[0]
    else:
        return {}

