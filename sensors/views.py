from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import SensorData

@api_view(['POST'])
def receive_data(request):
    temp = request.data.get('temperature')
    hum = request.data.get('humidity')

    if temp is not None and hum is not None:
        SensorData.objects.create(temperature=temp, humidity=hum)
        return Response({"status": "Data saved"}, status=201)
    return Response({"error": "Invalid data"}, status=400)
