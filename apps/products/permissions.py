from rest_framework.permissions import BasePermission



class IsOwnerCompany(BasePermission):
    message = 'It is not your Company'

    def has_object_permission(self, request, view, obj):
        if obj.company.owner == request.user:
            return True
        return False


class IsOwnCategory(BasePermission):
    message = 'It is not your Category'

    def has_object_permission(self, request, view, obj):
        if obj.category.company == obj.company:
            return True
        return False