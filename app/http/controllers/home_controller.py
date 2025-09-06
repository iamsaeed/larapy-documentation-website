"""
Home Controller
Handles the home page requests
"""

from .controller import Controller
from larapy.view import View
from larapy.http.request import Request
from larapy.http.response import Response

class HomeController(Controller):
    """
    Handle home page requests
    """
    
    async def index(self, request: Request) -> Response:
        """
        Show the application home page.
        
        Args:
            request: The HTTP request instance
            
        Returns:
            Response: The rendered home page
        """
        # You can pass data to the view
        data = {
            'title': 'Welcome to Larapy Documentation Website',
            'message': 'Laravel\'s elegant syntax meets Python\'s simplicity',
            'version': '1.0.0',
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