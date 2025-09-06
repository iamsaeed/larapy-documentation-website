"""
CreatePostsTable migration.
"""

from larapy.database.migrations.migration import Migration
from larapy.database.migrations.schema import Schema, Blueprint


class CreatePostsTable(Migration):
    """
    Run the migrations.
    
    @return void
    """
    
    def up(self):
        """
        Run the migrations.
        
        @return void
        """
        def create_posts_table(table: Blueprint):
            table.id()
            table.timestamps()
        
        Schema.create('posts', create_posts_table)

    def down(self):
        """
        Reverse the migrations.
        
        @return void
        """
        Schema.drop_if_exists('create_posts_table')
