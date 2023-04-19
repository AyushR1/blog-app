from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import BlogSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

class PostView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    serializer_class = BlogSerializer

    def post(self, request):
        try:
            data=request.data
            data['user']=request.user.id
            serializer = self.serializer_class(data = data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status = 201)
            return Response(serializer.errors, status = 400)
        except Exception as e:
            return Response({'error': str(e)}, status = 500)

    # Create your views here.
