import os
import sys
from dotenv import load_dotenv

# init
env = str(os.getenv("ENV")) if os.getenv("ENV") else ""
dotenv_path = ".env" if not env else (".env.%s" % env)
print("dotenv_path", dotenv_path, file=sys.stdout)
load_dotenv(dotenv_path=dotenv_path, verbose=True)

# app
IS_DEBUG = bool(os.getenv("IS_DEBUG")) if os.getenv("IS_DEBUG") else False
PORT = int(os.getenv("PORT")) if os.getenv("PORT") else 9001

# REDIS
REDIS_HOST = os.getenv("REDIS_HOST") or ""
REDIS_PASS = os.getenv("REDIS_PASS") or ""
REDIS_PORT = int(os.getenv("REDIS_PORT")) if os.getenv("REDIS_PORT") else 6379
REDIS_DB = int(os.getenv("REDIS_DB")) if os.getenv("REDIS_DB") else 0
