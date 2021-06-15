from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.

class User_list(APIView):
    def get(self, request, *args, **kwargs):
        data = {
            'data' : 'adeeb',
            'age' : 32,
        }

        return Response(data)
