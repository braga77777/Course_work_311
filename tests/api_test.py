import pytest
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve(strict=True).parent.parent
sys.path.append(str(BASE_DIR))

from app import app

def test_posts():
    response = app.test_client().get('/api/posts')
    assert response.status_code == 200
    assert type(response.json) is list, 'Апи должно возвращать список'
    key_list = ['poster_name', 'poster_avatar', 'pic', 'content', 'views_count', 'likes_count', 'pk']
    for k in key_list:
        for post in response.json:
            assert k in post, f'Нет необходимого ключа {k}'

def test_post():
    response = app.test_client().get('/api/posts/1')
    assert response.status_code == 200
    assert type(response.json) is dict, 'Апи должно возвращать словарь'
    key_list = ['poster_name', 'poster_avatar', 'pic', 'content', 'views_count', 'likes_count', 'pk']
    for k in key_list:
        assert k in response.json, f'Нет необходимого ключа {k}'