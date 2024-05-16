# -*- coding:utf-8 -*-
"""
@Time        :2024/5/10 下午7:55
@Author      :zhaowanpeng
@description :
"""
from typing import Callable, Sequence, Optional
from harmony.types import DecoratedCallable
from harmony import Security


def auth(depends: Sequence[Callable], *,
         scopes: Optional[Sequence[str]] = None,
         use_cache: bool = True,
         ) -> Callable:
    def decorator(func: DecoratedCallable) -> DecoratedCallable:
        func.depends = [Security(item, scopes=scopes, use_cache=use_cache) for item in depends]
        return func

    return decorator


class JWTAuth:

    def __init__(self, settings):
        pass

    def __call__(self, *args, **kwargs):
        # 是否有token

        # jwt解码,是否成功？

        # jwt是否已经被强制下线? redis中被删除

        # 用户存在吗

        # 用户封禁、注销、

        pass


# 限流，检查这个请求是否还在redis

class Permission:

    def __init__(self):
        pass
        # 用户角色是否具有权限

        # 限制在某些ip登录
