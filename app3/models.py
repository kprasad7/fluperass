from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone

def validate_date(date):
    if date < timezone.now().date():
        raise ValidationError("Date cannot be in the past")


class Category(models.Model):
    cat_name = models.CharField(max_length=10)
    created_date = models.DateTimeField(auto_now_add=True , null=True, blank=True, validators=[validate_date])
    cat_image = models.FileField(upload_to="img/%y")
    is_active = models.BooleanField(default=True)
    
    

    


