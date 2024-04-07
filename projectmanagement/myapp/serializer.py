from rest_framework import serializers
from .models import ProjectInformation,projectAuthority, Deliverable,project_detail,Resource

class ProjectInformationSerializer(serializers.ModelSerializer):
    class meta:
        model=ProjectInformation
        fields='__all__'

class ProjectDetailSerializers(serializers.ModelSerializer):
    class meta:
        model = project_detail
        fields='__all__'

        
class ResourceSerializer(serializers.ModelSerializer):
    class meta:
        model=Resource
        fields='__all__'



class DeliverableSerializer(serializers.ModelSerializer):
    class meta:
        model=Deliverable
        fields='__all__'

class ProjectAuthoritySerializer(serializers.ModelSerializer):
    class meta:
        model=projectAuthority
        fields='__all__'