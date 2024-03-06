from django.shortcuts import redirect
from django.http import Http404

from .models import Link


async def go(request, shortcut):
    try:
        link = await Link.objects.aget(shortcut=shortcut)
    except Link.DoesNotExist:
        raise Http404("Link does not exist")
    return redirect(link.target)
