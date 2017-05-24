from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Job, FwUsers
from .filters import JobFilter, CandidateFilter
from django.views import generic
from django.views.generic.edit import CreateView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
def jobsearch(request):

    job_list = Job.objects.all()
    job_filter = JobFilter(request.GET, queryset=job_list)
    return render(request, 'job_list.html', {'filter': job_filter})

def jobdetail(request):

    job_list = Job.objects.all()
    job_filter = JobFilter(request.GET, queryset=job_list)
    return render(request, 'job_detail.html', {'filter': job_filter})

def get_context_data(self, **kwargs):
    get_copy = request.GET.copy()
    parameters = get_copy.pop('page', True) and get_copy.urlencode()
    context['parameters'] = parameters
    return context

def candidatesearch(request):
    candidate_list = FwUsers.objects.filter(user_cdate__gte='2017-05-15')
    candidate_filter = CandidateFilter(request.GET, queryset=candidate_list)

    paginator = Paginator(candidate_filter.qs, 25)
    page = request.GET.get('page',1)
#    context['page']=page


    try:
        candidates = paginator.page(page)
    except PageNotAnInteger:
        candidates = paginator.page(1)
    except EmptyPage:
        candidates = paginator.page(paginator.num_pages)
    return render(request, 'candidate_list.html', {'candidates': candidates, 'filter': candidate_filter})

def candidateform(request):
    return render(request, 'candidate_form.html',)

class CandidateCreate (CreateView):
    model = FwUsers
    fields = ['user_fname','user_lname','user_email',
                'user_mobile','contact_no', 'flag_mobile_verified',
                'dob', 'user_sex',
                'user_city_name', 'user_state_name',
                'course_name', 'branch_name', 'hq_passout_year',
                'hq_mark','inst_name','univ_name',
                'job_type', 'user_skills', 'user_keywords'
                ]
    template_name = "candidate_form.html"
    success_url = "/candidateform"
