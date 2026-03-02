import os
import anthropic

# init the client - reads API key automatically
client = anthropic.Anthropic()

def generate_video_description(title: str) -> str:
    """Takes a video title, returns a short desc from Claude."""

    message = client.messages.create(
        model="claude-opus-4-5",
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": f"Write a 2 sentence YouTube description for a tech video titled: {title}"
            }
        ]
    )

    # The response content is a list of blocks (TextBlock, ThinkingBlock, etc.)
    # We cast to TextBlock so the type checker knows .text is valid here
    first_block = message.content[0]
    assert isinstance(first_block, anthropic.types.TextBlock)
    return first_block.text