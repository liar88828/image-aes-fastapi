from typing import Annotated

from fastapi import FastAPI, Request, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware

from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from sqlmodel import SQLModel, Field, select

from controller.userDB import userDB_controller
from database.connect import create_db_and_tables, SessionDep
from database.table.userDB import UserDB
from routes import user,user_route
from schema.response import Response
from service.image import UPLOAD_FOLDER

app = FastAPI()

# noinspection PyTypeChecker
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this to specific domains in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Set up the public directory
app.mount("/public", StaticFiles(directory="public"), name="public")


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    # create spesific route
    # if request.url.path == "/some_path_to_disable_middleware":
    #     # If the request path matches the one you want to exclude,
    #     # don't run the middleware and proceed directly to the route handler.
    #     response = await call_next(request)
    # else:
    #     start_time = time.time()
    #     response = await call_next(request)
    #     process_time = time.time() - start_time
    #     response.headers["X-Process-Time"] = str(process_time)
    response = await call_next(request)
    return response


app.include_router(user.router)
app.include_router(user_route.router)


# app.include_router(auth.router)
# app.include_router(image.router)


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


@app.get("/")
async def index_test():
    return {'msg': 'hello world'}


@app.get("/public-image/")
async def list_encrypted_images():
    """Return a list of encrypted image filenames in the public folder."""
    files = [file.name for file in UPLOAD_FOLDER.glob("*.enc")]
    return JSONResponse(content=files)


@app.get("/init")
async def read_root():
    create_db_and_tables()
    return {"message": "Database session is ready"}
