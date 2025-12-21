import logging
from mcp.server.fastmcp import FastMCP

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("/tmp/emoji-mcp.log"),
    ],
)

log = logging.getLogger("emoji-mcp")

# Define a simple server called "Hello MCP"
mcp = FastMCP("Hello MCP Server")

# Register a simple tool
@mcp.tool()
def hello(name: str = "World") -> str:
    log.info("hello() called with name=%s", name)
    return f"Hello, {name}!"

if __name__ == "__main__":
    # Start the MCP server on stdout/stdin
    mcp.run()
