#!/usr/bin/env python3
"""
Larapy Console Command Interface
Similar to Laravel's artisan command but uses 'larapy' as the command name
"""

import sys
import os
from pathlib import Path

# Add project root to Python path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

from larapy.console.application import Application as ConsoleApplication
from bootstrap.app import create_application

def main():
    """Main larapy entry point"""
    # Create the web application
    app = create_application()
    
    # Create console application
    console = ConsoleApplication('Larapy Framework', '0.2.0')
    
    # Register built-in Larapy commands
    console.add_commands([
        'larapy.console.commands.ServeCommand',
        'larapy.console.commands.MakeControllerCommand',
        'larapy.console.commands.MakeModelCommand',
        'larapy.console.commands.MakeMiddlewareCommand',
        'larapy.console.commands.MakeMigrationCommand',
        'larapy.console.commands.MigrateCommand',
        'larapy.console.commands.MigrateRollbackCommand',
        'larapy.console.commands.MigrateResetCommand',
        'larapy.console.commands.MigrateRefreshCommand',
        'larapy.console.commands.MigrateStatusCommand',
        'larapy.console.commands.SeedCommand',
        'larapy.console.commands.MakeSeederCommand',
        'larapy.console.commands.MakeFactoryCommand',
        'larapy.console.commands.TinkerCommand',
        'larapy.console.commands.KeyGenerateCommand',
    ])
    
    # Register application commands
    from app.Console.Commands.TestCommand import TestCommand
    console.add(TestCommand())
    
    # Register additional custom commands here
    # from app.Console.Commands.CustomCommand import CustomCommand
    # console.add(CustomCommand())
    
    # Register console routes (closure-based commands)
    from routes import console as console_routes
    console_routes.register_commands(console)
    
    # Run the console
    console.run()

if __name__ == '__main__':
    main()