from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RegisterSerialiser, LoginSerializer


class RegisterView(APIView):
    serializer_class = RegisterSerialiser

    def post(self, request):
        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)
            return Response(serializer.errors, status=400)
        except Exception as e:
            return Response({'error': str(e)}, status=500)


class LoginView(APIView):
    serializer_class = LoginSerializer

    def post(self, request):
        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                return Response(
                    serializer.get_jwt_token(
                        serializer.validated_data),
                    status=200)
            return Response(serializer.errors, status=400)
        except Exception as e:
            return Response({'error': str(e)}, status=500)


# Create your views here.
