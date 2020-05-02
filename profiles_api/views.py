from rest_framework.views import APIView
from rest_framework.response import Response


class HelloAPIView(APIView):

    def get(self, request, format=None):
        what = [
            "hello",
            "world",
            "!!"
        ]

        return Response({'message': "It works!", 'what': what})
