from django.urls import path
from django.http import HttpResponse, HttpRequest

from strawberry.django.views import AsyncGraphQLView
from asgiref.sync import sync_to_async

from .schema import schema


async def view(request: HttpRequest) -> HttpResponse:
    await sync_to_async(lambda: None, thread_sensitive=True)()
    await sync_to_async(lambda: None, thread_sensitive=False)()

    return HttpResponse('ok')


urlpatterns = [
    path("", AsyncGraphQLView.as_view(schema=schema)),
    path("view", view),
]
