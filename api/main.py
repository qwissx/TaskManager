from fastapi import FastAPI
from profiles.router import profile_router
from tasks.router import tasks_router
from users.router import users_router

api = FastAPI(docs_url="/")

api.include_router(users_router)
api.include_router(profile_router)
api.include_router(tasks_router)