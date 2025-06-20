from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
app = FastAPI()

@app.get('/')
def index():
    return 'jeyy'

@app.get('/blog/unpublished')
def unpublished():
    return {"blog":"all unpublished blogs!!!"}

@app.get('/blog/{id}')
def index(id: int):
    return {"user_id": id}

@app.get('/blog/{id}/comment')
def index(id):
    return {"user_id": id}

@app.get('/blog_page')   #http://127.0.0.1:8000/blog_page?limit=10&published=true&sort=latest
def get_blog(limit, published: bool, sort: Optional[str] = None):
    if published:
        return {"data": f"{limit} published blogs are there"}
    else:
        return {"data": f"{limit} unpublished blogs are there "}


# learning request body
class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool] | None = None

@app.post('/blog')
def create_blog(blog:Blog):
    return {"data": f'blog is creted with title as a {blog.title}'}