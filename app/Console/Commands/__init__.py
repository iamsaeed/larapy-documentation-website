# Commands module
"""
Console commands directory.
Similar to Laravel's app/Console/Commands directory.
"""

from .TestCommand import TestCommand

# Export commands for easy importing
__all__ = ['TestCommand']