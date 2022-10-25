from rest_framework import serializers

from .models import Question, Comment, PhoneRequest, Application, Picture


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ('name', 'phone_number', 'email', 'group_age')


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('name', 'phone_number', 'email')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('name', 'comment')


class PhoneRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneRequest
        fields = ('name', 'phone_number')


class PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Picture
        fields = ('image', 'text', 'title', 'id')
