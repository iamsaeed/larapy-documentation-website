#!/bin/bash

# Update Larapy Package Script
# Usage: ./update_package.sh

echo "🔄 Updating Larapy package..."

# Navigate to documentation website directory
cd "$(dirname "$0")"

# Uninstall current package
echo "📦 Uninstalling current larapy package..."
pip uninstall larapy -y

# Reinstall from local package
echo "📦 Installing updated larapy package..."
pip install -e ../package-larapy

# Verify installation
echo "✅ Verifying installation..."
python -c "import larapy; print(f'Larapy version: {larapy.__version__ if hasattr(larapy, \"__version__\") else \"development\"}')"

echo "🎉 Package updated successfully!"

# Optional: Run tests to verify everything works
echo "🧪 Running quick verification..."
python -c "
try:
    from larapy.core.application import Application
    from larapy.database.connection import DB
    print('✅ Core modules imported successfully')
except ImportError as e:
    print(f'❌ Import error: {e}')
"

echo "Done! 🚀"
