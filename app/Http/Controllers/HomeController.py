"""
Home Controller
Handles the home page requests
"""

from .Controller import Controller
from larapy.http.response import Response
from larapy.view import View

class HomeController(Controller):
    """
    Handle home page requests
    """
    
    async def index(self, request):
        """
        Show the application home page.
        
        Args:
            request: The HTTP request instance
            
        Returns:
            Response: The rendered home page
        """
        # You can pass data to the view
        data = {
            'title': 'Welcome to Larapy',
            'message': 'Laravel\'s elegant syntax meets Python\'s simplicity',
            'version': '0.2.0',
            'features': [
                'Larapy ORM',
                'Authentication System',
                'Middleware Support',
                'Caching System',
                'Queue System',
                'Event System'
            ]
        }
        
        return View.render('home', data)