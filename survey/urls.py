from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("depression-survey-question", views.depression_questions),
    path("depression-survey-uwc", views.depression_survey_uwc, name="depression_survey_uwc"),
    path("depression-survey-ww", views.depression_survey_ww, name="depression_survey_ww"),
    path("output-uwc/yes", views.yes, name="yes"),
    path("output-uwc/no", views.no, name="no"),
    path("confirm", views.confirm, name="confirm"),
    path("output-uwc/thank", views.thank, name="thank"),
    path("setup", views.setup, name="setup"),
    path("output-uwc/", views.output_uwc, name="output_uwc"),
    path("output-ww/", views.output_ww, name="output_ww"),
    path("output-ww/no", views.ww_no, name="ww_no"),
    path("cdc.gov/mentalhealth/learn/index.htm/", views.re, name="re"),
]
