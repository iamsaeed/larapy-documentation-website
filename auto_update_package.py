#!/usr/bin/env python3
"""
Larapy Package Auto-Updater
Watches for changes in the package directory and automatically reinstalls
"""

import os
import sys
import time
import subprocess
import argparse
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class LarapyPackageHandler(FileSystemEventHandler):
    """Handler for package file changes"""
    
    def __init__(self, debounce_seconds=2):
        self.debounce_seconds = debounce_seconds
        self.last_modified = 0
        self.website_dir = Path(__file__).parent
        self.package_dir = self.website_dir.parent / "package-larapy"
        
    def on_modified(self, event):
        """Handle file modification events"""
        if event.is_directory:
            return
            
        # Only react to Python files
        if not event.src_path.endswith('.py'):
            return
            
        # Debounce rapid changes
        current_time = time.time()
        if current_time - self.last_modified < self.debounce_seconds:
            return
            
        self.last_modified = current_time
        
        print(f"📝 Change detected: {event.src_path}")
        self.update_package()
    
    def update_package(self):
        """Update the package installation"""
        print("🔄 Updating package...")
        
        try:
            # Change to website directory
            os.chdir(self.website_dir)
            
            # Uninstall and reinstall package
            subprocess.run([sys.executable, "-m", "pip", "uninstall", "larapy", "-y"], 
                         capture_output=True, check=False)
            
            result = subprocess.run([sys.executable, "-m", "pip", "install", "-e", str(self.package_dir)], 
                                  capture_output=True, text=True)
            
            if result.returncode == 0:
                print("✅ Package updated successfully!")
                
                # Test import
                test_result = subprocess.run([sys.executable, "-c", "import larapy; print('Import test passed')"], 
                                           capture_output=True, text=True)
                
                if test_result.returncode == 0:
                    print("✅ Import test passed")
                else:
                    print(f"❌ Import test failed: {test_result.stderr}")
            else:
                print(f"❌ Package update failed: {result.stderr}")
                
        except Exception as e:
            print(f"❌ Error updating package: {e}")

def main():
    """Main function"""
    parser = argparse.ArgumentParser(description="Watch Larapy package for changes and auto-update")
    parser.add_argument("--debounce", type=int, default=2, 
                       help="Debounce time in seconds (default: 2)")
    parser.add_argument("--initial-update", action="store_true",
                       help="Perform initial package update before watching")
    
    args = parser.parse_args()
    
    # Setup paths
    script_dir = Path(__file__).parent
    package_dir = script_dir.parent / "package-larapy"
    
    if not package_dir.exists():
        print(f"❌ Package directory not found: {package_dir}")
        sys.exit(1)
    
    print("🔍 Larapy Package Auto-Updater")
    print(f"📁 Watching: {package_dir}")
    print(f"🏠 Website: {script_dir}")
    print(f"⏱️  Debounce: {args.debounce}s")
    print("-" * 50)
    
    # Create event handler
    event_handler = LarapyPackageHandler(debounce_seconds=args.debounce)
    
    # Perform initial update if requested
    if args.initial_update:
        print("🚀 Performing initial package update...")
        event_handler.update_package()
    
    # Setup file watcher
    observer = Observer()
    observer.schedule(event_handler, str(package_dir), recursive=True)
    
    # Start watching
    observer.start()
    print("👀 Watching for changes... (Press Ctrl+C to stop)")
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n🛑 Stopping watcher...")
        observer.stop()
    
    observer.join()
    print("✅ Watcher stopped")

if __name__ == "__main__":
    main()
