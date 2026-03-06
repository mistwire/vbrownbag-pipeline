import anthropic

client = anthropic.Anthropic()


def generate_linkedin_post(title: str, description: str) -> str:
    """Takes a title and description, returns a LinkedIn post."""

    try: 
        message = client.messages.create(
            model="claude-haiku-4-5",
            max_tokens=1024,
            messages=[
                {
                    "role": "user",
                    "content": f"Generate a LinkedIn post for a tech video on YouTube with the title:'{title}' with this description: {description}",
                }
            ],
        )
        first_block = message.content[0]
        assert isinstance(first_block, anthropic.types.TextBlock)
        return first_block.text
    except anthropic.AuthenticationError:
        raise ValueError("Invalid Anthropic API key - check your .env file")
    
    except anthropic.BadRequestError as e:
        raise ValueError(f"Anthropic API rejected request: {e}")
    
    except anthropic.APIConnectionError:
        raise ValueError("Could not connect to Anthropic API - check internet connection")
