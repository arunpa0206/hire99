from __future__ import unicode_literals
from django.db import models
import datetime
# Create your models here.
#Maps to Job table that has all jobs
class Job(models.Model):
    company_name = models.CharField(verbose_name="Company", max_length=500,)
    job_title = models.CharField(verbose_name="Title", max_length=500,)
    job_location = models.CharField(verbose_name="Location", max_length=500,)
    job_description = models.TextField(verbose_name="Job Description", max_length=10000,)
    job_status = models.CharField(verbose_name="Status", max_length=500,)
    skill_set = models.CharField(verbose_name="Skill Set", max_length=500,)
    keywords = models.CharField(verbose_name="Keywords", max_length=500,)
    creation_date = models.DateTimeField('date created')

class FwUsers(models.Model):
    l_id = models.AutoField(primary_key=True)
    fw_id = models.CharField(max_length=500)
    user_fname = models.CharField(verbose_name="First Name", max_length=500)
    user_lname = models.CharField(verbose_name="Last Name", max_length=500)
    user_email = models.EmailField(verbose_name="Email", max_length=500)
    user_mobile = models.BigIntegerField(verbose_name="Mobile")
    hq_mark = models.DecimalField(verbose_name="Highest Qualification Mark", max_digits=12, decimal_places=2)
    hq_mark_type = models.CharField(max_length=500)
    course_id = models.CharField(max_length=500)
    course_name = models.CharField(verbose_name="Qualification", max_length=500)
    branch_id = models.CharField(max_length=500)
    user_lat = models.CharField(max_length=500)
    user_long = models.CharField(max_length=500)
    resume_path = models.CharField(max_length=500)
    flag_mobile_verified = models.IntegerField()
    dob = models.DateField(blank=True, null=True)
    inst_state_id = models.CharField(max_length=500, blank=True, null=True)
    last_login = models.DateField(blank=True, null=True)
    user_state_id = models.IntegerField(blank=True, null=True)
    user_state_name = models.CharField(verbose_name="State", max_length=500)
    job_type = models.CharField(max_length=500, blank=True, null=True)
    branch_name = models.CharField(verbose_name="Branch", max_length=500, blank=True, null=True)
    user_keywords = models.CharField(verbose_name="Keywords", max_length=500, blank=True, null=True)
    subloc_id = models.CharField(max_length=500, blank=True, null=True)
    contact_no = models.CharField(max_length=500, blank=True, null=True)
    user_city_name = models.CharField(verbose_name="City", max_length=500, blank=True, null=True)
    user_qual_type = models.CharField(max_length=500, blank=True, null=True)
    user_pic_path = models.CharField(max_length=500, blank=True, null=True)
    hq_inst_id = models.IntegerField(blank=True, null=True)
    user_sex = models.CharField(verbose_name="Gender", max_length=500, blank=True, null=True)
    flag_resume = models.IntegerField(blank=True, null=True)
    user_skills = models.CharField(verbose_name="Skill Set", max_length=500, blank=True, null=True)
    branch_sname = models.CharField(max_length=500, blank=True, null=True)
    subloc_name = models.CharField(max_length=500, blank=True, null=True)
    hq_passout_year = models.IntegerField(verbose_name="Passout Year", blank=True, null=True)
    user_city_id = models.CharField(max_length=500, blank=True, null=True)
    fw_uid = models.CharField(max_length=500, blank=True, null=True)
    univ_name = models.CharField(verbose_name="University Name", max_length=500, blank=True, null=True)
    univ_id = models.IntegerField(blank=True, null=True)
    inst_name = models.CharField(verbose_name="Institution", max_length=500, blank=True, null=True)

    user_cdate = models.DateField('Creation Date',default=datetime.datetime.now, blank=True, null=True)

    class Meta:
        db_table = 'fw_users'
