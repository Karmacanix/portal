from django.db import models
from django.contrib.auth import get_user_model

UserModel = get_user_model()


# Create your models here.
class ActiveCampaignManager(models.Manager):
    def get_active_campaigns(self):
        return super().get_queryset().filter(active=True)
    

class Campaign(models.Model):
    name = models.CharField(max_length=60)
    start_date = models.DateField(verbose_name="Start")
    end_date = models.DateField(verbose_name="End")
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    sponsor = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    # fk m2m Goals
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    active_campaigns = ActiveCampaignManager()

    class Meta:
        ordering = ["-name"]

    def get_absolute_url(self):
        return f"/campaign/{self.pk}/"
    
    def __str__(self):
        return self.name


class TargetAudience(models.Model):
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    GENERATIONS_CHOICES = [
        ("Silt", "Silent Gen: 1925-1945"),
        ("Baby", "Baby Boomers: 1946-1964"),
        ("GenX", "Gen X: 1965-1979"),
        ("Xenn", "Xennials: 1975-1985"),
        ("Mill", "Millennials, GenY: 1980-1994"),
        ("iGen", "iGen/GenZ: 1995-2012"),
        ("GenA", "Gen Alpha: 2013-2025"),
    ]
    generation = models.CharField(
        max_length=4,
        choices=GENERATIONS_CHOICES,
        default="GenX",
        help_text="Select target generation:",
    )
    need = models.CharField(max_length=120, help_text="What need is being satisfied?")
    INCOME_BRACKET_CHOICES = [
            ("000K010K", "$1-$10,000"),
            ("010K020K", "$10,001-$20,000"),
            ("020K030K", "$20,001-$30,000"),
            ("030K040K", "$30,001-$40,000"),
            ("040K050K", "$40,001-$50,000"),
            ("050K060K", "$50,001-$60,000"),
            ("060K070K", "$60,001-$70,000"),
            ("070K080K", "$70,001-$80,000"),
            ("080K090K", "$80,001-$90,000"),
            ("090K100K", "$90,001-$100,000"),
            ("100K110K", "$100,001-$110,000"),
            ("110K120K", "$110,001-$120,000"),
            ("120K130K", "$120,001-$130,000"),
            ("130K140K", "$130,001-$140,000"),
            ("140K150K", "$140,001-$150,000"),
            ("150K160K", "$150,001-$160,000"),
            ("160K170K", "$160,001-$170,000"),
            ("170K180K", "$170,001-$180,000"),
            ("180K190K", "$180,001-$190,000"),
            ("190K200K", "$190,001-$200,000"),
            ("200K210K", "$200,001-$210,000"),
            ("210K220K", "$210,001-$220,000"),
            ("220K230K", "$220,001-$230,000"),
            ("230K240K", "$230,001-$240,000"),
            ("240K250K", "$240,001-$250,000"),
            ("250K260K", "$250,001-$260,000"),
            ("260K270K", "$260,001-$270,000"),
            ("270K280K", "$270,001-$280,000"),
            ("280K290K", "$280,001-$290,000"),
            ("300K300K", "$290,001-$300,000"),
            ("300K300P", "$300,001 and over"),
        ]
    income_bracket = models.CharField(
        max_length=8,
        choices=INCOME_BRACKET_CHOICES,
        default="050K060K",
        help_text="Select target income bracket:",
    )
    PROFESSIONAL_GROUP_CHOICES = [
            ("MANG", "Managers"),
            ("PROF", "Professionals"),
            ("TRAD", "Technicians and Trade Workers"),
            ("COMM", "Community and Personal Service Workers"),
            ("ADMN", "Clerical And Administration Workers"),
            ("SALE", "Sales Workers"),
            ("OPER", "Machinery Operators and Drivers"),
            ("LABR", "Labourers"),
        ]
    professional_group = models.CharField(
        max_length=4,
        choices=PROFESSIONAL_GROUP_CHOICES,
        default="LABR",
        help_text="Select target professional group:",
    )

    def get_absolute_url(self):
        return f"/targetaudience/{self.pk}/"
    
    @property
    def scode(self):
        return '-'.join([self.pk, '-', self.campaign, '-', self.generation, '-',self.need])