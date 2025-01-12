from os import getenv
from fastapi import FastAPI
from fastapi.responses import FileResponse, PlainTextResponse
from fastapi.staticfiles import StaticFiles
from .gen_md import CVGenerator
from pathlib import Path
from urllib.parse import urlparse

app = FastAPI()

# Define the path to the static folder
static_folder = Path("./static")

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def serve_index():
    index_file = static_folder / "index.html"
    if index_file.exists():
        return FileResponse(index_file)
    return PlainTextResponse("index.html not found", status_code=404)

@app.get("/cv", response_class=PlainTextResponse)
async def get_cv():
    host_is_local = urlparse(getenv("CVHOST", "https://cv.bogv.online")).hostname in ["localhost", "127.0.0.1"]
    show_private = getenv("CV_SHOW_PRIVATE", "false").lower() == "true" or host_is_local
    cvgen = CVGenerator(
        host=getenv("CVHOST", "https://cv.bogv.online"),
        show_private=show_private
    )
    return cvgen.get_md_cv()