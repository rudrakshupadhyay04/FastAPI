from fastapi import FastAPI

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