import pytest
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve(strict=True).parent.parent
sys.path.append(str(BASE_DIR))

from utils import *



def test_get_posts_all():
    assert type(get_posts_all()) is list, 'Фукнция должна возвращать список постов'

def test_get_posts_by_user_leo():
    posts = get_posts_by_user('leo')
    for post in posts:
        assert post['poster_name'] == 'leo', 'Пост не того автора'

def test_get_posts_by_user_ralf():
    posts = get_posts_by_user('ralf')
    assert posts == [], 'У данного пользователя нет постов'

def test_get_posts_by_user_ibragim():
    with pytest.raises(ValueError):
        get_posts_by_user('ibragim')


def test_get_comments_by_post_id_1():
    comments = get_comments_by_post_id(1)
    for com in comments:
        assert com['post_id'] == 1, 'Коммент от другого поста'

def test_get_comments_by_post_id_229():
    with pytest.raises(ValueError):
        get_comments_by_post_id(229)

def test_search_for_posts():
    assert type(search_for_posts('днем')) is list, 'Фукнция должна возвращать список постов'

def test_get_post_by_pk_1():
    assert get_post_by_pk(1)['pk'] == 1, 'Пост не с тем номером'

def test_get_post_by_pk_229():
    assert get_post_by_pk(229) == {}, 'Данного поста не существует'

