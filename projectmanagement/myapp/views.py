from rest_framework import generics
from .models import projectAuthority,ProjectInformation,Deliverable,project_detail,Resource
from .serializer import ProjectInformationSerializer,DeliverableSerializer,ProjectAuthoritySerializer,ProjectDetailSerializers,ResourceSerializer

class ProjectInformationListCreateAPIView(generics.ListCreateAPIView):
    queryset = ProjectInformation.objects.all()
    serializer_class = ProjectInformationSerializer


class projectInformationRetrieveUpdateDestroyApiview(generics.RetrieveUpdateDestroyAPIView):
    queryset=ProjectInformation.objects.all()
    serializer_class=ProjectInformationSerializer

class ProjectDetailListCreateAPIView(generics.ListCreateAPIView):
    queryset=project_detail.objects.all()
    serializer_class=ProjectDetailSerializers


class ProjectDetailRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset=project_detail.objects.all()
    serializer_class=ProjectDetailSerializers

class ResourceListCreateAPIView(generics.ListCreateAPIView):
    queryset=Resource.objects.all()
    serializer_class=ResourceSerializer

class ResourceRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Resource.objects.all()
    serializer_class=ResourceSerializer


class DeliverableListCreateAPIView(generics.ListCreateAPIView):
    queryset=Deliverable.objects.all()
    serializer_class=DeliverableSerializer


class DeliverableRetreiveUpdateDestroyApiview(generics.RetrieveUpdateDestroyAPIView):
    queryset=Deliverable.objects.all()
    serializer_class=DeliverableSerializer


class ProjectAuthorityListCreateAPIView(generics.ListCreateAPIView):
    queryset = projectAuthority.objects.all()
    serializer_class = ProjectAuthoritySerializer
class projectAuthorityRetrieveUpdateDestroyApiview(generics.RetrieveUpdateDestroyAPIView):
    queryset=projectAuthority.objects.all()
    serializer_class=ProjectAuthoritySerializer
