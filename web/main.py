import json
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.responses import FileResponse  # Use this to serve a public/index.html
from simplekv.memory.redisstore import RedisStore
from simplekv.fs import FilesystemStore
import redis
from config import REDIS_HOST, REDIS_PORT, REDIS_DB, REDIS_PASS, IS_DEBUG, PORT
import uvicorn
from wordcookies import game

# init FastAPI
app = FastAPI()
app.mount("/public", StaticFiles(directory="./public"), name="public")

# init cache
# TODO: move to constant
text_domain = "wordcookies"
if REDIS_HOST == "":
    cache_path = "./cache"
    print("cache storage: file, inside %s" % cache_path)
    store = FilesystemStore(cache_path)
else:
    print("cache storage: Redis, host %s" % REDIS_HOST)
    store = RedisStore(redis.StrictRedis(REDIS_HOST, REDIS_PORT, REDIS_DB, REDIS_PASS))


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
    global text_domain

    chars = game.clean(s)
    key_name = "%s_%s" % (text_domain, "".join(chars))
    g = None

    try:
        cached_data = store.get(key_name)
        print("key_name: %s, found cached_data" % key_name)
        g = json.loads(cached_data.decode("utf8").replace("'", '"'))

    except Exception as e:
        print("key_name: %s, not found cached_data" % str(e))
        answers = game.get_possible_answers(chars)
        g = game.group(answers)

        # save cache
        store.put(key_name, json.dumps(g).encode("utf-8"))

    return {"code": 200, "message": "", "data": g}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=PORT, debug=IS_DEBUG, reload=IS_DEBUG)
