"""
User Model
Similar to Laravel's app/Models/User.php
"""

from larapy.orm.model import Model
from larapy.auth.authenticatable import Authenticatable
from larapy.auth.notifications import CanResetPassword
from larapy.database.factory import HasFactory

class User(Model, Authenticatable, CanResetPassword, HasFactory):
    """
    User model for authentication and user management
    """
    
    # Database table name (optional - will default to 'users')
    table = 'users'
    
    # Primary key
    primary_key = 'id'
    
    # Indicates if the model should be timestamped
    timestamps = True
    
    # Mass assignable attributes
    fillable = [
        'name',
        'email',
        'password',
    ]
    
    # Hidden attributes for serialization
    hidden = [
        'password',
        'remember_token',
    ]
    
    # Attribute casting
    casts = {
        'email_verified_at': 'datetime',
        'password': 'hashed',
        'created_at': 'datetime',
        'updated_at': 'datetime',
    }
    
    # Validation rules
    rules = {
        'name': 'required|string|max:255',
        'email': 'required|string|email|max:255|unique:users',
        'password': 'required|string|min:8|confirmed',
    }
    
    def get_auth_identifier_name(self):
        """Get the name of the unique identifier for the user."""
        return 'id'
    
    def get_auth_identifier(self):
        """Get the unique identifier for the user."""
        return self.getattr(self.get_auth_identifier_name())
    
    def get_auth_password(self):
        """Get the password for the user."""
        return self.password
    
    def get_remember_token(self):
        """Get the token value for the "remember me" session."""
        return self.remember_token if hasattr(self, 'remember_token') else None
    
    def set_remember_token(self, value):
        """Set the token value for the "remember me" session."""
        self.remember_token = value
    
    def get_remember_token_name(self):
        """Get the column name for the "remember me" token."""
        return 'remember_token'
    
    def get_email_for_password_reset(self):
        """Get the e-mail address where password reset links are sent."""
        return self.email
    
    @staticmethod
    def find_for_passport(identifier):
        """Find user instance for Passport authentication."""
        return User.where('email', identifier).first()
    
    # Accessors & Mutators
    def get_name_attribute(self, value):
        """Get the user's name (accessor)."""
        return value.title() if value else None
    
    def set_password_attribute(self, value):
        """Hash the user's password (mutator)."""
        from larapy.support.facades.Hash import Hash
        self.attributes['password'] = Hash.make(value)
    
    # Relationships (examples for future use)
    def posts(self):
        """Get all posts for the user."""
        from app.Models.Post import Post
        return self.has_many(Post)
    
    def profile(self):
        """Get the user's profile."""
        from app.Models.Profile import Profile
        return self.has_one(Profile)
    
    def roles(self):
        """Get the user's roles."""
        from app.Models.Role import Role
        return self.belongs_to_many(Role, 'user_roles')
    
    # Scopes
    def scope_verified(self, query):
        """Scope a query to only include verified users."""
        return query.where_not_null('email_verified_at')
    
    def scope_unverified(self, query):
        """Scope a query to only include unverified users."""
        return query.where_null('email_verified_at')
    
    def scope_active(self, query):
        """Scope a query to only include active users."""
        return query.where('status', 'active')
    
    # Helper methods
    def is_verified(self):
        """Check if the user's email is verified."""
        return self.email_verified_at is not None
    
    def mark_email_as_verified(self):
        """Mark the user's email as verified."""
        from datetime import datetime
        self.email_verified_at = datetime.now()
        self.save()
    
    def send_password_reset_notification(self, token):
        """Send the password reset notification."""
        # Implementation for sending password reset email
        pass
    
    def send_email_verification_notification(self):
        """Send the email verification notification."""
        # Implementation for sending email verification
        pass
    
    def __str__(self):
        """String representation of the user."""
        return f"User(id={self.id}, name='{self.name}', email='{self.email}')"
    
    def __repr__(self):
        """Developer representation of the user."""
        return f"<User id={self.id} email='{self.email}'>"