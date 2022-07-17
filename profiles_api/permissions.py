from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allows user to edit their own profile"""
    
    def has_object_permission(self, request, view, obj):
        """Check if user trying to edit their own profile"""

        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.id == request.user.id