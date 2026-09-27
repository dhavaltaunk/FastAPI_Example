from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
# from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

posts = [
    {"id": 1, "title": "First Post", "content": "This is the content of the first post."},
    {"id": 2, "title": "Second Post", "content": "This is the content of the second post."}
]

@app.get("/", include_in_schema=False)
@app.get("/posts", include_in_schema=False)
def read_root(request: Request):
    return templates.TemplateResponse(request, "home_new.html", {"posts": posts, "title": "Home"})

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}