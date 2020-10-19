from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.responses import FileResponse  # Use this to serve a public/index.html
from config import IS_DEBUG, PORT
import uvicorn
from wordcookies import game

# init FastAPI
app = FastAPI()
app.mount("/public", StaticFiles(directory="./public"), name="public")


@app.get("/")
def read_index():
    return FileResponse("./public/index.html")


@app.get("/healthcheck")
def read_healthcheck():
    return {"message": "ok"}


@app.get("/404")
def read_404():
    return {"Not": "Found"}


@app.get("/api/solve/{s}")
def read_input(s: str):
    chars = game.clean(s)

    answers = game.get_possible_answers(chars)
    g = game.group(answers)

    return {"code": 200, "message": "", "data": g}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=PORT, debug=IS_DEBUG, reload=IS_DEBUG)
