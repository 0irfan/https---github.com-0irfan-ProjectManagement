from rest_framework import serializers
from .models import ProjectInformation,projectAuthority, Deliverable,project_detail,Resource

class ProjectInformationSerializer(serializers.ModelSerializer):
    class meta:
        model=ProjectInformation
        fields='__all__'
    def validate(self,value):
        start_date=value['start_date']
        end_date=value['End_date']
        if start_date>end_date:
            raise serializers.ValidationError("start date should be less than end date")
        
        return value

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


class projectAuthoritySerializer(serializers.ModelSerializer):
    class Meta:
        model=projectAuthority
        fields='__all__'
    #Field Level Custom Validation On Serializer 
    def validate_phone_number(self,value):
        if value>=15:
            raise serializers.ValidationError("Phone Number can't be greater than 15")
        return value