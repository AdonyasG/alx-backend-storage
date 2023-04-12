#!/usr/bin/env python3
"""
Module - web
"""
import requests
import redis


r = redis.Redis()


def get_page(url: str) -> str:
    """get page"""
    count_key = f"count:{url}"
    content_key = f"content:{url}"
    content = r.get(content_key)

    if content:
        return content.decode('utf-8')
    else:
        response = requests.get(url)

        content = response.content.decode('utf-8')
        r.set(content_key, content, ex=10)

        r.incr(count_key)

        return content
