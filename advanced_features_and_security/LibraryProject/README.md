# README.md - Documentation
"""
# Django Permissions and Groups Setup

## Custom Permissions
- `can_view`: Allows users to view articles.
- `can_create`: Allows users to create new articles.
- `can_edit`: Allows users to edit existing articles.
- `can_delete`: Allows users to delete articles.

## Groups and Their Permissions
- **Viewers**: Can only view articles.
- **Editors**: Can view, create, and edit articles.
- **Admins**: Have all permissions.

## Usage
1. Run migrations: `python manage.py makemigrations && python manage.py migrate`
2. Assign users to groups via Django Admin.
3. Test permissions by logging in as different users.
"""