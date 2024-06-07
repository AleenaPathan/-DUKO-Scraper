from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from.serializers import CoinSerializer
from.models import Coin
from.tasks import start_scraping, get_scraping_status

class CoinAPIView(APIView):
    def get(self, request):
        coins = Coin.objects.all()
        serializer = CoinSerializer(coins, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CoinSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StartScrapingView(APIView):
    def post(self, request):
        start_scraping.delay()
        return Response({'message': 'Scraping started'}, status=status.HTTP_200_OK)

class GetScrapingStatusView(APIView):
    def get(self, request):
        status = get_scraping_status()
        return Response({'status': status}, status=status.HTTP_200_OK)
