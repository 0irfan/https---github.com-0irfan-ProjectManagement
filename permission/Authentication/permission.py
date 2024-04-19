from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.method=='GET'
    
class IsUser(BasePermission):
    def has_object_permission(self, request, view, obj):
            return request.method in ['POST','PUT','PATCH','DELETE']
    


        
