from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import VisitaPOISerializer

@api_view(['POST'])
def registrar_visita(request):
    serializer = VisitaPOISerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"estado": "ok", "mensaje": "Visita registrada"})
    return Response(serializer.errors, status=400)
