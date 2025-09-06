"""
Test Command
A simple test command that prints a message to the console
"""

from larapy.console.command import Command

class TestCommand(Command):
    """
    Simple test command for demonstration
    """
    
    # The name and signature of the console command
    signature = 'test:command {name?} {--greeting=Hello}'
    
    # The console command description
    description = 'A simple test command that prints a message'
    
    def handle(self):
        """
        Execute the console command.
        """
        # Get the name argument (optional)
        name = self.argument('name') or 'World'
        
        # Get the greeting option
        greeting = self.option('greeting')
        
        # Print the main test message
        self.info('Hello! This is a test larapy command.')
        self.line('')
        
        # Print personalized greeting
        self.line(f'{greeting}, {name}!')
        self.line('')
        
        # Show some styled output examples
        self.comment('This command demonstrates:')
        self.line('• Console command creation')
        self.line('• Arguments and options handling')
        self.line('• Styled output methods')
        self.line('')
        
        # Show different output styles
        self.info('✅ Info message (green)')
        self.comment('💬 Comment message (yellow)')
        self.question('❓ Question message (cyan)')
        self.error('❌ Error message (red)')
        self.warn('⚠️  Warning message (yellow)')
        self.line('')
        
        # Show a table example
        headers = ['Feature', 'Status']
        rows = [
            ['Console Commands', '✅ Working'],
            ['Arguments', '✅ Working'],
            ['Options', '✅ Working'],
            ['Styled Output', '✅ Working'],
        ]
        
        self.table(headers, rows)
        self.line('')
        
        # Success message
        self.success('🎉 Test command completed successfully!')
        
        return 0  # Success exit code

# Command registration
command = TestCommand()