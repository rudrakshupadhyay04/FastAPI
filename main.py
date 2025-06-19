from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return 'jeyy'

@app.get('/helo')
def index():
    return 'jeyy hello'