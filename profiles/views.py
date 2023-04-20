from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Profile
from .serializers import ProfileSerializer


class ProfileList(APIView):
    """
    A view that returns a list of all profiles.
    """
    def get(self, request):
        """
        Retrieve all profile instances and serialize them.
        """
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data)


class ProfileDetail(APIView):
    """
    A view that returns the details of a single profile.
    """
    def get_object(self, pk):
        """
        Retrieve a single profile instance by primary key 
        or return a 404 error.
        """
        try:
            profile = Profile.objects.get(pk=pk)
            return profile
        except Profile.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        """
        Retrieve and serialize a single profile instance by primary key.
        """
        profile = self.get_object(pk)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)