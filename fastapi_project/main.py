from typing import Optional
from xmlrpc.client import boolean
from fastapi import FastAPI, status, Response
from enum import Enum
from router import blog_get
from router import blog_post

app = FastAPI()
app.include_router(blog_get.router)
app.include_router(blog_post.router)

@app.get('/hello')
def index():
    return {'message':'Hello World' }