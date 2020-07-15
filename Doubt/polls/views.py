from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view
from polls.models import Student, Doubt
from polls.serializers import StudentSerializer,DoubtSerializer
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status

@api_view(['GET', 'POST'])
def StudentAPI(request):
    if request.method == 'GET':
        student = Student.objects.all()
        

        student_serializer = StudentSerializer(student, many=True)
        return JsonResponse(student_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
       

@api_view(['GET', 'POST'])
def DoubtAPI(request):
    if request.method == 'GET':
        doubt = Doubt.objects.all()
        

        doubt_serializer = DoubtSerializer(doubt, many=True)
        return JsonResponse(doubt_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == 'POST':
        serializer = DoubtSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)