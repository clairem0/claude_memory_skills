---
name: diary
description: Extract structured insights from the current conversation and save as a diary entry. Use when the user says "save to diary", "remember this conversation", or at the end of significant conversations.
---

# Diary Skill

Extract structured insights from the current conversation and save to `~/.claude/memory/diary/`.

## Requirements

**Environment**: Claude Desktop with filesystem MCP server enabled

**Critical**: Use the filesystem MCP tools (`write_file`, `read_file`, `list_directory`) to interact with the user's filesystem. Do NOT create downloadable artifacts - write files directly to disk using the MCP tools.

## When to Activate

- User says "save to diary", "save this conversation", "record this"
- User types /diary
- User says "remember what we discussed", "log this session"
- At the end of a significant conversation when user says "thanks", "that's all" - offer to save

## Approach: Context-First

Reflect on the conversation history to extract insights. You have access to:
- All user messages and requests
- Your responses and actions
- Topics explored and questions answered
- Decisions made and reasoning discussed
- User preferences expressed

## Diary Entry Format

Create a markdown file at `~/.claude/memory/diary/YYYY-MM-DD-session-N.md`:

```markdown
# Session Diary Entry

**Date**: YYYY-MM-DD
**Time**: HH:MM:SS

## Summary
[2-3 sentences: What was this conversation about?]

## Topics Discussed
- [Topic 1]
- [Topic 2]

## Conclusions & Actions
- Conclusions reached
- Actions taken or recommended
- Problems solved
- Ideas developed

## Decisions Made
[Document key decisions and WHY they were made]
- [Decision]: [Rationale]
- [Choice made]: [Reasoning]

## Challenges & Solutions
- Challenges encountered
- Approaches that didn't work
- Solutions that worked

## Key Insights
- Important realizations
- New understanding gained
- Connections made

## User Preferences Observed
[Document preferences for future sessions]

### Communication Preferences:
- [How user likes to interact]

### Working Style:
- [Patterns in how user approaches problems]

### Interests & Context:
- [Relevant background, interests, ongoing projects]

## Follow-ups
- Questions to revisit
- Topics to explore further
- Next steps

## Notes
[Any other observations worth remembering]
```

## Procedure

1. **Review conversation**: Reflect on what happened in this session
   - What was the user trying to accomplish or understand?
   - What conclusions were reached?
   - What decisions were made and why?
   - What preferences did the user express?

2. **Determine session number**:
   - Use `list_directory` MCP tool on `~/.claude/memory/diary/` to find files starting with today's date
   - Increment N for the next session number
   - Format: `YYYY-MM-DD-session-N.md`

3. **Create the entry**:
   - Fill in all sections with relevant content
   - Be specific - include key quotes, exact preferences
   - Focus on the "why" not just the "what"
   - Skip sections that don't apply (but include User Preferences if any were observed)

4. **Save the file**: Use `write_file` MCP tool to write to `~/.claude/memory/diary/YYYY-MM-DD-session-N.md`

5. **Confirm to user**: Tell them what was captured and where it was saved

## Guidelines

- **Be factual and specific**: Include concrete details
- **Capture the 'why'**: Explain reasoning behind decisions
- **Document ALL user preferences**: Communication style, interests, how they like to work
- **Include what didn't work**: Failed approaches are valuable learning
- **Keep it structured**: Follow the template consistently
- **Don't save literal conversation**: Extract insights, don't copy messages
- **Adapt to context**: Code sessions, research, brainstorming, planning - capture what's relevant

## Examples

**User**: "Save this to my diary"
**Action**: Review conversation, create structured entry, save to diary/

**User**: "Thanks, that's all for now"
**Action**: Offer: "Want me to save a diary entry from this conversation?"

**User**: After a brainstorming session about a project idea
**Action**: Document the ideas explored, decisions made, and next steps

**User**: After a research conversation
**Action**: Document key findings, sources discussed, and conclusions reached
