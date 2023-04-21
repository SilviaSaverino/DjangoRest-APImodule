from rest_framework import serializers
from .models import Profile

#BELOW:
# We’ll create a ProfileSerializer class and inherit  
# from ModelSerializer. We’ll specify ‘owner’ as a  
# ReadOnlyField so that it can’t be edited. 
# We’ll  also populate it with the owner's username.
# In the Meta class, we’ll point to our Profile  model 
# and specify the fields we’d like to  
# include in the response. 
# be explicit about which  fields you are including, 
# because you might want  
# to add another field to the Profile model later  on, 
# that you don’t want to be included in the serializer.

class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner_username')
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Profile
        fields = [
            'id', 'owner', 'created_at', 'updated_at', 'name',
            'content', 'image', 'is_owner'
        ]