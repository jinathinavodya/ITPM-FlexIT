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




# diliya
class Cvdetails(models.Model):

    name = models.CharField(max_length=100, null=True)
    nic = models.CharField(max_length=20, null=True)
    date_of_birth = models.DateField(max_length=20, null=True)
    address = models.CharField(max_length=100, null=True)
    mobile_contact = models.CharField(max_length=10, null=True)
    home_contact = models.CharField(max_length=10, null=True)
    email = models.CharField(max_length=100, null=True)
    experience = models.CharField(max_length=100, null=True)
    ol_result = models.CharField(max_length=100, null=True)
    al_stream = models.CharField(max_length=100, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)


    def __str__(self):
        return self.name

class Skill(models.Model):
    class Meta:
        verbose_name_plural = 'Skills'
        verbose_name = 'Skill'
    
    name = models.CharField(max_length=20, blank=True, null=True)
    score = models.IntegerField(default=80, blank=True, null=True)
    image = models.FileField(blank=True, null=True, upload_to="skills")
    is_key_skill = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name

# class UserProfile(models.Model):

#     class Meta:
#         verbose_name_plural = 'User Profiles'
#         verbose_name = 'User Profile'
    
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     avatar = models.ImageField(blank=True, null=True, upload_to="avatar")
#     title = models.CharField(max_length=200, blank=True, null=True)
#     bio = models.TextField(blank=True, null=True)
#     skills = models.ManyToManyField(Skill, blank=True)
#     cv = models.FileField(blank=True, null=True, upload_to="cv")

#     def __str__(self):
#         return f'{self.user.first_name} {self.user.last_name}'

class Media(models.Model):

    class Meta:
        verbose_name_plural = 'Media Files'
        verbose_name = 'Media'
        ordering = ["name"]
	
    image = models.ImageField(blank=True, null=True, upload_to="media")
    url = models.URLField(blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    is_image = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if self.url:
            self.is_image = False
        super(Media, self).save(*args, **kwargs)
    def __str__(self):
        return self.name

class Portfolio(models.Model):

    class Meta:
        verbose_name_plural = 'Portfolio Profiles'
        verbose_name = 'Portfolio'
        ordering = ["name"]
    date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    body = RichTextField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to="portfolio")
    slug = models.SlugField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Portfolio, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/portfolio/{self.slug}"