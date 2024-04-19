from rest_framework import generics
from .models import User
from .serializers import RegisterSerializer
from .permission import IsAdminOrReadOnly


# Create your views here.
class UserList(generics.ListCreateAPIView):
    permission_classes=[IsAdminOrReadOnly]
    queryset = User.objects.all()
    serializer_class = User
    
    

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class=
    permission_classes=[IsAdminOrReadOnly]
