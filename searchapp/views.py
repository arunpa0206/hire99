from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Job, FwUsers
from .filters import JobFilter, CandidateFilter
from django.views import generic

# Create your views here.
def jobsearch(request):

    job_list = Job.objects.all()
    job_filter = JobFilter(request.GET, queryset=job_list)
    return render(request, 'job_list.html', {'filter': job_filter})

def jobdetail(request):

    job_list = Job.objects.all()
    job_filter = JobFilter(request.GET, queryset=job_list)
    return render(request, 'job_detail.html', {'filter': job_filter})

def candidatesearch(request):

    candidate_list = FwUsers.objects.filter(user_cdate__gte='2017-05-10')

    candidate_filter = CandidateFilter(request.GET, queryset=candidate_list)
    return render(request, 'candidate_list.html', {'filter': candidate_filter})

def candidateform(request):

    return render(request, 'candidate_form.html',)
