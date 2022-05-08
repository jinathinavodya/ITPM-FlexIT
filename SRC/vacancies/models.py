from django.db import models

# Create your models here.

class vacancy (models.Model):
    WORKINGHOURS = (

        ('6h','6h'),
        ('7h','7h'),
        ('8h','8h'),
        ('9h','9h'),
        ('10h','10h'),

        )

    JOBTITLE= (

        ('Software Engineering','Software Engineering'),
        ('Big data engineer','Big data engineer'),
        ('DevOps Engineer','DevOps Engineer'),
        ('Information systems security manager','Information systems security manager'),
        ('Mobile applications developer','Mobile applications developer'),
        ('Database manager','Database manager'),
        ('Data scientist','Data scientist'),
        ('Network/cloud engineer','Network/cloud engineer'),
        
        )

    WORKSSTATUS= (

        ('Remote','Remote'),
        ('On-Site','On-Site'),
        ('Hybrid','Hybrid'),
      
        
        )

        
    NOOFAPPLICANTS = (

        ('1-5','1-5'),
        ('5-10','5-10'),
        ('10-20','10-20'),
        ('20-50','20-50'),
        ('50+','50+'),
        
        )

    EXPERIENCE = (

        ('Intern','Intern'),
        ('6 months','6 months'),
        ('1 Year','1 Year'),
        ('2 Year','2 Year'),
        ('3 Year','3 Year'),
        ('4 Year','4 Year'),
        ('5 Year','5 Year'),
        ('6 Year','6 Year'),
        ('6+','6+'),
        
        )

 



    company_name =  models.CharField(max_length=200,null=True)
    address =  models.CharField(max_length=200,null=True)
    company_type =  models.CharField(max_length=200,null=True)
    job_title =  models.CharField(max_length=200,null=True,choices=JOBTITLE)
    about_company =  models.CharField(max_length=200,null=True)
    Essentional_duties_responsibilities =  models.CharField(max_length=200,null=True)
    educational_requirements =  models.CharField(max_length=200,null=True)
    #works_status =  models.CharField(max_length=200,null=True,choices=WORKSSTATUS)
    #graduate_status =  models.CharField(max_length=200,null=True)
    #working_status =  models.CharField(max_length=200,null=True)
    working_hours =  models.CharField(max_length=200,null=True,choices=WORKINGHOURS)
    no_of_applicants =  models.CharField(max_length=200,null=True,choices=NOOFAPPLICANTS)
    experience =  models.CharField(max_length=200,null=True,choices=EXPERIENCE)
     

    def __str__(self) :
        return self.company_name