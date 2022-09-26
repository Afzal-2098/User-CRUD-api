from rest_framework.views import APIView
from .serializer import UserSeriarizer
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

# Crud operations class
class UserApi(APIView):
    # function for get user data
    def get(self, request, pk=None, format=None):
        '''handles all the get requests contains or do not contains user's id'''
        if pk is not None:
            user = User.objects.get(pk=pk)
            serializer = UserSeriarizer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)

        user = User.objects.all()
        serializer = UserSeriarizer(user, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    # function for update complete user's data
    def put(self, request, pk, format=None):
        '''updates all the field data of existing user'''
        id = pk
        user = User.objects.get(pk=id)
        serializer = UserSeriarizer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete Data Updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    # function for update user's data partially
    def patch(self, request, pk, format=None):
        '''updates user's field data partially(not all fields will update)'''
        id = pk
        user = User.objects.get(pk=id)
        serializer = UserSeriarizer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Partial Data Updated'})
        return Response(serializer.errors)


    # function for inserting new user data into database
    def post(self, request, format=None):
        '''creates new user's data and save it into the database'''
        serializer = UserSeriarizer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'New Data Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    # function for deleting perticular data from the database
    def delete(self, request, pk=None, format=None):
        '''deletes those user's data whose id is passed through the url to the server'''
        if pk is not None:
            id = pk
            user = User.objects.get(pk=id)
            user.delete()
            return Response({'msg':'Data Deleted'}, status=status.HTTP_204_NO_CONTENT)
        return Response({'msg':'ID is Not Provided. Please Provide the id of the product which you wanted to delete.'}, status=status.HTTP_400_BAD_REQUEST)