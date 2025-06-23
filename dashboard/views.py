from django.shortcuts import render
from visitas.models import VisitaPOI
from django.db.models import Count
from datetime import datetime

def resumen_visitas(request):
    fecha_inicio = request.GET.get('fecha_inicio')
    fecha_fin = request.GET.get('fecha_fin')

    visitas = VisitaPOI.objects.all()

    # Aplica filtro por fecha si se especifican ambas
    if fecha_inicio and fecha_fin:
        try:
            # Convierte fechas a objetos datetime
            fecha_inicio_dt = datetime.strptime(fecha_inicio, "%Y-%m-%d")
            fecha_fin_dt = datetime.strptime(fecha_fin, "%Y-%m-%d")
            # Filtra por el campo correcto (timestamp)
            visitas = visitas.filter(timestamp__range=[fecha_inicio_dt, fecha_fin_dt])
        except ValueError:
            pass  # Puedes agregar un mensaje de error si lo deseas

    # Agrupa por poi_id y cuenta visitas
    resumen = (
        visitas
        .values('poi_id')
        .annotate(total=Count('id'))
        .order_by('-total')
    )

    # Calcula total general
    total_visitas = visitas.count()

    # Prepara datos para pasar al template
    visitas_resumen = [
        {'poi': item['poi_id'], 'total': item['total']} for item in resumen
    ]

    return render(request, 'dashboard/dashboard.html', {
        'visitas': visitas_resumen,
        'total_visitas': total_visitas,
        'fecha_inicio': fecha_inicio,
        'fecha_fin': fecha_fin
    })
