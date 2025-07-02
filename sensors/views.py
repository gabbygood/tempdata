from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import SensorData
from .serializers import SensorDataSerializer  # You'll create this next

@api_view(['GET', 'POST'])
def receive_data(request):
    if request.method == 'POST':
        temp = request.data.get('temperature')
        hum = request.data.get('humidity')

        if temp is not None and hum is not None:
            SensorData.objects.create(temperature=temp, humidity=hum)
            return Response({"status": "Data saved"}, status=201)
        return Response({"error": "Invalid data"}, status=400)

    if request.method == 'GET':
        data = SensorData.objects.order_by('-timestamp')[:50]  # latest 50 records
        serializer = SensorDataSerializer(data, many=True)
        return Response(serializer.data)
