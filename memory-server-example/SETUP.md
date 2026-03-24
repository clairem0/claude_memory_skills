# Memory Server — How It Works

> **Note:** If you're setting up for the first time, use the main [SETUP.md](../SETUP.md) guide. This page explains what the memory server does and how to customize it.

---

## What This Does

When you say "Load my memory" in Claude Desktop, Claude calls a tool that reads your preferences file (`~/.claude/CLAUDE.md`) and loads it into the conversation.

This file (`server.py`) is that tool — about 30 lines of Python.

---

## The Code Explained

```python
from pathlib import Path
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Memory")

@mcp.tool()
def memory() -> str:
    """Load user preferences and context from CLAUDE.md."""
    claude_md_path = Path.home() / ".claude" / "CLAUDE.md"

    if not claude_md_path.exists():
        return "No CLAUDE.md file found at ~/.claude/CLAUDE.md"

    content = claude_md_path.read_text()
    return f"# User Context (from CLAUDE.md)\n\n{content}"

def main():
    mcp.run()
```

**What each part does:**

- `FastMCP("Memory")` — Creates a server named "Memory"
- `@mcp.tool()` — Makes the function available as a tool Claude can call
- The docstring ("Load user preferences...") — Claude reads this to know when to use the tool
- `Path.home() / ".claude" / "CLAUDE.md"` — The file path to your preferences
- `mcp.run()` — Starts the server

---

## Adding Your Own Tools

Want Claude to be able to do more? Add another function with `@mcp.tool()`.

**Example: List your diary entries**

```python
@mcp.tool()
def list_diary_entries() -> str:
    """List all diary entries."""
    diary_path = Path.home() / ".claude" / "memory" / "diary"

    if not diary_path.exists():
        return "No diary folder found"

    entries = sorted(diary_path.glob("*.md"))
    return "\n".join(f"- {e.name}" for e in entries)
```

After editing, restart Claude Desktop to pick up changes.

---

## Troubleshooting

### "command not found: memory-server"

The server isn't installed in your PATH:
```bash
pip3 install --user -e .
```

### "No module named 'mcp'"

Install the MCP library:
```bash
pip3 install mcp
```

### Claude doesn't see the tool

- Fully quit Claude Desktop (Cmd+Q) and reopen
- Check `claude_desktop_config.json` has the memory server entry
- Make sure the command is exactly `"memory-server"`

---

## Learn More

- [MCP Documentation](https://modelcontextprotocol.io/)
- [FastMCP on GitHub](https://github.com/jlowin/fastmcp)
