"""
User model for database operations.
"""

from larapy.orm.model import Model  # Import the base Model class from Larapy ORM


class User(Model):
    """
    User model for database interactions.
    
    This model represents the user entity in the database.
    Inherits from the base Larapy ORM Model class.
    """
    
    # Specify the table name (optional - defaults to snake_case plural of class name)
    # table = 'users'
    
    # Mass assignment protection - specify which fields can be mass assigned
    fillable = [
        'name',
        'email',
        'password',
    ]
    
    # Alternative: specify guarded fields (fields that cannot be mass assigned)
    # guarded = ['id', 'created_at', 'updated_at']
    
    # Specify casts for automatic type conversion
    casts = {
        'created_at': 'datetime',
        'updated_at': 'datetime',
    }
    
    # Specify which fields should be hidden when serializing
    hidden = [
        'password',
        'remember_token',
    ]
    
    # Define relationships
    def example_relationship(self):
        """
        Example relationship method.
        Uncomment and modify as needed.
        """
        # return self.belongs_to('OtherModel')
        # return self.has_many('RelatedModel')
        # return self.has_one('RelatedModel')
        pass
    
    # Define scopes for reusable query constraints
    @classmethod
    def active(cls):
        """
        Scope to get only active records.
        Example scope method.
        """
        # return cls.where('is_active', True)
        return cls.query()
    
    # Define accessors and mutators
    def get_full_name_attribute(self):
        """
        Example accessor for computed attribute.
        This would create a 'full_name' attribute.
        """
        # return f"{self.first_name} {self.last_name}"
        pass
    
    def set_name_attribute(self, value):
        """
        Example mutator for input transformation.
        This would automatically capitalize the name when set.
        """
        return value.title() if value else None
