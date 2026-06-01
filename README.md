# 🧪 Sandbox / Test Environment

This repository is a safe space to practice Git workflows, experiment with code, and get comfortable with the pull request process. Break things, try things, learn things — that's what it's here for.

---

## Getting Started

### Clone the Repository

To pull the repo down to your local machine for the first time:

```bash
git clone https://github.com/your-org/your-repo.git
```

Then navigate into the project directory:

```bash
cd your-repo
```

If you've already cloned the repo and just want to pull down the latest changes:

```bash
git pull origin main
```

---

## Making and Pushing a Commit

### 1. Create a new branch

Always work on a new branch — don't commit directly to `main`:

```bash
git checkout -b your-branch-name
```

Use a descriptive name, e.g. `feat/add-hello-world` or `test/try-new-script`.

### 2. Make your changes

Edit, add, or delete files as needed.

### 3. Stage your changes

Stage everything:

```bash
git add .
```

Or stage specific files:

```bash
git add path/to/your/file.txt
```

### 4. Commit your changes

```bash
git commit -m "Your descriptive commit message here"
```

**Tips for good commit messages:**
- Use the imperative mood: *"Add feature"* not *"Added feature"*
- Keep it short and descriptive (under 72 characters)
- Reference an issue number if relevant: `"Fix login bug (#42)"`

### 5. Push your branch

```bash
git push origin your-branch-name
```

---

## Opening a Pull Request

Once your branch is pushed, you can open a pull request (PR) on GitHub:

1. Go to the repository on GitHub
2. Click the **"Compare & pull request"** button that appears at the top of the page, or navigate to **Pull requests → New pull request**
3. Set the **base branch** to `main` and the **compare branch** to your branch
4. Fill in the PR form:
   - **Title** — short summary of what you changed
   - **Description** — explain what you did and why; include any relevant context or screenshots
5. Click **"Create pull request"**

A maintainer (or yourself, for practice) can then review and merge the PR.

---

## Quick Reference

| Task | Command |
|------|---------|
| Clone the repo | `git clone <url>` |
| Pull latest changes | `git pull origin main` |
| Create a new branch | `git checkout -b <branch-name>` |
| Check status | `git status` |
| Stage all changes | `git add .` |
| Commit | `git commit -m "message"` |
| Push branch | `git push origin <branch-name>` |

---

## Questions?

Feel free to open an issue or ask in the team chat. No question is too basic here — this repo exists for learning! 🚀