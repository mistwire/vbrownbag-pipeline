from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

# Point Jinja2 at the templates folder
templates = Jinja2Templates(directory="templates")

router = APIRouter()

@router.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    # Render the template, passing in the variables it needs
    return templates.TemplateResponse(
        request=request, 
        name="index.html", 
        context={"status": "running"}
    )

@router.post("/process")
def process(title: str):
    from app.services.video import process_video
    result = process_video(title)
    return result
