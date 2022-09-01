from django.core.mail import send_mail
from django.conf import settings

from rest_framework import generics
from rest_framework.response import Response

from .models import Question, Comment, PhoneRequest, Application, Picture
from .serializers import QuestionSerializer, CommentSerializer, PhoneRequestSerializer, ApplicationSerializer, \
    PictureSerializer


class ApplicationAPIView(generics.CreateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

    def create(self, request, *args, **kwargs):
        send_mail(
            subject='Уведобление: заявка на поступление',
            message=dict_to_str(request.data),
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=['panda-kids33@yandex.ru']
        )

        return super().create(request, *args, **kwargs)


class QuestionAPIView(generics.CreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def create(self, request, *args, **kwargs):
        send_mail(
            subject='Уведобление: запись на экскурсию',
            message=dict_to_str(request.data),
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=['panda-kids33@yandex.ru']
        )

        return super().create(request, *args, **kwargs)


class CommentAPIView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def create(self, request, *args, **kwargs):
        send_mail(
            subject='Уведобление: новый комментарий',
            message=dict_to_str(request.data),
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=['panda-kids33@yandex.ru']
        )

        return super().create(request, *args, **kwargs)


class PhoneRequestAPIView(generics.CreateAPIView):
    queryset = PhoneRequest.objects.all()
    serializer_class = PhoneRequestSerializer

    def create(self, request, *args, **kwargs):
        send_mail(
            subject='Уведобление: заказ телефонного звонка',
            message=dict_to_str(request.data),
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=['panda-kids33@yandex.ru']
        )

        return super().create(request, *args, **kwargs)


class PictureAPIView(generics.ListAPIView):
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer

    def list(self, request, *args, **kwargs):
        result = super().list(request, *args, **kwargs)
        try:
            offset = int(request.query_params['offset'])
            page = int(request.query_params['page'])
        except:
            return result

        start = offset * page
        queryset = Picture.objects.all()[start: start+offset]
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


def dict_to_str(data):
    message = ''
    for key, value in data.items():
        message += key + ' : ' + value + '\n'
    return message
