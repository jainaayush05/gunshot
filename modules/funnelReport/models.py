from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())

class GsFunnelFormula(models.Model):
    belongs_to = models.IntegerField(blank=True)
    f1 = models.IntegerField(blank=True)
    f2 = models.IntegerField(blank=True)
    type = models.CharField(max_length=255, blank=True)
    class Meta:
        managed = True
        db_table = 'gs_funnel_formula'

class GsFunnelLabel(models.Model):
    label = models.CharField(max_length=255, blank=True)
    parent = models.IntegerField(blank=True)
    type = models.CharField(max_length=255, blank=True)
    group_source_type = models.CharField(max_length=255, blank=True)
    display_order = models.IntegerField(blank=True) #

    class Meta:
        managed = True
        db_table = 'gs_funnel_label'

class GsFunnelDataMonthly(models.Model):
    metric_id = models.IntegerField(blank=True)
    value = models.CharField(max_length=255, blank=True)
    date = models.DateField(blank=True)
    
    class Meta:
        managed = True
        db_table = 'gs_funnel_data_monthly'