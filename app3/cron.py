from app3.models import Category
def my_scheduled():
    Category.objects.all().update(is_active=False)