"""
Base Controller
Similar to Laravel's app/Http/Controllers/Controller.php
"""

from larapy.http.controller import Controller as BaseController
from larapy.auth.access import AuthorizesRequests
from larapy.http.validation import ValidatesRequests
from larapy.routing.controller import DispatchesJobs

class Controller(BaseController, AuthorizesRequests, ValidatesRequests, DispatchesJobs):
    """
    Base controller class for all application controllers
    """
    pass