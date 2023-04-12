#!/usr/bin/env python3
"""
Module - web
"""
import redis
import requests

r = redis.Redis()


def get_page(url: str) -> str:
    """get page"""
    cached_page = r.get(url)
    if cached_page is not None:
        return cached_page.decode('utf-8')

    response = requests.get(url)
    page_content = response.content.decode('utf-8')

    r.set(url, page_content, ex=10)

    r.incr(f'count:{url}')

    return page_content
