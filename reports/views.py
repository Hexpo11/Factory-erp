from django.shortcuts import render
from django.http import HttpResponse
from django.db import models
from inventory.models import Material

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas


def reports_home(request):
    materials = Material.objects.all()

    # Filters
    name_query = request.GET.get("name", "")
    low_stock_only = request.GET.get("low_stock")

    if name_query:
        materials = materials.filter(name__icontains=name_query)

    if low_stock_only:
        materials = materials.filter(
            quantity__lte=models.F("min_quantity")
        )

    total_materials = materials.count()
    total_quantity = sum(m.quantity for m in materials)

    context = {
        "materials": materials,
        "total_materials": total_materials,
        "total_quantity": total_quantity,
        "name_query": name_query,
        "low_stock_only": low_stock_only,
    }
    return render(request, "reports/home.html", context)


def download_report_pdf(request):
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = 'attachment; filename="inventory_report.pdf"'

    pdf = canvas.Canvas(response, pagesize=A4)
    width, height = A4
    y = height - 50

    pdf.setFont("Helvetica-Bold", 16)
    pdf.drawString(50, y, "Factory ERP - Inventory Report")
    y -= 40

    materials = Material.objects.all()

    pdf.setFont("Helvetica", 12)
    pdf.drawString(50, y, f"Total Materials: {materials.count()}")
    y -= 20
    pdf.drawString(
        50, y,
        f"Total Quantity: {sum(m.quantity for m in materials)}"
    )
    y -= 30

    pdf.setFont("Helvetica-Bold", 14)
    pdf.drawString(50, y, "Materials List")
    y -= 20

    pdf.setFont("Helvetica", 11)

    for m in materials:
        pdf.drawString(
            50, y,
            f"{m.name} | Qty: {m.quantity} | Min: {m.min_quantity}"
        )
        y -= 15
        if y < 50:
            pdf.showPage()
            y = height - 50

    pdf.showPage()
    pdf.save()
    return response
