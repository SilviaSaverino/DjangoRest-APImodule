from rest_framework import serializers
from .models import Profile
from followers.models import Follower
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
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    following_id = serializers.SerializerMethodField()
    posts_count = serializers.ReadOnlyField()
    followers_count = serializers.ReadOnlyField()
    following_count = serializers.ReadOnlyField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_following_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            following = Follower.objects.filter(
                owner=user, followed=obj.owner
            ).first()
            # print(following)
            return following.id if following else None
        return None

    class Meta:
        model = Profile
        fields = [
            'id', 'owner', 'created_at', 'updated_at', 'name',
            'content', 'image', 'is_owner', 'following_id',
            'posts_count', 'followers_count', 'following_count',
        ]