# Import libraries and dependencies
import os
import pathlib
import random
import string

from fastapi import FastAPI, File, HTTPException, Request, UploadFile, status
from fastapi.responses import HTMLResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles

# Import cores
### also import the AI models here ASSHOLE ###
from core.jinja import jinja

# Create instance from FastAPI
app = FastAPI(title="HowRU")

# Include mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")


# Utils functions
def file_iterator(file_path: str, chunk_size: int = 1024):
    with open(file_path, mode="rb") as file:
        while chunk := file.read(chunk_size):
            yield chunk


def generate_random_string(length: int = 10) -> str:
    characters = string.ascii_letters + string.digits
    random_string = "".join(random.choice(characters) for _ in range(length))
    return random_string


# Main route for check application works
@app.get(
    path="/",
    status_code=status.HTTP_200_OK,
    description="This endpoint returns an HTML response with a message telling you if the api is working or not",
    tags=["API"],
    name="API checker",
    summary="Check if the API is live or not, just it",
    response_class=HTMLResponse,
)
async def api_check(request: Request):
    # Define veriables for output context
    message = "HowRU is alive..."

    # Context preparation
    context = {"message": message}

    # Response
    return jinja.response(request=request, name="form.html", context=context)


@app.post(
    path="/process",
    description="Upload picture and prepare that for pass to AI model for processing and send result to client",
    status_code=status.HTTP_200_OK,
    summary="Main job of whole application",
    tags=["PROCESS", "API"],
    # response_class=HTMLResponse,
    name="process",
)
async def upload_picture(request: Request, file: UploadFile = File(...)):
    # definition upload path
    main_path = os.path.dirname(os.path.abspath(__file__))
    upload_path = f"{main_path}/uploads"

    file_extension = file.filename.split(".")[-1].lower()

    if file_extension not in ["png", "jpg"]:
        raise HTTPException(
            status_code=400,
            detail="Unsupported file format. Only PNG and JPG are allowed.",
        )

    file_name = generate_random_string(10) + f".{file_extension}"

    uploaded_file_path = f"{upload_path}/{file_name}"

    # store files in upload folder
    with open(uploaded_file_path, "wb") as file_temp:
        file_temp.write(await file.read())

    # run AI methods, functions, actions whatever bullshit you want to call them

    ### ...
    ### ...
    ### ...
    ### ...

    ### put the result message into message variable
    message = "This NIGGA smiles because he sees your weird face"

    context = {"message": message, "file_name": file_name}

    return jinja.response(request=request, name="result.html", context=context)


@app.get("/file/{file_name}")
async def show_file(file_name: str):
    main_path = os.path.dirname(os.path.abspath(__file__))
    upload_path = f"{main_path}/uploads"

    file_path = pathlib.Path(f"{upload_path}/{file_name}")

    if not file_path.exists() or not file_path.is_file():
        return {"error": "File not found"}
    return StreamingResponse(
        file_iterator(file_path),
        media_type="application/octet-stream",
        headers={"Content-Disposition": f"attachment; filename={file_name}"},
    )
