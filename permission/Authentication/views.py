from rest_framework import generics
from .models import User
from .serializers import UserSerializer
<<<<<<< HEAD
from .permission import IsAdminOrReadOnly,IsUserOrReadOnly

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save()

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminOrReadOnly,IsUserOrReadOnly]

    def perform_update(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.delete()
=======
from .permission import IsAdmin,IsUser


# Create your views here.
class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes=[IsAdmin,IsUser]
    

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class=UserSerializer
    permission_classes=[IsAdmin,IsUser]
>>>>>>> d4b30990d1f4c30bb086f2dc6b0cd641d04a4b40
