<<<<<<< HEAD
from rest_framework import permissions


from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
   

    def has_permission(self, request, view):
        
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user.is_authenticated and request.user.is_staff

class IsUserOrReadOnly(permissions.BasePermission):


    def has_object_permission(self, request, view, obj):
        
        if request.method in permissions.SAFE_METHODS:
            return True

       
        return obj == request.user

            
        
        




    

=======
from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.method=='GET'
    
class IsUser(BasePermission):
    def has_object_permission(self, request, view, obj):
            return request.method in ['POST','PUT','PATCH','DELETE']
>>>>>>> d4b30990d1f4c30bb086f2dc6b0cd641d04a4b40
    


        
