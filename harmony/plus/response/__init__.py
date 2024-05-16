# -*- coding:utf-8 -*-
"""
@Time        :2024/5/16 下午3:06
@Author      :zhaowanpeng
@description :
"""
from harmony.encoders import jsonable_encoder
from harmony.responses import JSONResponse


def base_response(content,
                  http_code: int,
                  headers=None,
                  media_type=None,
                  background=None):
    """基础返回格式"""

    result = JSONResponse(
        content=content,
        status_code=http_code,
        headers=headers,
        media_type=media_type,
        background=background
    )
    return result


def fail(code=0, http_code=400, message=None, data=None, headers=None, media_type=None, background=None, **kwargs):
    """失败返回格式"""
    if data is None:
        data = {}
    content = jsonable_encoder({
        "code": code,
        "message": message,
        "data": data,
        **kwargs
    })
    return base_response(content, http_code, headers, media_type, background)


def success(code=1, http_code=200, message=None, data=None, headers=None, media_type=None, background=None, **kwargs):
    """成功返回格式"""
    if data is None:
        data = {}
    content = jsonable_encoder({
        "code": code,
        "message": message,
        "data": data,
        **kwargs
    })
    return base_response(content, http_code, headers, media_type, background)