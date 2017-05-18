from django import forms
from .models import Job, FwUsers
import django_filters


class JobFilter(django_filters.FilterSet):
    keywords = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Job
        fields = {
            'company_name': ['icontains',],
            'job_location': ['exact',],
            'job_title': ['icontains',],
            'skill_set': ['icontains',],
        }

class CandidateFilter(django_filters.FilterSet):
    user_keywords = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = FwUsers
        fields = {
            'user_fname': ['icontains',],
            'user_lname': ['icontains',],
            'user_sex' : ['exact',],
            'user_city_name': ['icontains',],
            'hq_passout_year': ['exact',],
            'course_name': ['icontains'],
        }
