#!/usr/bin/env python3
"""
Module - exercise
"""
import redis
import uuid
from typing import Union


class Cache:
    """cache in a redis storage"""
    def __init__(self, host='localhost', port=6379) -> None:
        """initialize"""
        self._redis = redis.Redis(host=host, port=port)
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int or float]) -> str:
        """store the data by setting key and data"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key