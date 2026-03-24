---
name: reflect
description: Analyze diary entries to identify patterns, synthesize insights, and propose updates to CLAUDE.md. Use when user says "reflect on diary", "what patterns have you noticed?", or periodically after several sessions.
---

# Reflect Skill

Analyze multiple diary entries to identify recurring patterns and propose updates to the user's CLAUDE.md file.

## Requirements

**Environment**: Claude Desktop with filesystem MCP server enabled

**Critical**: Use the filesystem MCP tools (`write_file`, `read_file`, `list_directory`) to interact with the user's filesystem. Do NOT create downloadable artifacts - write files directly to disk using the MCP tools.

## When to Activate

- User says "reflect on diary entries", "reflect on my sessions"
- User types /reflect
- User asks "what patterns have you noticed?"
- User says "update CLAUDE.md from diary"
- Periodically after several sessions (suggest to user)
- User asks "what have you learned about how I work?"

## Parameters (User Can Specify)

- **Date range**: "from YYYY-MM-DD to YYYY-MM-DD"
- **Entry count**: "last N entries" (default: last 10)
- **Pattern filter**: "related to [keyword]"

If no parameters provided, default to analyzing the last 10 unprocessed diary entries.

## Memory Locations

```
~/.claude/memory/
├── diary/                    # Diary entries to analyze
│   └── YYYY-MM-DD-session-N.md
└── reflections/              # Synthesized patterns
    ├── YYYY-MM-reflection-N.md
    └── processed.log         # Tracks processed entries
```

## Procedure

### 1. Check Processed Entries

Use `read_file` MCP tool on `~/.claude/memory/reflections/processed.log` to find already-processed diary entries.

Format: `[diary-filename] | [reflection-date] | [reflection-filename]`

If file doesn't exist, create it. All entries are unprocessed.

### 2. Load Diary Entries

- Use `list_directory` MCP tool on `~/.claude/memory/diary/`
- Exclude already-processed entries (unless user explicitly requests re-analysis)
- Filter by date range, count, or keyword if specified
- Use `read_file` MCP tool to read and parse each entry

### 3. Read Current CLAUDE.md

Use `read_file` MCP tool on `~/.claude/CLAUDE.md` to understand existing rules. This is CRITICAL for:
- Detecting rule violations in diary entries
- Avoiding duplicate rules
- Understanding current structure

### 4. Analyze for Patterns

**Frequency analysis**: Which preferences appear 2+ times?

**Rule violation detection**:
- Check if diary entries show violations of existing CLAUDE.md rules
- Look in "Challenges & Solutions", "User Preferences Observed"
- If a diary mentions user correcting Claude for violating an existing rule, this is HIGH PRIORITY

**Consistency check**: Are preferences consistent or contradictory?

**Abstraction**: Can specific instances be generalized into rules?

### 5. Synthesize Insights

Organize findings into categories:

**A. RULE VIOLATIONS (Highest Priority)**
- Existing CLAUDE.md rules that were violated
- These require STRENGTHENING (more explicit, moved to top, zero tolerance language)

**B. Communication Preferences (2+ occurrences)**
- How the user likes to receive information
- Tone, length, format preferences
- What they appreciate vs. find unhelpful

**C. Working Style Patterns**
- How the user approaches problems
- Decision-making style
- What kinds of support they find valuable

**D. Recurring Interests & Topics**
- Subjects that come up repeatedly
- Ongoing projects or goals
- Areas of expertise or learning

**E. Approaches That Worked**
- Conversation patterns that were effective
- Problem-solving strategies that succeeded
- Formats or structures that helped

**F. Anti-Patterns to Avoid**
- Approaches that didn't work 2+ times
- Common frustrations
- What NOT to do

**G. Context-Specific Patterns**
- Patterns for specific types of conversations (research, brainstorming, planning, coding)

### 6. Generate Reflection Document

Use `write_file` MCP tool to save to `~/.claude/memory/reflections/YYYY-MM-reflection-N.md`:

```markdown
# Reflection: [Date Range]

**Generated**: YYYY-MM-DD HH:MM:SS
**Entries Analyzed**: [count]
**Date Range**: [first-date] to [last-date]

## Summary
[2-3 paragraph overview of key insights about working with this user]

## Rule Violations Detected
[Only if violations found]

**Rule**: [The existing CLAUDE.md rule that was violated]
**Violation Pattern**: [How it appeared in diary entries]
**Frequency**: [X/Y entries showed this violation]
**Strengthening Action**: [Changes to make rule more effective]

## Patterns Identified

### Communication Preferences (2+ occurrences)

1. **[Preference Name]** (appeared in X/Y entries)
   - Observation: [What was consistently preferred]
   - CLAUDE.md rule: `- [succinct actionable rule]`

### Working Style

1. **[Pattern Name]** (appeared in X/Y entries)
   - Observation: [How user likes to work]
   - CLAUDE.md rule: `- [succinct actionable rule]`

### Anti-Patterns to Avoid

1. **[Anti-pattern Name]** (appeared in X/Y entries)
   - What didn't work: [Brief description]
   - What to do instead: [Alternative]
   - CLAUDE.md rule: `- avoid X, do Y instead`

[Continue for other categories...]

## Proposed CLAUDE.md Updates

[Succinct bullet points ready to add]

## Metadata
- Diary entries analyzed: [list of filenames]
- Topics covered: [list]
```

### 7. Propose CLAUDE.md Updates

**CRITICAL: Get user confirmation before applying changes**

Present proposed updates to user:
- List any strengthened rules (with before/after)
- List any new rules to add
- Ask for confirmation

**Format requirements for CLAUDE.md**:
- Keep updates **succinct** (one line per rule)
- Use imperative tone: "do X", "use Y", "avoid Z"
- Add context prefix when needed: "for research:", "when brainstorming:"
- No explanations - just the rule
- Group related rules together

**Good example** (succinct):
```markdown
- be direct and concise, skip unnecessary preamble
- when user asks a question, answer it first before adding context
- for research tasks: provide sources and confidence levels
```

**Bad example** (too verbose):
```markdown
- When the user asks a question, it's important to answer their
  question directly first before providing additional context,
  because this shows respect for their time...
```

### 8. Apply Updates (After Confirmation)

Only after user approves:
- Use `read_file` MCP tool to get current `~/.claude/CLAUDE.md` content
- Use `write_file` MCP tool to update `~/.claude/CLAUDE.md` with new rules
- Strengthen any violated rules
- Report what was changed

### 9. Update Processed Log

Use `read_file` MCP tool to get current content, then use `write_file` MCP tool to append to `~/.claude/memory/reflections/processed.log`:
```
[diary-filename] | [YYYY-MM-DD] | [reflection-filename]
```

One line per diary entry processed.

## Pattern Recognition Thresholds

- **Strong pattern** (add to CLAUDE.md): 3+ occurrences with consistency
- **Emerging pattern** (note in reflection): 2 occurrences
- **One-off** (document but don't add to CLAUDE.md): Single occurrence

## Quality Checks Before Proposing Updates

Before proposing a CLAUDE.md update, verify:
- ✅ Does this apply to future sessions? (not just the past)
- ✅ Is this actionable? (Claude can actually follow it)
- ✅ Is this generalizable? (not too specific to one conversation)
- ✅ Is this consistent? (doesn't contradict other patterns)
- ✅ Is this valuable? (will it improve future interactions)

## Error Handling

- If no diary entries exist: Inform user, suggest running diary skill first
- If all entries processed and no new ones: Inform user
- If fewer than 3 entries: Proceed but note low confidence
- If CLAUDE.md cannot be read: Report error but continue with reflection
- If processed.log doesn't exist: Use `write_file` MCP tool to create it with header comment

## Examples

**User**: "Reflect on my diary entries"
**Action**: Analyze last 10 unprocessed entries, generate reflection, propose CLAUDE.md updates

**User**: "What patterns have you noticed in my sessions?"
**Action**: Same as above, but frame response conversationally

**User**: "Reflect on entries related to writing"
**Action**: Filter entries for "writing" keyword, analyze patterns

**User**: "What have you learned about how I like to work?"
**Action**: Summarize key preferences and working style patterns from diary entries
