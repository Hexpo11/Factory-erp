from django.shortcuts import render, redirect, get_object_or_404
from .models import Material

def inventory_list(request):
    materials = Material.objects.all()
    return render(request, 'inventory/inventory_list.html', {
        'materials': materials
    })


def add_material(request):
    if request.method == 'POST':
        name = request.POST['name']
        quantity = int(request.POST['quantity'])
        min_quantity = int(request.POST['min_quantity'])

        Material.objects.create(
            name=name,
            quantity=quantity,
            min_quantity=min_quantity
        )
        return redirect('inventory_list')

    return render(request, 'inventory/add_material.html')


def edit_material(request, pk):
    material = get_object_or_404(Material, pk=pk)

    if request.method == 'POST':
        material.name = request.POST['name']
        material.quantity = int(request.POST['quantity'])
        material.min_quantity = int(request.POST['min_quantity'])
        material.save()
        return redirect('inventory_list')

    return render(request, 'inventory/edit_material.html', {
        'material': material
    })


def delete_material(request, pk):
    material = get_object_or_404(Material, pk=pk)
    material.delete()
    return redirect('inventory_list')


def low_stock(request):
    materials = Material.objects.filter(quantity__lte=models.F('min_quantity'))
    return render(request, 'inventory/low_stock.html', {
        'materials': materials
    })
