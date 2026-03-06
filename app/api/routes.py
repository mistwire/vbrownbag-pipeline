from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.services.video import process_video

# Point Jinja2 at the templates folder
templates = Jinja2Templates(directory="templates")
router = APIRouter()

@router.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    # Render the template, passing in the variables it needs
    return templates.TemplateResponse(
        request=request, 
        name="index.html", 
        context={"result": None}
    )

@router.post("/process-form", response_class=HTMLResponse)
def process_form(request: Request, title: str = Form(...)):
    # Call the service layer - same as before, just from a form now
    result = process_video(title)
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"result": result}
    )
