# Import libraries and dependencies
from fastapi import FastAPI, Request, status
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

from core.jinja import jinja

# Create instance from FastAPI
app = FastAPI(title="HowRU")

# Include mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")


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
    return jinja.response(request=request, name="main.html", context=context)
