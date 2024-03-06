from django.db import IntegrityError
from django.utils.cache import patch_vary_headers
from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Link
from .serializers import LinkSerializer


class LinkViewSet(viewsets.ModelViewSet):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        last_err = None
        for _retry in range(5): # to handle possible duplicate shortcuts
            try:
                instance, created = Link.objects.get_or_create(
                    target = serializer.validated_data['target'],
                    defaults = dict(
                        shortcut = Link.make_random_shortcut(),
                    )
                )
                break
            except IntegrityError as e:
                last_err = e
        else:
            raise last_err

        serializer = self.get_serializer(instance=instance)
        return Response(serializer.data, status=status.HTTP_201_CREATED if created else status.HTTP_200_OK)

    def finalize_response(self, request, response, *args, **kwargs):
        res = super().finalize_response(request, response, *args, **kwargs)
        patch_vary_headers(res, ('Origin',))
        res['Access-Control-Allow-Origin'] = request.headers.get('Origin', '*')
        res['Access-Control-Allow-Headers'] = 'content-type'
        res['Access-Control-Allow-Methods'] = 'POST'
        return res
