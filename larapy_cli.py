#!/usr/bin/env python3
"""
Larapy CLI Entry Point for Global Command
This file provides the global 'larapy' command interface
"""

import sys
import os
from pathlib import Path

# Add project root to Python path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

def main():
    """Main entry point for global larapy command"""
    # Import the main CLI application
    from larapy_main import main as larapy_main
    larapy_main()

if __name__ == '__main__':
    main()