from rest_framework import serializers 
from polls.models import Student,Doubt
 
 
class StudentSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Student
       
        fields = ('id',
                  'name',
                  'roll_no',
                  'standard')


class DoubtSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Doubt
       
        fields = '__all__'