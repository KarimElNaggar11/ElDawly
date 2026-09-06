from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q
from django.views.generic import ListView, DetailView
from .models import Property, PropertyType, Feature

class PropertyListView(ListView):
    model = Property
    template_name = 'properties/property_list.html'
    context_object_name = 'properties'
    paginate_by = 9
    
    def get_queryset(self):
        queryset = Property.objects.all()
        
        # Filter by property type
        property_type = self.request.GET.get('type')
        if property_type:
            queryset = queryset.filter(property_type__name=property_type)
        
        # Filter by price range
        min_price = self.request.GET.get('min_price')
        max_price = self.request.GET.get('max_price')
        if min_price:
            queryset = queryset.filter(price__gte=min_price)
        if max_price:
            queryset = queryset.filter(price__lte=max_price)
        
        # Filter by rooms
        rooms = self.request.GET.get('rooms')
        if rooms:
            queryset = queryset.filter(rooms=rooms)
        
        # Filter by district
        district = self.request.GET.get('district')
        if district:
            queryset = queryset.filter(district=district)
        
        # Search
        search_query = self.request.GET.get('q')
        if search_query:
            queryset = queryset.filter(
                Q(title__icontains=search_query) |
                Q(description__icontains=search_query) |
                Q(address__icontains=search_query) |
                Q(district__icontains=search_query)
            )
        
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['property_types'] = PropertyType.objects.all()
        context['features'] = Feature.objects.all()
        context['districts'] = Property.objects.values_list('district', flat=True).distinct()
        return context

class PropertyDetailView(DetailView):
    model = Property
    template_name = 'properties/property_detail.html'
    context_object_name = 'property'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['related_properties'] = Property.objects.filter(
            property_type=self.object.property_type
        ).exclude(id=self.object.id)[:3]
        return context

def home(request):
    featured_properties = Property.objects.filter(is_featured=True)[:6]
    latest_properties = Property.objects.all().order_by('-created_at')[:6]
    property_types = PropertyType.objects.all()
    
    context = {
        'featured_properties': featured_properties,
        'latest_properties': latest_properties,
        'property_types': property_types,
    }
    return render(request, 'properties/home.html', context)

def about(request):
    return render(request, 'properties/about.html')

def contact(request):
    if request.method == 'POST':
        # Handle contact form submission
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        # Add your email sending logic here
        return render(request, 'properties/contact.html', {'success': True})
    return render(request, 'properties/contact.html')
