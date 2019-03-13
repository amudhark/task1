from django.db import models
import datetime
# Create your models here.
class Post(models.Model):
    Year = models.PositiveSmallIntegerField(blank=False, null=False, default=2019)
    Month = models.CharField(max_length=100, null=False, blank=False, default='March')
    Date = models.DateTimeField(null=False)
    Shift = models.TextField(null=False)
    Day_Of_Week = models.TextField(null=False)
    Time = models.TimeField(blank=False)
    Responded_Time =  models.TimeField(blank=False)
    Time_spent = models.TimeField(blank=False)
    Complexity = models.CharField(max_length=10)
    Responsible_Team = models.CharField(max_length=100, null=True, blank=False, default='Please select')
    False_Alarm = models.TextField(null=False, default='No')
    Incident_Type = models.CharField(max_length=100, null=True, blank=False, default='Please select')
    Priority = models.TextField(null=False, default='None')
    Name = models.CharField(max_length=100, null=True, blank=False, default='Please select')
    If_Others_Please_Specify = models.CharField(max_length=100,null=False, default='NA')
    Description = models.TextField(null=True, blank=False)
    Environment = models.CharField(max_length=100, null=True, blank=False, default='Please select')
    Host_Type = models.CharField(max_length=100, null=True, blank=False, default='Please select')
    Host_Name = models.CharField(max_length=100, null=True, blank=False)
    Source_of_Alert = models.CharField(max_length=100, null=True, blank=False, default='Please select')
    Mode_of_Alert = models.TextField(null=False, default='Manual check')
    NOC_Engineer = models.CharField(max_length=100, null=True, blank=False, default='Please select')
    Remediation = models.TextField(null=False,default='No')
    Escalated = models.TextField(null=False, default='NA')
    Escalated_Reason = models.CharField(max_length=100, null=True, blank=False, default='Please select')
    Status = models.CharField(max_length=100, null=True, blank=False, default='Resolved')
    Escalated_to = models.CharField(max_length=100, null=True, blank=False, default='NA')
    Resolved_by_Team = models.CharField(max_length=100, null=True, blank=False, default='Please select')
    Resolved_by_Engineer = models.CharField(max_length=30,null=False, default='noc')
    Resolution = models.TextField(null=False,default='NA')
    Comments = models.TextField(null=True,default='NA')



    def __str__(self):
        return self.title

    #pub_data = models.DateTimeField()
    #image = models.ImageField(upload_to='media/')
    #body = models.TextField()
    #Time_spent = models.TimeField(_(u"Responded Time"), blank=False)
