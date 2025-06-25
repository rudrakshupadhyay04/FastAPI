from fastapi import FastAPI # type: ignore
from . import schema, models
from .database import engine


app = FastAPI()
models.Base.metadata.create_all(engine)



@app.post('/blog')
def create(request:schema.Blog):
    return {'title': request.title, 'body':request.body}