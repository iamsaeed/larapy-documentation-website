# Models module
"""
Application models directory.
Similar to Laravel's app/Models directory.
"""

from .User import User

# Export models for easy importing
__all__ = ['User']