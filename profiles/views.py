from rest_framework import generics
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Profile
from .serializers import ProfileSerializer


class ProfileList(generics.ListAPIView):
    """
    List all profiles.
    No create view as profile creation is handled by django signals.
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileDetail(generics.RetrieveUpdateAPIView):
    """
    Retrieve or update a profile if you're the owner.
    """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

#--------------------------------------REFACTORED CODE ABOVE VS ORIGINAL BELOW:
# from django.http import Http404
# from rest_framework import status
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from .models import Profile
# from .serializers import ProfileSerializer
# from drf_api.permissions import IsOwnerOrReadOnly


# class ProfileList(APIView):
#     """
#     A view that returns a list of all profiles.
#     """
#     def get(self, request):
#         """
#         Retrieve all profile instances and serialize them.
#         """
#         profiles = Profile.objects.all()
#         serializer = ProfileSerializer(profiles, many=True, context={'request': request})
#         return Response(serializer.data)


# class ProfileDetail(APIView):
#     """
#     A view that returns the details of a single profile.
#     """
#     serializer_class = ProfileSerializer
#     permission_classes = [IsOwnerOrReadOnly]

#     def get_object(self, pk):
#         """
#         Retrieve a single profile instance by primary key 
#         or return a 404 error.
#         """
#         try:
#             profile = Profile.objects.get(pk=pk)
#             self.check_object_permissions(self.request, profile)
#             return profile
#         except Profile.DoesNotExist:
#             raise Http404

#     def get(self, request, pk):
#         """
#         Retrieve and serialize a single profile instance by primary key.
#         """
#         profile = self.get_object(pk)
#         serializer = ProfileSerializer(profile, context={'request': request} )
#         return Response(serializer.data)

#     def put(self, request, pk):
#         """
#         Update a single profile instance by primary key.
#         """
#         profile = self.get_object(pk)
#         serializer = ProfileSerializer(profile, data=request.data,  context={'request': request})
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)