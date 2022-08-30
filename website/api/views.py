from django.core.mail import send_mail
from django.conf import settings

from rest_framework import generics

from .models import Question, Comment, PhoneRequest, Application, Picture
from .serializers import QuestionSerializer, CommentSerializer, PhoneRequestSerializer, ApplicationSerializer, \
    PictureSerializer


class ApplicationAPIView(generics.CreateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

    def create(self, request, *args, **kwargs):
        super().create(request, *args, **kwargs)
        print(request)


class QuestionAPIView(generics.CreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class CommentAPIView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class PhoneRequestAPIView(generics.CreateAPIView):
    queryset = PhoneRequest.objects.all()
    serializer_class = PhoneRequestSerializer


class PictureAPIView(generics.ListAPIView):
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer
