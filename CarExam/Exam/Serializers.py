from rest_framework import serializers
from .models import *

class QuestionSerializers (serializers.ModelSerializer):
    # 生成考卷信息



    class Meta:
        models = Question
        fields = '__all__'


class StudentSerializers (serializers.ModelSerializer):
    # 生成考卷信息


    class Meta:
        models = Student
        fields = '__all__'

class HistoryExamSerializers(serializers.ModelSerializer):

    class Meta:
        models = Examine
        fields = (
            'em_in',
            'student',
            'score',
            'em_date',
            'status'
        )


