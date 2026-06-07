Perfect. For your **100 Days of Python** challenge, you do **not** need to learn 50 Git commands. You need to master about **10 commands** really well.

I'll teach them in the order you'll actually use them.

---

# Mental Model First

Think of Git as having 3 areas:

```text
Working Directory
       ↓
    git add
       ↓
 Staging Area
       ↓
  git commit
       ↓
 Local Repository
       ↓
   git push
       ↓
     GitHub
```

### What these mean

**Working Directory**

* Your actual files in VS Code.
* Where you write code.

**Staging Area**

* A "shopping cart" of changes you want in the next commit.

**Local Repository**

* Git's history stored on your laptop.

**GitHub**

* Online backup and sharing platform.

---

# 1. git clone

Command:

```bash
git clone <repository-url>
```

Example:

```bash
git clone https://github.com/username/100-days-python.git
```

### What it does

Downloads the GitHub repository to your computer.

### Why needed

Without cloning:

```text
GitHub Repository
```

With cloning:

```text
GitHub Repository
        ↓
Your Laptop Copy
```

### When used

Usually only once per project.

---

# 2. git status

Command:

```bash
git status
```

### What it does

Shows Git's current situation.

### Why needed

Git tells you:

```text
Which files changed?
Which files are staged?
Which files are untracked?
```

### Example

```text
modified: Day08/solution.py

untracked: Day09/
```

This is the command professionals run constantly.

---

# 3. git add

Command:

```bash
git add .
```

or

```bash
git add Day08/
```

or

```bash
git add Day08/solution.py
```

### What it does

Moves changes into the staging area.

### Why needed

Git doesn't automatically commit everything.

You choose what goes into the next commit.

Think:

```text
Files
 ↓
git add
 ↓
Shopping Cart
```

---

# 4. git commit

Command:

```bash
git commit -m "Day 01 completed"
```

### What it does

Creates a snapshot/checkpoint.

### Why needed

Without commit:

```text
Changes exist
```

After commit:

```text
Changes permanently recorded
```

Think of saving a game.

---

# 5. git push

Command:

```bash
git push origin main
```

Later you can usually just use:

```bash
git push
```

### What it does

Uploads your commits to GitHub.

### Why needed

Before push:

```text
Laptop ✔
GitHub ✘
```

After push:

```text
Laptop ✔
GitHub ✔
```

---

# Daily Workflow

This is what you'll do 90% of the time:

```bash
git status
git add .
git commit -m "Day 10 completed"
git push
```

That's it.

---

# 6. git pull

Command:

```bash
git pull
```

### What it does

Downloads latest changes from GitHub.

### Why needed

Imagine:

```text
GitHub
  ↓
New Changes

Laptop
  ↓
Old Version
```

`git pull` updates your laptop.

### For your challenge

You'll rarely need it because you're the only contributor.

Still important to know.

---

# 7. git log

Command:

```bash
git log
```

### What it does

Shows commit history.

### Why needed

Lets you see:

```text
Day 01
Day 02
Day 03
...
```

Every commit you've ever made.

---

# 8. git diff

Command:

```bash
git diff
```

### What it does

Shows exact code changes.

### Why needed

Before committing:

```python
x = 5
```

After editing:

```python
x = 10
```

Git highlights the difference.

Useful for debugging.

---

# 9. git restore

Command:

```bash
git restore file.py
```

### What it does

Undo local changes.

### Why needed

Suppose:

```text
Day01 solution was perfect
```

You accidentally break it.

Instead of manually fixing:

```bash
git restore Day01/solution.py
```

Git returns it to the last committed version.

Very useful.

---

# 10. git rm

Command:

```bash
git rm file.py
```

### What it does

Deletes file and tells Git about it.

### Why needed

If you remove a file from the project permanently.

Not used often in your challenge.

---

# Commands You Need This Month

Memorize only these:

| Command       | Purpose             |
| ------------- | ------------------- |
| `git clone`   | Download repository |
| `git status`  | Check changes       |
| `git add`     | Stage changes       |
| `git commit`  | Save snapshot       |
| `git push`    | Upload to GitHub    |
| `git pull`    | Download updates    |
| `git log`     | View history        |
| `git diff`    | See changes         |
| `git restore` | Undo changes        |

---

# Your First Real Task

Right now:

### Step 1

Clone your repository:

```bash
git clone <your-repo-url>
```

### Step 2

Open the cloned folder in VS Code.

### Step 3

Create:

```text
Day01/
│
├── solution.py
└── notes.md
```

### Step 4

Run:

```bash
git status
```

Then come back and tell me:

**"I cloned the repo and here is the output of git status."**

We'll continue from there and you'll learn Git by actually using it instead of memorizing commands.
