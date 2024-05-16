# -*- coding:utf-8 -*-
"""
@Time        :2024/5/16 下午2:31
@Author      :zhaowanpeng
@description :
"""
import uuid
import hashlib
from passlib.context import CryptContext

hash_context = CryptContext(schemes=["argon2"], deprecated="auto")


def create_hash(txt):
    return hash_context.hash(txt)


def verify_hash(plain_txt, hashed_txt):
    return hash_context.verify(plain_txt, hashed_txt)


def random_str():
    """
    唯一随机字符串
    :return: str
    """
    only = hashlib.md5(str(uuid.uuid1()).encode(encoding='UTF-8')).hexdigest()
    return str(only)


def create_jid():
    return create_hash(random_str())
