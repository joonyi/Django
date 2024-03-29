from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ResumeSerializer 
from .models import Resume

class ResumeAuthentication(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request':request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response(token.key)

class ResumeList(APIView):
    def get(self, request):
        model = Resume.objects.all()
        serializer = ResumeSerializer(model, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ResumeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)    
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ResumeDetail(APIView):
    def get_user(self, resume_id):
        try:
            model = Resume.objects.get(id=resume_id)
            return model
        except Resume.DoesNotExist:
            return 
        
    def get(self, request, resume_id):
        if not self.get_user(resume_id):
            return Response(f"Resume id {resume_id} is Not Found", status=status.HTTP_404_NOT_FOUND)
        serializer = ResumeSerializer(self.get_user(resume_id))
        return Response(serializer.data)

    def put(self, request, resume_id):
        if not self.get_user(resume_id):
            return Response(f"Resume id {resume_id} is Not Found", status=status.HTTP_404_NOT_FOUND)
        serializer = ResumeSerializer(self.get_user(resume_id), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)    
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, resume_id):
        if not self.get_user(resume_id):
            return Response(f"Resume with id:{resume_id} is Not Found", status=status.HTTP_404_NOT_FOUND)
        model = self.get_user(resume_id)
        model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)