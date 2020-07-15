from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.renderers import JSONRenderer

from polls.models import Student, Doubt

@api_view(['GET', 'POST'])
def StudentAPI(request):
    if request.method == 'GET':
        student = Student.objects.all()
        
        name = request.query_params.get('name', None)
        if name is not None:
            student = student.filter(title__icontains=name)
        
        student_serializer = TutorialSerializer(students, many=True)
        return JsonResponse(student_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        tutorial_data = JSONParser().parse(request)
        tutorial_serializer = TutorialSerializer(data=tutorial_data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Tutorial.objects.all().delete()
        return JsonResponse({'message': '{} Tutorials were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 



from rest_framework import serializers

from polls.models  import *

class StudentSerializer(serializers.Serializer):
    class Meta:
        models = Student
        fields = '__all__'



class DoubtSerializer(serializers.Serializer):
    class Meta:
        model = Doubt
        fields = '__all__'




from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view
from polls.models import Student, Doubt
from polls.serializers import StudentSerializer
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
        student_data = JSONParser().parse(request)
        student_serializer = StudentSerializer(data=student_data)
        if student_serializer.is_valid():
            student_serializer.save()
            return JsonResponse(student_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(student_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
       
