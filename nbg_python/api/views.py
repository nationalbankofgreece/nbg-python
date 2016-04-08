import os
import sys

from rest_framework import viewsets
from rest_framework.response import Response

from api import serializers


sys.path.append(
    os.path.join(os.getcwd(), os.pardir)
)


import nbg


class ResourceViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ResourceSerializer
    queryset = None

    def list(self, response):
        return Response([])

    def retrieve(self, response):
        return Response([])

    def retrieve_cached(self, response):
        return Response([])

    def head(self, response):
        return Response([])

    def create(self, response):
        return Response([])

    def modify(self, response):
        return Response([])

    def remove(self, response):
        return Response([])
