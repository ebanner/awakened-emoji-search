import base64
import logging
from mcp.server.fastmcp import FastMCP

from embeddings_model import get_emojis

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("/tmp/emoji-mcp.log"),
    ],
)

log = logging.getLogger("emoji-mcp")

mcp = FastMCP("Awakened Emoji Search MCP Server")

@mcp.tool()
def awakened_emoji_search(emoji_name: str = "World") -> str:
    log.info("awakened_emoji_search() called with emoji_name=%s", emoji_name)

    emojis = get_emojis(emoji_name)

    return str(emojis)


if __name__ == "__main__":
    mcp.run()
