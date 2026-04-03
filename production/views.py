from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import ProductionOrder
from .forms import ProductionOrderForm

@login_required
def production_home(request):
    orders = ProductionOrder.objects.all()
    return render(request, 'production/production_list.html', {'orders': orders})

@login_required
def add_order(request):
    form = ProductionOrderForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('production_home')
    return render(request, 'production/add_order.html', {'form': form})

@login_required
def update_status(request, pk):
    order = get_object_or_404(ProductionOrder, pk=pk)
    if request.method == 'POST':
        order.status = request.POST.get('status')
        order.save()
        return redirect('production_home')
    return render(request, 'production/update_status.html', {'order': order})
