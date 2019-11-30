from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .api import ResumeList, ResumeDetail, ResumeAuthentication

# from resume import views

urlpatterns = [
    path('', ResumeList.as_view()),
    path('<int:company_id>/', ResumeDetail.as_view()),
    path('auth/', ResumeAuthentication.as_view())
]
urlpatterns = format_suffix_patterns(urlpatterns)
