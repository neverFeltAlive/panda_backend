from django.core.mail import send_mail
from django.conf import settings

from rest_framework import serializers

from .models import Question, Comment, PhoneRequest, Application, Picture


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = '__all__'

    def create(self, validate_data):
        instance = super(ApplicationSerializer, self).create(validate_data)
        send_mail(
            subject='Уведомление: заявка на поступление',
            message=dict_to_str(validate_data),
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=['panda-kids33@yandex.ru'],
            fail_silently=False,
        )
        return instance


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

    def create(self, validate_data):
        instance = super(QuestionSerializer, self).create(validate_data)
        send_mail(
            subject='Уведомление: запись на экскурсию',
            message=dict_to_str(validate_data),
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=['panda-kids33@yandex.ru'],
            fail_silently=False,
        )
        return instance


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

    def create(self, validate_data):
        instance = super(CommentSerializer, self).create(validate_data)
        send_mail(
            subject='Уведомление: новый комментарий',
            message=dict_to_str(validate_data),
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=['panda-kids33@yandex.ru'],
            fail_silently=False,
        )
        return instance


class PhoneRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneRequest
        fields = ('name', 'phone_number')

    def create(self, validate_data):
        instance = super(PhoneRequestSerializer, self).create(validate_data)
        send_mail(
            subject='Уведоvление: заказ телефонного звонка',
            message=dict_to_str(validate_data),
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=['panda-kids33@yandex.ru'],
            fail_silently=False,
        )
        return instance


class PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Picture
        fields = ('image', 'text', 'title', 'id')


def dict_to_str(data):
    message = ''
    for key, value in data.items():
        message += key + ' : ' + value + '\n'
    return message