from django.shortcuts import render

# Create your views here.
import logging
import random
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import JsonResponse

logger = logging.getLogger(__name__)


class Debug(APIView):

    def get(self, request):
        logger.debug("This is debug message", extra={'extraParam': 'mux'})

        return Response(data={'debug', 'hello'})


class Error(APIView):

    def get(self, request):
        logger.error("This is error message")

        return Response(data={'error', 'hello'})


class Info(APIView):

    def get(self, request):
        logger.info("This is info message")

        return Response(data={'info', 'hello'})


class UserBasedLogging(APIView):
    def get(self, request):
        numberOfLogsToGenerate = 10
        userId = []
        for i in range(0, numberOfLogsToGenerate):
            number = random.randint(1111,9999)
            logger.info("User:" + str(number))
            userId.append(number)
        return JsonResponse(userId, safe=False)
