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
        models = Question
        fields = '__all__'


