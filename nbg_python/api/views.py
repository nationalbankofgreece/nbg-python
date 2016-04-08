import os
import sys

from django.shortcuts import render
from rest_framework import status
from rest_framework import views
from rest_framework.response import Response

sys.path.append(
    os.path.join(os.getcwd(), os.pardir)
)


import nbg


class ProxyView(views.APIView):
    def post(self, request, *args, **kwargs):
        return Response(
            nbg.create_resource(data=request.data).text.strip(u'\u0000'),
            status=status.HTTP_201_CREATED)

    def put(self, request, *args, **kwargs):
        return Response(
            nbg.modify_resource(data=request.data).text.strip(u'\u0000'))

    def get(self, request, *args, **kwargs):
        if 'cached' in request.GET:
            query = request.GET.copy()
            query.pop('cached')
            return Response(
                nbg.retrieve_resource_cached(data=query).text.strip(u'\u0000'))
        return Response(
            nbg.retrieve_resource(data=request.GET).text.strip(u'\u0000'))

    def head(self, request, *args, **kwargs):
        return Response({}, headers=nbg.retrieve_resource_headers(data={}))

    def delete(self, request, *args, **kwargs):
        return Response(nbg.remove_resource(data={}).text.strip(u'\u0000'),
                        status=status.HTTP_204_NO_CONTENT)


def ui_view(request):
    return render(request, 'api/index.html')
