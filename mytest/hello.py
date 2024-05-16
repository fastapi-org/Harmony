# -*- coding:utf-8 -*-
"""
@Time        :2024/5/10 下午4:23
@Author      :zhaowanpeng
@description :
"""
from harmony import Harmony
import uvicorn

def haha():
    print(123)

def xx(func):
    print(func.__name__)
    print(321)

xx(haha)
app = Harmony()


@app.get("/")
def read_root():
    return {"Hello": "World"}


if __name__ == "__main__":
    uvicorn.run("hello:app", host="0.0.0.0", port=8000, reload=True)