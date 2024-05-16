# -*- coding:utf-8 -*-
"""
@Time        :2024/5/16 下午2:25
@Author      :zhaowanpeng
@description :
"""
import time
import secrets
from jose import JWTError, jwt
from typing import Dict
from datetime import datetime, timedelta
from harmony.security.encrypt import core as encrypt_core

jwt_algorithm: str = 'HS256'
jwt_pri_key = secrets.token_urlsafe()
jwt_access_exp: int = 10 * 60
jwt_refresh_exp: int = 180 * 60


def create_token(subject: Dict, exp: int) -> str:
    """
    生成token
    :param exp:
    :param subject:需要存储到token的数据
    :return:
    """
    expires = int(time.mktime((datetime.now() + timedelta(minutes=exp)).timetuple()))
    subject.update(exp=expires)
    encoded_jwt = jwt.encode(subject, jwt_pri_key, algorithm=jwt_algorithm)
    return encoded_jwt


def jwt_decode(token, verify_exp=True):
    """
    jwt解密
    :param token:
    :param verify_exp:
    :return:
    """

    # token解密
    payload = jwt.decode(
        token,
        jwt_pri_key+"3241",
        algorithms=[jwt_algorithm],
        options={"verify_exp": verify_exp}
    )
    print(payload)
    return payload


def issuance_of_jwt(user_id, username, nickname, **kwargs):
    """
    签发jwt
    :param user:
    :return:
    """
    jid = encrypt_core.create_jid()
    jwt_data = {
        **kwargs,
        "jid": jid,
        "user_id": user_id,
        "username": username,
        "nickname": nickname,
    }

    access_token = create_token(
        subject=jwt_data,
        exp=jwt_access_exp
    )

    refresh_token = create_token(
        subject={
            "refresh_key": encrypt_core.create_hash(f"{user_id}{jid}{username}")
        },
        exp=jwt_refresh_exp
    )

    data = {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "expires_in": int(time.mktime(
            (datetime.now() + timedelta(minutes=jwt_access_exp)
             ).timetuple())),
        "token_type": "Bearer",
        "user_id": user_id,
        "username": username,
        "nickname": nickname,
        **kwargs
    }
    return data
