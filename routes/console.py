"""
Console Routes
Similar to Laravel's routes/console.php
"""

from larapy.console.command import Larapy

def register_commands(kernel):
    """
    Register Closure based console commands.
    """
    
    # Simple closure-based command
    @Larapy.command('inspire')
    def inspire():
        """Display an inspiring quote."""
        quotes = [
            "The way to get started is to quit talking and begin doing. -Walt Disney",
            "The pessimist sees difficulty in every opportunity. The optimist sees opportunity in every difficulty. -Winston Churchill",
            "Don't let yesterday take up too much of today. -Will Rogers",
            "You learn more from failure than from success. Don't let it stop you. Failure builds character. -Unknown",
            "It's not whether you get knocked down, it's whether you get up. -Vince Lombardi",
        ]
        
        import random
        quote = random.choice(quotes)
        
        print("\n" + "="*60)
        print(quote)
        print("="*60 + "\n")
    
    # Another example command with arguments
    @Larapy.command('greet {name} {--lang=en}')
    def greet(name, lang='en'):
        """Greet someone in different languages."""
        greetings = {
            'en': f'Hello, {name}!',
            'es': f'¡Hola, {name}!', 
            'fr': f'Bonjour, {name}!',
            'de': f'Hallo, {name}!',
            'it': f'Ciao, {name}!',
        }
        
        greeting = greetings.get(lang, greetings['en'])
        print(f"\n🌍 {greeting}\n")