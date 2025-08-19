from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .serializers import VisitaPOISerializer

@api_view(['GET'])
@permission_classes([AllowAny])
@authentication_classes([])
def health(request):
    return Response({"status": "ok"})

@api_view(['POST'])
@permission_classes([AllowAny])
@authentication_classes([])
def registrar_visita(request):
    serializer = VisitaPOISerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"estado": "ok", "mensaje": "Visita registrada"}, status=201)  # <-- 201
    return Response(serializer.errors, status=400)
