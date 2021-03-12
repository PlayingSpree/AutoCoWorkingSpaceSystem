from rest_framework import serializers

from feedback.models import Feedback, ProblemType, Problem


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ['id', 'user', 'rating', 'text', 'date_created']
        read_only_fields = ['id', 'date_created']


class ProblemTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProblemType
        fields = ['id', 'name', 'detail']
        read_only_fields = ['id']


class ProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Problem
        fields = ['id', 'user', 'type', 'severity', 'date_created', 'date_created']
        read_only_fields = ['id', 'date_created', 'date_created']
