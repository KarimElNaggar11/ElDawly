from django.db import models
from django.core.validators import MinValueValidator
from django.utils.text import slugify

class PropertyType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Property Types"

class Feature(models.Model):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=50, blank=True)  # For FontAwesome icons
    
    def __str__(self):
        return self.name

class Property(models.Model):
    STATUS_CHOICES = [
        ('available', 'Available'),
        ('rented', 'Rented'),
        ('sold', 'Sold'),
        ('reserved', 'Reserved'),
    ]
    
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField()
    property_type = models.ForeignKey(PropertyType, on_delete=models.CASCADE)
    features = models.ManyToManyField(Feature, blank=True)
    
    # Location
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100, default='Vienna')
    district = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=10)
    
    # Property Details
    price = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.DecimalField(max_digits=8, decimal_places=2, validators=[MinValueValidator(0)])
    rooms = models.PositiveIntegerField()
    bathrooms = models.PositiveIntegerField()
    floor = models.IntegerField()
    year_built = models.PositiveIntegerField()
    
    # Status
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available')
    is_featured = models.BooleanField(default=False)
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "Properties"
        ordering = ['-created_at']

class PropertyImage(models.Model):
    property = models.ForeignKey(Property, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='properties/')
    is_primary = models.BooleanField(default=False)
    caption = models.CharField(max_length=200, blank=True)
    
    def __str__(self):
        return f"Image for {self.property.title}"
    
    class Meta:
        ordering = ['-is_primary', 'id']
