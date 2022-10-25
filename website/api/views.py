from django.core.mail import send_mail
from django.conf import settings

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from .models import Question, Comment, PhoneRequest, Application, Picture
from .serializers import QuestionSerializer, CommentSerializer, PhoneRequestSerializer, ApplicationSerializer, \
    PictureSerializer


class ApplicationAPIView(generics.CreateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer


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

    def list(self, request, *args, **kwargs):
        result = super().list(request, *args, **kwargs)
        try:
            offset = int(request.query_params['offset'])
            page = int(request.query_params['page'])
        except:
            return result

        start = offset * page
        queryset = Picture.objects.all()[start: start + offset]
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)



