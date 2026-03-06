import anthropic

client = anthropic.Anthropic()


def generate_video_tags(title: str, description: str) -> list[str]:
    """Takes a title and description, returns a list of YouTube tags."""

    try:
        message = client.messages.create(
            model="claude-haiku-4-5",
            max_tokens=1024,
            messages=[
                {
                    "role": "user",
                    "content": f"Generate 10 YouTube tags for a video titled '{title}' with this description: {description}. Return only the tags as a comma-separated list, nothing else.",
                }
            ],
        )

        # Split the comma-separated response into a clean list
        first_block = message.content[0]
        assert isinstance(first_block, anthropic.types.TextBlock)
        raw = first_block.text
        return [tag.strip() for tag in raw.split(",")]

    except anthropic.AuthenticationError:
        raise ValueError("Invalid Anthropic API key - check your .env file")
    
    except anthropic.BadRequestError as e:
        raise ValueError(f"Anthropic API rejected request: {e}")
    
    except anthropic.APIConnectionError:
        raise ValueError("Could not connect to Anthropic API - check internet connection")

