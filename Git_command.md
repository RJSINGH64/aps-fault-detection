#!/bin/bash

# Check the status of the repository
echo "Checking repository status..."
git status

# Show the current branch
echo "Current branch:"
git branch

# Fetch changes from the remote repository
echo "Fetching changes from remote..."
git fetch origin

# Pull changes from the remote branch (main)
echo "Pulling changes from remote main branch..."
git pull origin main

# Add all changes to the staging area
echo "Adding changes to staging area..."
git add .

# Commit changes with a specified message
echo "Committing changes..."
git commit -m "Your commit message"

# Push changes to the remote branch (main)
echo "Pushing changes to remote main branch..."
git push origin main

# Create a new branch and switch to it
echo "Creating and switching to a new branch..."
git checkout -b new-branch

# Push the new branch to the remote repository
echo "Pushing new branch to remote..."
git push -u origin new-branch

# List all branches (local and remote)
echo "Listing all branches..."
git branch -a

# Rename the current branch
echo "Renaming the current branch..."
git branch -m new-branch-name

# Delete a local branch
echo "Deleting local branch..."
git branch -d branch-to-delete

# Force delete a local branch
echo "Force deleting local branch..."
git branch -D branch-to-delete

# Delete a remote branch
echo "Deleting remote branch..."
git push origin --delete branch-to-delete

# View commit history
echo "Viewing commit history..."
git log

# View commit history with a graph
echo "Viewing commit history with a graph..."
git log --graph --oneline --all

# Show detailed information about the last commit
echo "Showing detailed information about the last commit..."
git show HEAD

# Reset to a specific commit (use with caution)
echo "Resetting to a specific commit..."
git reset --hard commit-hash

# Create a tag
echo "Creating a tag..."
git tag -a v1.0 -m "Version 1.0"

# Push tags to the remote repository
echo "Pushing tags to remote..."
git push origin --tags