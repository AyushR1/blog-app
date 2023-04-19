from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import BlogSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Blog


class PostView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
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

    def get(self,request):
        try:
            blogs=Blog.objects.all()
            serializer=self.serializer_class(blogs,many=True)
            return Response(serializer.data,status=200)
        except Exception as e:
            return Response({'error': str(e)}, status = 500) 
    

class PostSpecificView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]
    serializer_class = BlogSerializer

    def get(self,request, pk):
        try:
            print(pk)
            blogs=Blog.objects.filter(uid = pk)
            serializer=self.serializer_class(blogs,many=True)
            return Response(serializer.data,status=200)
        except Exception as e:
            return Response({'error': str(e)}, status = 500) 
    
    def patch(self, request, pk):
        try:
            data=request.data
            blog=Blog.objects.filter(uid = pk)
            
            if not blog.exists():
                return Response({'error': 'Blog does not exist'}, status = 400)

            if request.user.id != blog[0].user.id:
                return Response({'error': 'You are not authorized to update this blog'}, status = 400)
            
            serializer = self.serializer_class(blog[0],data = data,partial=True)
            
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status = 201)
            return Response(serializer.errors, status = 400)
        except Exception as e:
            return Response({'errore': str(e)}, status = 500)



    # Create your views here.


