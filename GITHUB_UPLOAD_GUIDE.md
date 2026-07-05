# Step-by-Step Guide to Upload to GitHub

## Prerequisites
- GitHub account (create one at https://github.com if you don't have)
- Git installed on your Mac (check with `git --version`)

## Steps to Upload Your Project

### Step 1: Create a New Repository on GitHub
1. Go to https://github.com/new
2. Enter repository name: `sentiment-analysis` (or your preferred name)
3. Add description: "Tweet Sentiment Analysis using LSTM"
4. Choose visibility: **Public** (for GitHub portfolios) or **Private**
5. Click "Create repository"
6. **Copy the repository URL** (you'll need it in Step 3)

### Step 2: Initialize Git in Your Local Project
Open Terminal and navigate to your project:

```bash
cd /Users/yogesh/c0DE/bproject\ pratice/sentiment
```

Initialize git repository:

```bash
git init
```

### Step 3: Add Your Files to Git
Add all files:

```bash
git add .
```

Or add specific files:

```bash
git add app.py sentiment_lstm_model.h5 tokenizer.pkl label_encoder.pkl README.md requirements.txt Sentiment_analysis_2.ipynb
```

### Step 4: Create First Commit
```bash
git commit -m "Initial commit: Sentiment analysis LSTM model with Streamlit app"
```

### Step 5: Add Remote Repository
Replace `YOUR_USERNAME` and `REPOSITORY_NAME` with your GitHub username and repo name:

```bash
git remote add origin https://github.com/YOUR_USERNAME/REPOSITORY_NAME.git
```

Example:
```bash
git remote add origin https://github.com/yogesh/sentiment-analysis.git
```

### Step 6: Rename Branch to Main (if needed)
```bash
git branch -M main
```

### Step 7: Push to GitHub
```bash
git push -u origin main
```

You may be asked to authenticate. Use one of these options:

#### Option A: Personal Access Token (Recommended)
1. Go to GitHub Settings → Developer settings → Personal access tokens
2. Generate new token with `repo` scope
3. Copy the token
4. When prompted for password, paste the token

#### Option B: SSH Key
1. Generate SSH key: `ssh-keygen -t ed25519 -C "your_email@example.com"`
2. Add to GitHub settings
3. Use SSH URL instead: `git@github.com:YOUR_USERNAME/REPOSITORY_NAME.git`

---

## Complete Terminal Commands

Run these commands in sequence:

```bash
# Navigate to project
cd /Users/yogesh/c0DE/bproject\ pratice/sentiment

# Initialize git
git init

# Add all files
git add .

# Create commit
git commit -m "Initial commit: Sentiment analysis LSTM model with Streamlit app"

# Add remote (replace with your details)
git remote add origin https://github.com/YOUR_USERNAME/sentiment-analysis.git

# Rename branch
git branch -M main

# Push to GitHub
git push -u origin main
```

---

## After Upload: Making Updates

For future changes:

```bash
# Make changes to files

# Add changes
git add .

# Commit
git commit -m "Description of your changes"

# Push
git push
```

---

## Verify Upload

Visit `https://github.com/YOUR_USERNAME/sentiment-analysis` to see your repository!

## Troubleshooting

**Error: "fatal: could not read Username"**
- Use Personal Access Token instead of password
- Or set up SSH keys

**Error: "repository already exists"**
- You may have already pushed. Try: `git push -u origin main`

**Error: "Permission denied"**
- Check your authentication method (token/SSH)
- Make sure repository is set to public

---

## Optional: Add .gitignore

Create `.gitignore` file to exclude unnecessary files:

```bash
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Virtual environment
sentiment_env/
venv/

# IDE
.vscode/
.idea/
*.swp
*.swo

# Jupyter
.ipynb_checkpoints/

# OS
.DS_Store
```

Then add and commit:
```bash
git add .gitignore
git commit -m "Add .gitignore file"
git push
```

