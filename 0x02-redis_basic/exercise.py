#!/usr/bin/env python3
"""
Module - exercise
"""
import redis
import uuid
from typing import Union, Callable, Any
import functools


def count_calls(fn: Callable) -> Callable:
    """
    decorator takes a single method argument e  
    and returns a new function that wraps 
    the original method
    """
    @functools.wraps(fn)
    def wrapper(self, *args, **kwargs) -> Any:
        """
        gets the qualified name of the method using the __qualname__ attribute
        and uses it as the Redis key to store the count of calls. 
        It then increments the count using the Redis INCR
        """
        if isinstance(self._redis, redis.Redis):
            key = fn.__qualname__
            self._redis.incr(key)
            return fn(self, *args, **kwargs)
    return wrapper

class Cache:
    """cache in a redis storage"""
    def __init__(self, host='localhost', port=6379) -> None:
        """initialize"""
        self._redis = redis.Redis(host=host, port=port)
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """store the data by setting key and data"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key, fn=None):
        """get method that take a key string argument"""
        data = self._redis.get(key)

        if fn:
            return fn(data)

        return data

    def get_str(self, key):
        """parametrize wit the correct conversion fun"""
        return self.get(key, fn=str)

    def get_int(self, key):
        """parametrize wit the correct conversion fun"""
        return self.get(key, fn=int)
