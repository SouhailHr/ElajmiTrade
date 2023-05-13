from django.db import models

# Create your models here.

category_choices = (

    ('Agri-food', 'Agri-food'),
    ('Building materials', 'Building materials'),
    ('Hardware items', 'Hardware items'),
    ('Sanitary facilities', 'Sanitary facilities'),
    ('Hygienic & cleaning products', 'Hygienic & cleaning products'),
    ('Cosmetic products', 'Cosmetic products'),
)

class Product(models.Model):
    category = models.CharField(max_length=50, choices=category_choices, default='')
    image = models.ImageField(upload_to='images/%y/%m/%d/', max_length=255, null=False, blank=False)
    name = models.CharField(max_length=254, default='')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
            ordering = ['-created']
            ordering = ['-updated']