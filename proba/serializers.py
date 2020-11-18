from rest_framework import serializers
from proba.models import Prob

class ProbaListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prob
        fields = ('id', 'number', 'user')



class ProbDetailSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Prob
        fields = '__all__'