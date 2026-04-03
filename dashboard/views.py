from django.shortcuts import render
from inventory.models import Material

def dashboard_home(request):
    total_materials = Material.objects.count()
    low_stock_count = Material.objects.filter(quantity__lte=10).count()
    latest_material = Material.objects.last()

    context = {
        'total_materials': total_materials,
        'low_stock_count': low_stock_count,
        'latest_material': latest_material,
    }
    return render(request, 'dashboard/dashboard.html', context)
