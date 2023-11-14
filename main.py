from fastapi import FastAPI
from views.user_views import user_router

app = FastAPI()

user_tags_metadata = {"tags": ["User"]}

app.include_router(user_router, **user_tags_metadata)
