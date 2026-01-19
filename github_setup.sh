#!/bin/bash

# GitHub Repository Setup Script for Alpha AI Assistant
# Created by SuperNinja

echo "========================================="
echo "📦 GITHUB REPOSITORY SETUP 📦"
echo "========================================="
echo ""

# Check if git is installed
if ! command -v git &> /dev/null; then
    echo "❌ Git is not installed. Installing git..."
    pkg install git -y
fi

# Ask for GitHub username
read -p "Enter your GitHub username: " github_username

# Ask for repository name (default: alpha_ai_assistant)
read -p "Enter repository name [default: alpha_ai_assistant]: " repo_name
repo_name=${repo_name:-alpha_ai_assistant}

# Ask for GitHub token (optional)
read -p "Enter your GitHub personal access token (optional, press Enter to skip): " github_token

echo ""
echo "🔧 Configuring git..."

# Configure git user
read -p "Enter your git user name: " git_name
read -p "Enter your git email: " git_email

git config --global user.name "$git_name"
git config --global user.email "$git_email"

echo ""
echo "📁 Initializing git repository..."

# Initialize git repository
git init

# Create .gitignore
echo "📝 Creating .gitignore..."
cat > .gitignore << 'EOF'
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
ENV/
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

# Alpha AI specific
screenshots/
codes/
logs/
alpha_log.txt
screenshot.png
*.log

# Termux
.termux/
*.sh~

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
Thumbs.db

# Temporary files
*.tmp
*.temp
EOF

# Add all files to git
echo "📦 Adding files to git..."
git add .

# Commit files
echo "💾 Committing files..."
git commit -m "Initial commit: Alpha AI Assistant with female voice

Features:
- Female voice TTS
- Voice recognition
- Screen analysis
- Phone automation
- Play Store integration
- WhatsApp/Instagram messaging
- Camera access
- YouTube control
- Code generation
- Beautiful floating UI with drag-drop
- Start/Stop/Uninstall controls"

# Create repository on GitHub
echo ""
echo "🌐 Creating repository on GitHub..."
echo ""

if [ -n "$github_token" ]; then
    # Create repository using API
    curl -X POST -H "Authorization: token $github_token" \
        -H "Accept: application/vnd.github.v3+json" \
        https://api.github.com/user/repos \
        -d "{&quot;name&quot;:&quot;$repo_name&quot;,&quot;description&quot;:&quot;Alpha AI Assistant - Female Voice AI for Android&quot;,&quot;private&quot;:false}"
    
    # Add remote
    git remote add origin https://${github_token}@github.com/${github_username}/${repo_name}.git
else
    echo "⚠️ No GitHub token provided."
    echo "Please create repository manually at: https://github.com/new"
    echo "Repository name: $repo_name"
    read -p "Press Enter after creating the repository..."
    
    # Add remote
    git remote add origin https://github.com/${github_username}/${repo_name}.git
fi

# Push to GitHub
echo ""
echo "📤 Pushing to GitHub..."

# Set main branch
git branch -M main

# Push to GitHub
git push -u origin main

echo ""
echo "========================================="
echo "✅ GITHUB SETUP COMPLETE! ✅"
echo "========================================="
echo ""
echo "Repository URL: https://github.com/${github_username}/${repo_name}"
echo ""
echo "Your Alpha AI Assistant is now on GitHub!"
echo "Users can install it with:"
echo "  git clone https://github.com/${github_username}/${repo_name}.git"
echo "  cd ${repo_name}"
echo "  ./install.sh"
echo ""
echo "========================================="