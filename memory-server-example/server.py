"""Memory MCP Server - Load CLAUDE.md context into Claude Desktop conversations."""

from pathlib import Path

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Memory")


@mcp.tool()
def memory() -> str:
    """Load user preferences and context from CLAUDE.md.

    Call this tool when the user asks to "load memory", "what do you know about me",
    or wants their preferences/context loaded into the conversation.
    """
    claude_md_path = Path.home() / ".claude" / "CLAUDE.md"

    if not claude_md_path.exists():
        return "No CLAUDE.md file found at ~/.claude/CLAUDE.md"

    content = claude_md_path.read_text()
    return f"# User Context (from CLAUDE.md)\n\n{content}"


def main():
    """Entry point for the memory server."""
    mcp.run()


if __name__ == "__main__":
    main()
