from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponsePermanentRedirect
from .models import Link
from .serializers import LinkSerializer
from django.utils import timezone

class LinkViewSet(viewsets.ModelViewSet):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer
    lookup_field = 'short_code'
    http_method_names = ['get', 'post']

    @action(detail=True, methods=['get'])
    def redirect_link(self, request):
        link = self.get_object()

        return Response({'original_url': link.orig_url}, status=200)
    
def short_code_redirect(request, short_code):
    link = get_object_or_404(Link, short_code=short_code)
    link.clicks += 1
    link.last_clicked = timezone.now()
    link.save()
    return HttpResponsePermanentRedirect(link.orig_url)