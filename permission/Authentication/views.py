from rest_framework import generics
from .models import User
from .serializers import UserSerializer
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
