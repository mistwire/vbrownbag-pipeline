from app.agents.description import generate_video_description
from app.agents.tags import generate_video_tags
from app.agents.linkedin import generate_linkedin_post

def process_video(title: str) -> dict:
    """
    Orchestrate video processing.
    Currently: generates a description and LinkedIn social post
    Later: Thumbnails, token tracking, etc.
    """
    try:
        description = generate_video_description(title)
        tags = generate_video_tags(title, description)
        linkedin_post = generate_linkedin_post(title, description)
        return {"title": title, "description": description, "tags": tags, "linkedin_post": linkedin_post}

    except ValueError as e:
        return {"title": title, "error": f"Something bad happened: {e}"}

    
   
        