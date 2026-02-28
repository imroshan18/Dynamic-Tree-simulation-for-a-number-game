from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import Request
from decision_tree import build_tree

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

root = build_tree()
current_node = root


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/start")
def start_game():
    global current_node
    current_node = root
    return {"question": current_node.question}


@app.post("/answer/{response}")
def answer(response: str):
    global current_node

    if response == "yes":
        current_node = current_node.yes
    else:
        current_node = current_node.no

    if current_node.result:
        result = current_node.result
        current_node = root
        return {"result": result}

    return {"question": current_node.question}