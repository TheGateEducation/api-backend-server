from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class WelcomeView(APIView):
    def get(self, request):
        content = {
            'message': 'Welcome to the API',
            'status_code': status.HTTP_200_OK,
        }
        return Response(content, status=status.HTTP_200_OK)