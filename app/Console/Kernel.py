"""
Console Kernel
Similar to Laravel's app/Console/Kernel.php
"""

from larapy.console.kernel import Kernel as ConsoleKernel

class Kernel(ConsoleKernel):
    """
    The Larapy commands provided by your application.
    """
    
    # The Larapy commands provided by your application
    commands = [
        'app.Console.Commands.TestCommand.TestCommand',
    ]
    
    def schedule(self, schedule):
        """
        Define the application's command schedule.
        
        Args:
            schedule: The schedule instance
        """
        # Example scheduled commands:
        # schedule.command('inspire').hourly()
        # schedule.command('test:command').daily_at('02:00')
        pass
    
    def commands(self):
        """
        Register the commands for the application.
        """
        # Load commands from the Commands directory
        self.load(__file__ + '/Commands')
        
        # Load routes/console.py commands
        try:
            from routes import console
            console.register_commands(self)
        except ImportError:
            pass