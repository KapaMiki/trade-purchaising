from rest_framework.permissions import BasePermission



class IsOwnerCompany(BasePermission):
    message = 'It is not your Company'

    def has_object_permission(self, request, view, obj):
        if obj.owner == request.user:
            return True
        return False