from django.contrib import admin
from django.urls import path, include

from .views import QuestionAPIView, CommentAPIView, PhoneRequestAPIView, ApplicationAPIView, PictureAPIView

app_name = 'api'
urlpatterns = [
    path('create-application', ApplicationAPIView.as_view(), name='create_application'),
    path('create-question', QuestionAPIView.as_view(), name='create_question'),
    path('create-comment', CommentAPIView.as_view(), name='create_comment'),
    path('create-phone-request', PhoneRequestAPIView.as_view(), name='create_phone_request'),
    path('get-pictures', PictureAPIView.as_view(), name='get_pictures')
]
