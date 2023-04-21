from rest_framework import permissions

class IsOwnerOrReadOnly(permission.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """
    def has_object_permission(self,request,view,obj):
        """
        Check if the user has permission to access the object.

        """
        if request.method in permission.SAFE-METHOD:
            return True
        return obj.owner == request.user