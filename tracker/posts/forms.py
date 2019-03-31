from django import forms
from django.contrib.auth.models import User
from django.utils import timezone
import datetime
from . import models
from django.utils.safestring import mark_safe
from django.forms import widgets
from django.db.models.fields import BLANK_CHOICE_DASH
from datetime import date
#class HorizontalRadioRenderer(forms.RadioSelect):
#   def render(self, name, value, attrs=None, renderer=None):
#     return mark_safe(u'\n'.join([u'%s\n' % w for w in self]))

class CreateArticle(forms.ModelForm):

    weeknumber = date.today().isocalendar()[1]
    Week = forms.IntegerField(initial=weeknumber)


    shift_choices=(('apac','APAC'),('emea','EMEA'),('usa','USA'))
    currentTime = datetime.datetime.now().hour
    x = ""
    if currentTime in range (5, 14, 1):
        x = ("apac")
    elif currentTime in range (14, 22, 1):
        x = ("emea")
    elif currentTime in range (22, 5, 1):
        x = ("usa")

    Shift = forms.ChoiceField(choices=shift_choices, widget=forms.RadioSelect, initial=x)

    #Date = forms.DateField(widget=forms.SelectDateWidget(), initial = timezone.now)

    Day_Of_Week=(('Weekday','Weekday'),('Weekend','Weekend'))
    weekno = datetime.datetime.today().weekday()

    if weekno<5:
        x = ("Weekday")
    else:
        x = ("Weekend")

    Day_Of_Week = forms.ChoiceField(choices=Day_Of_Week, widget=forms.RadioSelect, initial=x)

    Time = forms.DateTimeField(input_formats=['%H:%M'])

    Responded_Time = forms.DateTimeField(input_formats=['%H:%M'])

    MONTH_CHOICES = (
    ('1', 'January'),
    ('2', 'February'),
    ('3', 'March'),
    ('4', 'April'),
    ('5', 'May'),
    ('6', 'June'),
    ('7', 'July'),
    ('8', 'August'),
    ('9', 'September'),
    ('10', 'October'),
    ('11', 'November'),
    ('12', 'December'),
)
    today = datetime.date.today()
    #months = ['January','February','March','April','May','June','July','August','September','October','November','December']
    #current_month = months[today.month]
    months = today.month
    Month = forms.ChoiceField(choices=MONTH_CHOICES,initial=months)

    Res_team = (
    ('B2B - Core', 'B2B - Core'),
    ('B2B - Data', 'B2B - Data'),
    ('B2B - Reporting', 'B2B - Reporting'),
    ('Beehive', 'Beehive'),
    ('BI', 'BI'),
    ('Data Infra', 'Data Infra'),
    ('Data Prod', 'Data Prod'),
    ('Data Science', 'Data Science'),
    ('Dev', 'Dev'),
    ('Dynamic Cretive', 'Dynamic Cretive'),
    ('Facebook', 'Facebook'),
    ('Growth', 'Growth'),
    ('Growth IO', 'Growth IO'),
    ('Internal Tools', 'Internal Tools'),
    ('IT', 'IT'),
    ('NA', 'NA'),
    ('NOC', 'NOC'),
    ('omnom', 'omnom'),
    ('Prospecting', 'Prospecting'),
    ('Rakuten', 'Rakuten'),
    ('RTB', 'RTB'),
    ('Sendroll', 'Sendroll'),
    ('SRE', 'SRE'),
    ('TAM', 'TAM'),
    ('Voltron', 'Voltron'),
    ('Webapp', 'Webapp'),
)
    Res_team_empty =  tuple(BLANK_CHOICE_DASH + list(Res_team))
    Responsible_Team = forms.ChoiceField(choices=(Res_team_empty))

    fse_alarm=(('Yes','Yes'),('No','No'))
    False_Alarm = forms.ChoiceField(choices=fse_alarm, widget=forms.RadioSelect, initial='No')

    inc_type = (
    ('Alert', 'Alert'),
    ('GHC', 'GHC'),
    ('Other', 'Other'),
    ('Security Audit', 'Security Audit'),
    ('Task', 'Task'),
)
    inc_type_empty = tuple(BLANK_CHOICE_DASH + list(inc_type))
    Incident_Type = forms.ChoiceField(choices=(inc_type_empty))

    prior=(('None','P0'),('P1','P1'),('P2','P2'),('None','None'))
    Priority = forms.ChoiceField(choices=prior, widget=forms.RadioSelect, initial='no')



    name = (
    ('Celery Dashboard check', 'Celery Dashboard check'),
    ('Dashboard monitoring', 'Dashboard monitoring'),
    ('Pipeline monitoring', 'Pipeline monitoring'),
    ('Storm Monitoring', 'Storm Monitoring'),
)
    name_empty = tuple(BLANK_CHOICE_DASH + list(name))
    Name = forms.ChoiceField(choices=(name_empty))

    envi = (
    ('Production', 'Production'),
    ('Staging', 'Staging'),
    ('Test', 'Test'),
    ('Dev', 'Dev'),
    ('Local', 'Local'),
    ('Multiple', 'Multiple'),
    ('NA', 'NA'),
)
    envi_empty = tuple(BLANK_CHOICE_DASH + list(envi))
    Environment = forms.ChoiceField(choices=(envi_empty))

    hosttype = (
    ('AWS Batch', 'AWS Batch'),
    ('AWS ECS', 'AWS ECS'),
    ('AWS EC2', 'AWS EC2'),
    ('AWS Elasticache', 'AWS Elasticache'),
    ('emr', 'AWS EMR'),
    ('AWS RDS', 'AWS RDS'),
    ('Batchie Patchie', 'Batchie Patchie'),
    ('Celery Worker', 'Celery Worker'),
    ('Docker Registry', 'Docker Registry'),
    ('Docker Server', 'Docker Server'),
    ('Hbase cluster', 'Hbase cluster'),
    ('Jenkins', 'Jenkins'),
    ('Load Balancer', 'Load Balancer'),
    ('Localhost', 'Localhost'),
    ('Luigi', 'Luigi'),
    ('NA', 'NA'),
    ('Other', 'Other'),
    ('Presto', 'Presto'),
    ('Puppet', 'Puppet'),
    ('puppet', 'Puppet'),
    ('Quentin', 'Quentin'),
    ('Strom cluster', 'Strom cluster'),
    ('Thrift Cluster', 'Thrift Cluster'),
)
    hosttype_empty = tuple(BLANK_CHOICE_DASH + list(hosttype))
    Host_Type = forms.ChoiceField(choices=(hosttype_empty))

    source = (
    ('AWS', 'AWS'),
    ('Celery', 'Celery'),
    ('DataDog', 'DataDog'),
    ('Icinga', 'Icinga'),
    ('Jenkins', 'Jenkins'),
    ('Logentries', 'Logentries'),
    ('NA', 'NA'),
    ('New Relic', 'New Relic'),
    ('Pingdom', 'Pingdom'),
    ('Sentry', 'Sentry'),
    ('Slack', 'Slack'),
    ('Threatstack', 'Threatstack'),
)
    source_empty = tuple(BLANK_CHOICE_DASH + list(source))
    Source_of_Alert = forms.ChoiceField(choices=(source_empty))

    mode=[('Email','Email'),('Manual Check','Manual Check'),('Slack','Slack')]
    Mode_of_Alert = forms.ChoiceField(choices=mode, widget=forms.RadioSelect, initial='mc')

    engineer= (
    ('Ajmeer Khaja', 'Ajmeer Khaja'),
    ('Gowtham Perumalsamy', 'Gowtham Perumalsamy'),
    ('Hajamoideen Jailaudeen','Hajamoideen Jailaudeen'),
    ('Irfan Junaid', 'Irfan Junaid'),
    ('MIS team', 'MIS team'),
    ('QA team', 'QA team'),
    ('Rajaram Ganesapandian', 'Rajaram Ganesapandian'),
    ('Ramesh Krishna', 'Ramesh Krishna'),
    ('Rohit Nannan', 'Rohit Nannan'),
    ('Shivani Ramesh', 'Shivani Ramesh'),
    ('Thirumalaibarathi Thangavelu', 'Thirumalaibarathi Thangavelu'),
    ('Umashree Ramesh', 'Umashree Ramesh'),
    ('Vijay Mohan', 'Vijay Mohan'),
)
    engineer_empty = tuple(BLANK_CHOICE_DASH + list(engineer))
    NOC_Engineer = forms.ChoiceField(choices=(engineer_empty))

    escalate=[('Yes','Yes'),('No','No')]
    #Escalated = forms.ChoiceField(choices=escalate, widget=forms.RadioSelect, initial='no')
    escalate_empty = tuple(BLANK_CHOICE_DASH + list(escalate))
    Escalated = forms.ChoiceField(choices=(escalate_empty), initial='No')

    escreason = (
    ('Code level issue', 'Code level issue'),
    ('Configuration Changes', 'Configuration Changes'),
    ('Requesting Remediation', 'Requesting Remediation'),
    ('Unable to Resolve', 'Unable to Resolve'),
    ('Review Needed', 'Review Needed'),
    ('No Access', 'No Access'),
    ('NA', 'NA'),
)
    escreason_empty = tuple(BLANK_CHOICE_DASH + list(escreason))
    Escalated_Reason = forms.ChoiceField(choices=(escreason_empty), required=False)

    stat = (
    ('Resolved', 'Resolved'),
    ('Pending', 'Pending'),
    ('Pending Followup', 'Pending Followup'),
    ('Handed over', 'Handed over')
    )
    stat_empty = tuple(BLANK_CHOICE_DASH + list(stat))
    Status = forms.ChoiceField(choices=(stat_empty))

    escto = (
    ('B2B core', 'B2B core'),
    ('B2B reporting', 'B2B reporting'),
    ('B2B Data', 'B2B Data'),
    ('Beehive', 'Beehive'),
    ('BI', 'BI'),
    ('Data-Infra', 'Data-Infra'),
    ('Data-Prod', 'Data-Prod'),
    ('Data-Sci', 'Data-Sci'),
    ('Dev', 'Dev'),
    ('Dynamic Creative', 'Dynamic Creative'),
    ('Facebook', 'Facebook'),
    ('Growth', 'Growth'),
    ('GrowthIO', 'GrowthIO'),
    ('Internal tools', 'Internal tools'),
    ('IT', 'IT'),
    ('NA', 'NA'),
    ('NOC', 'NOC'),
    ('Omnom', 'Omnom'),
    ('Prospecting', 'Prospecting'),
    ('Rakuten', 'Rakuten'),
    ('RTB', 'RTB'),
    ('Sendroll', 'Sendroll'),
    ('SRE', 'SRE'),
    ('TAM', 'TAM'),
    ('Voltron', 'Voltron'),
    ('Webappp', 'Webappp'),
)
    escto_empty = tuple(BLANK_CHOICE_DASH + list(escto))
    Escalated_to = forms.ChoiceField(choices=(escto_empty), required=False)

    resby = (
    ('B2B core', 'B2B core'),
    ('B2B reporting', 'B2B reporting'),
    ('B2B Data', 'B2B Data'),
    ('Beehive', 'Beehive'),
    ('BI', 'BI'),
    ('Data-Infra', 'Data-Infra'),
    ('Data-Prod', 'Data-Prod'),
    ('Data-Sci', 'Data-Sci'),
    ('Dev', 'Dev'),
    ('Dynamic Creative', 'Dynamic Creative'),
    ('Facebook', 'Facebook'),
    ('Growth', 'Growth'),
    ('GrowthIO', 'GrowthIO'),
    ('Internal tools', 'Internal tools'),
    ('IT', 'IT'),
    ('NA', 'NA'),
    ('NOC', 'NOC'),
    ('Omnom', 'Omnom'),
    ('Prospecting', 'Prospecting'),
    ('Rakuten', 'Rakuten'),
    ('RTB', 'RTB'),
    ('Sendroll', 'Sendroll'),
    ('SRE', 'SRE'),
    ('TAM', 'TAM'),
    ('Voltron', 'Voltron'),
    ('Webappp', 'Webappp'),
)
    resby_empty = tuple(BLANK_CHOICE_DASH + list(resby))
    Resolved_by_Team = forms.ChoiceField(choices=(resby_empty))


    class Meta:
        model = models.Post
        fields = '__all__'
        field_order = ['Year','Month','Week','Date','Shift','Day_Of_Week','Time','Responded_Time','Time_spent','Complexity','Responsible_Team','False_alarm','Incident_Type','Priority','If_Others_Please_Specify','Description','Environment','Host_Type','Host_Name','Source_of_Alert','Mode_of_Alert','NOC_Engineer','Remediation','Escalated',
        'Escalated_Reason','Status','Escalated_to','Resolved_by_Team','Resolved_by_Engineer','Resolution','Comments']










































'''
    def __init__(self, *args, **kwargs):
        super(CreateArticle, self).__init__(*args, **kwargs)
        self.fields['Escalated'].widget = TextInput(attrs={
            'id': 'myCustomId',
            'class': 'myCustomClass',
            'name': 'myCustomName',
            'placeholder': 'myCustomPlaceholder'})

    def clean(self):
       Incident_Type = self.cleaned_data.get('Incident_Type')
       if Incident_Type == 'Alert':
           Priority = prior['P1']

        def create_user(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        do_something_with(form.cleaned_data)
        return redirect("create_user_success")

    return render_to_response("signup/form.html", {'form': form})


    def create_user(request):
    extra_questions = get_questions(request)
    form = UserCreationForm(request.POST or None, extra=extra_questions)
    if form.is_valid():
        for (question, answer) in form.extra_answers():
            save_answer(request, question, answer)
        return redirect("create_user_success")

    return render_to_response("signup/form.html", {'form': form})
'''