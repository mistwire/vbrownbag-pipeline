from app.agents.description import generate_video_description
from app.agents.tags import generate_video_tags

def process_video(title: str) -> dict:
    """
    Orchestrate video processing.
    Currently: generates a description.
    Later: Thumbnails, social posts, token tracking, etc.
    """
    try:
        description = generate_video_description(title)
        tags = generate_video_tags(title, description)
        return {"title": title, "description": description, "tags": tags}

    except ValueError as e:
        return {"title": title, "error": f"Something bad happened: {e}"}

    
   
        