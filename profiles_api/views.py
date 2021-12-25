from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """API View Test """

    def get(self,request,format=None):
        """Retuns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives most control over the application logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

#from django.shortcuts import render
