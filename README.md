# Claude Memory Skills

**Teach Claude to remember you** — with files you can see and edit.

## The Problem

Claude Desktop has built-in memory, but you can't see what it remembers or control how it learns about you. It's a black box.

## The Solution

This project gives you **transparent memory** using simple text files:

- ✅ See exactly what Claude knows about you
- ✅ Edit or delete anything
- ✅ You decide what gets saved
- ✅ Watch your preferences build up over time

## How It Works

```
Your conversations
      ↓
   "Save this to my diary"     ← You save what matters
      ↓
   Diary entries (staging)     ← Claude doesn't read these automatically
      ↓
   "Reflect on my diary"       ← You trigger pattern analysis
      ↓
   CLAUDE.md (your preferences) ← You approve what gets added
      ↓
   "Load my memory"            ← Future conversations use your preferences
```

**Nothing gets "learned" without your explicit approval.**

## Day-to-Day Usage

Once set up, you just need to remember three phrases:

| You say... | What happens |
|------------|--------------|
| **"Load my memory"** | Claude reads your preferences and adapts to you |
| **"Save this to my diary"** | Claude saves insights from your conversation |
| **"Reflect on my diary"** | Claude finds patterns and suggests updates to your preferences |

## Setup

**→ [Complete Setup Guide](SETUP.md)** ← Start here!

The guide walks you through everything step-by-step, even if you've never used Terminal before.

Setup takes about 20-30 minutes.

## What's in This Project

```
claude_memory_skills/
├── diary/                    # Skill: saves conversations to diary
├── reflect/                  # Skill: analyzes diary, updates preferences
├── memory-server-example/    # Lets Claude load your preferences
├── SETUP.md                  # Step-by-step setup guide
└── README.md                 # You are here
```

## How Your Memory Builds Up

1. **Week 1:** Save a few conversations to your diary
2. **Week 2:** Run "reflect" — Claude notices you prefer concise answers
3. **Week 3:** Run "reflect" again — Claude notices you like code examples
4. **Month 2:** Your CLAUDE.md has 10+ preferences Claude follows automatically

The more you use it, the better Claude understands how you like to work.

## Requirements

- Claude Desktop (Mac)
- Python 3.10+ (for the memory server)
- 20-30 minutes for setup

## License

MIT — use it however you want!
