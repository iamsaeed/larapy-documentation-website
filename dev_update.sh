#!/bin/bash

# Enhanced Larapy Package Update Script
# Usage: ./dev_update.sh [options]
# Options:
#   --force, -f    Force reinstall even if no changes detected
#   --test, -t     Run tests after update
#   --migrate, -m  Run migrations after update
#   --help, -h     Show this help message

set -e  # Exit on any error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Default options
FORCE_UPDATE=false
RUN_TESTS=false
RUN_MIGRATIONS=false

# Parse command line arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        -f|--force)
            FORCE_UPDATE=true
            shift
            ;;
        -t|--test)
            RUN_TESTS=true
            shift
            ;;
        -m|--migrate)
            RUN_MIGRATIONS=true
            shift
            ;;
        -h|--help)
            echo "Enhanced Larapy Package Update Script"
            echo ""
            echo "Usage: $0 [options]"
            echo ""
            echo "Options:"
            echo "  -f, --force     Force reinstall even if no changes detected"
            echo "  -t, --test      Run tests after update"
            echo "  -m, --migrate   Run migrations after update"
            echo "  -h, --help      Show this help message"
            echo ""
            echo "Examples:"
            echo "  $0                  # Basic update"
            echo "  $0 --force --test   # Force update and run tests"
            echo "  $0 -m               # Update and run migrations"
            exit 0
            ;;
        *)
            echo "Unknown option $1"
            echo "Use --help for usage information"
            exit 1
            ;;
    esac
done

echo -e "${BLUE}🔄 Larapy Package Development Update${NC}"
echo "========================================"

# Navigate to documentation website directory
cd "$(dirname "$0")"

# Check if package directory exists
if [ ! -d "../package-larapy" ]; then
    echo -e "${RED}❌ Package directory '../package-larapy' not found${NC}"
    exit 1
fi

# Check for changes in package (optional optimization)
if [ "$FORCE_UPDATE" = false ]; then
    echo -e "${YELLOW}📊 Checking for package changes...${NC}"
    
    # Get last modification time of package files
    PACKAGE_MODIFIED=$(find ../package-larapy -name "*.py" -type f -exec stat -c %Y {} \; | sort -n | tail -1)
    
    # Check if we have a timestamp file
    TIMESTAMP_FILE=".last_package_update"
    if [ -f "$TIMESTAMP_FILE" ]; then
        LAST_UPDATE=$(cat "$TIMESTAMP_FILE")
        
        if [ "$PACKAGE_MODIFIED" -le "$LAST_UPDATE" ]; then
            echo -e "${GREEN}✅ No changes detected in package since last update${NC}"
            echo "Use --force to update anyway"
            exit 0
        fi
    fi
fi

echo -e "${YELLOW}📦 Updating package installation...${NC}"

# Create virtual environment backup info
echo -e "${BLUE}💾 Backing up environment info...${NC}"
pip freeze > .backup_requirements.txt

# Uninstall current package
echo -e "${YELLOW}🗑️  Uninstalling current larapy package...${NC}"
pip uninstall larapy -y 2>/dev/null || echo "Package not installed or already removed"

# Install package in editable mode
echo -e "${YELLOW}📦 Installing updated larapy package...${NC}"
pip install -e ../package-larapy

# Update timestamp
echo $(date +%s) > .last_package_update

# Verify installation
echo -e "${YELLOW}✅ Verifying installation...${NC}"
python -c "
import sys
try:
    import larapy
    from larapy.core.application import Application
    from larapy.database.connection import DB
    print('✅ Core modules imported successfully')
    
    # Check version if available
    if hasattr(larapy, '__version__'):
        print(f'📋 Larapy version: {larapy.__version__}')
    else:
        print('📋 Larapy version: development')
        
except ImportError as e:
    print(f'❌ Import error: {e}')
    sys.exit(1)
"

if [ $? -ne 0 ]; then
    echo -e "${RED}❌ Package installation verification failed${NC}"
    echo -e "${YELLOW}🔄 Attempting to restore from backup...${NC}"
    pip install -r .backup_requirements.txt
    exit 1
fi

# Run migrations if requested
if [ "$RUN_MIGRATIONS" = true ]; then
    echo -e "${YELLOW}🗄️  Running migrations...${NC}"
    if command -v larapy &> /dev/null; then
        larapy migrate
    else
        echo -e "${YELLOW}⚠️  larapy command not found, skipping migrations${NC}"
    fi
fi

# Run tests if requested
if [ "$RUN_TESTS" = true ]; then
    echo -e "${YELLOW}🧪 Running tests...${NC}"
    if [ -d "tests" ]; then
        python -m pytest tests/ -v
    else
        echo -e "${YELLOW}⚠️  No tests directory found${NC}"
    fi
fi

# Clean up backup
rm -f .backup_requirements.txt

echo ""
echo -e "${GREEN}🎉 Package updated successfully!${NC}"
echo -e "${BLUE}📝 Next steps:${NC}"
echo "   • Test your application: python public/index.py"
echo "   • Run migrations: larapy migrate"
echo "   • Run tests: larapy test"
echo ""
