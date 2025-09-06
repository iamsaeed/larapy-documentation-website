#!/bin/bash

# Install git hook for automatic package updates
# Run this from the documentation website directory

echo "🔗 Installing Git Hook for Automatic Package Updates"
echo "===================================================="

# Check if we're in the right directory
if [ ! -f "simple_update.py" ]; then
    echo "❌ Please run this script from the documentation website directory"
    exit 1
fi

# Check if package directory exists
PACKAGE_DIR="../package-larapy"
if [ ! -d "$PACKAGE_DIR" ]; then
    echo "❌ Package directory not found: $PACKAGE_DIR"
    exit 1
fi

# Check if package has git repository
PACKAGE_GIT_DIR="$PACKAGE_DIR/.git"
if [ ! -d "$PACKAGE_GIT_DIR" ]; then
    echo "❌ Package directory is not a git repository"
    exit 1
fi

# Copy hook to package git hooks directory
HOOK_SOURCE="git-hooks/post-commit"
HOOK_DEST="$PACKAGE_DIR/.git/hooks/post-commit"

if [ ! -f "$HOOK_SOURCE" ]; then
    echo "❌ Hook source file not found: $HOOK_SOURCE"
    exit 1
fi

echo "📂 Copying hook to: $HOOK_DEST"
cp "$HOOK_SOURCE" "$HOOK_DEST"

# Make hook executable
chmod +x "$HOOK_DEST"

echo "✅ Git hook installed successfully!"
echo ""
echo "Now, whenever you commit changes to the package, the documentation"
echo "website will automatically update its package installation."
echo ""
echo "To test the hook:"
echo "  1. cd $PACKAGE_DIR"
echo "  2. Make a small change and commit it"
echo "  3. The hook should automatically update this website's package"
