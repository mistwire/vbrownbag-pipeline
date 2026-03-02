from app.agents.llm import generate_video_description

def process_video(title: str) -> dict:
    """
    Orchestrate video processing.
    Currently: generates a description.
    Later: Thumbnails, social posts, token tracking, etc.
    """

    description = generate_video_description(title)

    return {
        "title": title, 
        "description": description
    }