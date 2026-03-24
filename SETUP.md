# Setup Guide

This guide is for **complete beginners**. No coding experience required.

---

## What You'll Be Able to Do

After setup, you can say these three things to Claude Desktop:

| You say... | What happens |
|------------|--------------|
| **"Load my memory"** | Claude reads your preferences and adapts to you |
| **"Save this to my diary"** | Claude saves key insights from your conversation |
| **"Reflect on my diary"** | Claude finds patterns and suggests preference updates |

That's it. Three phrases. The rest of this guide is just one-time setup.

---

## Before You Start

### You'll need:
- **Claude Desktop** installed on your Mac (this guide is Mac-focused)
- **20-30 minutes** for initial setup
- Willingness to copy/paste a few things into Terminal

### What's Terminal?
Terminal is an app on your Mac that lets you type commands. You'll use it a few times during setup. 

**To open Terminal:**
1. Press `Cmd + Space` (opens Spotlight search)
2. Type `Terminal`
3. Press Enter

You'll see a window with a blinking cursor. That's where you'll paste commands.

### 💡 Get help from Claude as you go

Stuck on a step? **Share this guide with Claude and ask for help!**

1. Open the `SETUP.md` file (in the folder you'll download)
2. Copy the contents
3. Paste it into a Claude Desktop conversation
4. Ask: *"Can you help me with Step 4? I'm getting an error..."*

Claude can read the guide and walk you through any step that's confusing.

---

## Step 1: Download This Project

1. Go to: **https://github.com/clairem0/claude_memory_skills**
2. Click the green **"Code"** button
3. Click **"Download ZIP"**
4. Find the downloaded file (probably in your Downloads folder)
5. Double-click to unzip it
6. You now have a folder called `claude_memory_skills-main`

**Remember where this folder is** — you'll need it later.

---

## Step 2: Enable the Filesystem Connector

Claude Desktop has a built-in way to read/write files, but it's off by default.

1. Open **Claude Desktop**
2. Click the **gear icon** (Settings)
3. Look for **"connectors"** and **"browse connectors"**
4. You'll see something called Filesystem in desktop connectors. Enable it
5. It should be allowed access to your user directory by default, but to be safe check that you allow the full path  `/Users/YOURNAME/.claude` (replace YOURNAME with your Mac username) 

> **Not sure of your username?** Open Terminal and type `whoami` then press Enter. That's your username.

---

## Step 3: Install Python (if you don't have it)

The memory server needs Python to run.

**Check if you have Python:**
1. Open Terminal
2. Paste this and press Enter:
   ```
   python3 --version
   ```

**If you see** `Python 3.10` or higher — skip to Step 4.

**If you see** "command not found" or a version below 3.10:
1. Go to [python.org/downloads](https://www.python.org/downloads/)
2. Download the latest Python for Mac
3. Run the installer
4. Restart Terminal and check again

---

## Step 4: Install the Memory Server

This is the trickiest part. We'll walk through it.

**4a. Open Terminal and go to the downloaded folder:**

First, you need to "navigate" to the memory-server-example folder. The easiest way:

1. Open **Finder**
2. Find your `claude_memory_skills-main` folder
3. Open it, then open the `memory-server-example` folder inside
4. Right-click on the folder background
5. Hold the **Option** key — you'll see **"Copy 'memory-server-example' as Pathname"**
6. Click that to copy the path

Now in Terminal:
1. Type `cd ` (with a space after it)
2. Paste the path you copied (Cmd+V)
3. Press Enter

You're now "inside" that folder in Terminal.

**4b. Install the server:**

Paste this command and press Enter:
```
pip3 install -e .
```

Wait for it to finish. You might see some text scrolling by — that's normal.

**4c. Verify it worked:**

Paste this and press Enter:
```
which memory-server
```

If you see a file path (like `/Users/yourname/.../memory-server`), it worked!

If you see nothing or an error, try:
```
pip3 install --user -e .
```

---

## Step 5: Configure Claude Desktop

You need to tell Claude Desktop about the memory server.

**5a. Open the Claude config folder:**

In Terminal, paste this and press Enter:
```
open ~/Library/Application\ Support/Claude/
```

A Finder window will open showing Claude's config folder.

**5b. Find or create the config file:**

Look for a file called `claude_desktop_config.json`.

- **If it exists:** Open it with TextEdit (right-click → Open With → TextEdit)
- **If it doesn't exist:** You'll create it in the next step

**5c. Add the memory server config:**

If the file **doesn't exist**, create a new file in TextEdit and paste this:

```json
{
  "mcpServers": {
    "memory": {
      "command": "memory-server"
    }
  }
}
```

Save it as `claude_desktop_config.json` in the Claude folder. (Make sure TextEdit doesn't add `.txt` to the end — if it asks about the extension, choose "Use .json")

If the file **already exists**, you need to add the memory server to it. Look for `"mcpServers": {` and add the memory part inside. If you're unsure, you can ask Claude to help you merge the configs!

---

## Step 6: Install the Skills

Skills are uploaded through Claude Desktop's settings — no Terminal needed for this step!

**6a. Enable code execution:**

1. Open **Claude Desktop**
2. Click the **gear icon** (Settings)
3. Go to **Capabilities**
4. Make sure **"Code execution and file creation"** is turned on

**6b. Create ZIP files for each skill:**

1. Open **Finder** and navigate to your `claude_memory_skills-main` folder
2. Find the `diary` folder
3. Right-click it → **Compress "diary"** (creates `diary.zip`)
4. Do the same for the `reflect` folder (creates `reflect.zip`)

**6c. Upload the skills:**

1. In Claude Desktop, go to **Settings > Capabilities**
2. Scroll to the **Skills** section
3. Click **"Upload skill"**
4. Select `diary.zip` and upload it
5. Click **"Upload skill"** again
6. Select `reflect.zip` and upload it
7. Make sure both skills are **toggled on**

You should now see `diary` and `reflect` in your skills list!

---

## Step 7: Create the Memory Folders

Claude needs folders to store your diary entries and reflections.

In Terminal, paste this and press Enter:
```
mkdir -p ~/.claude/memory/diary ~/.claude/memory/reflections
```

---

## Step 8: Create Your Preferences File

This is the file where Claude will store what it learns about you.

In Terminal, paste this:
```
echo "# My Preferences\n\nClaude will add to this file as it learns about you." > ~/.claude/CLAUDE.md
```

---

## Step 9: Restart Claude Desktop

**Important:** You must fully quit Claude Desktop, not just close the window.

1. Click on Claude Desktop
2. Press `Cmd + Q` (this fully quits the app)
3. Open Claude Desktop again

---

## Step 10: Test It!

Open a new conversation in Claude Desktop.

**Test 1 — Memory loading:**
> Say: "Load my memory"

Claude should respond that it found your preferences file (it'll be mostly empty for now).

**Test 2 — Diary saving:**
> Have a short chat about anything, then say: "Save this to my diary"

Claude should confirm it saved a diary entry.

**Test 3 — Reflecting:**
> Say: "Reflect on my diary"

Claude should analyze your diary entry and offer to update your preferences.

---

## You're Done! 🎉

From now on, your workflow is simple:

1. **Start conversations** you want personalized → say **"Load my memory"**
2. **After meaningful chats** → say **"Save this to my diary"**
3. **Every few diary entries** → say **"Reflect on my diary"** and approve updates

Over time, Claude will learn your preferences, communication style, and how you like to work.

---

## Troubleshooting

### "Load my memory" doesn't work

- Did you fully quit Claude Desktop (Cmd+Q) and reopen it?
- Check that `claude_desktop_config.json` exists and has the memory server config
- In Terminal, run `which memory-server` — if nothing shows, the install failed

### "Save this to my diary" doesn't work

- Check that the skills folders are in the right place
- Each folder (`diary`, `reflect`) should contain a `SKILL.md` file
- Restart Claude Desktop

### Terminal says "command not found"

- Make sure you have Python 3.10+ installed
- Try running the install command again with `pip3 install --user -e .`

### Can't find a folder or file

Hidden folders (starting with `.`) don't show in Finder by default. Press `Cmd + Shift + .` in any Finder window to show hidden files.
