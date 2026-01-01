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

mcp = FastMCP("Hello MCP Server")

@mcp.tool()
def hello(name: str = "World") -> str:
    log.info("hello() called with name=%s", name)

    emojis = get_emojis(name)

    return str(emojis)


if __name__ == "__main__":
    mcp.run()
