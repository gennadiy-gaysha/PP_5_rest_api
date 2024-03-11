from rest_framework.decorators import api_view
from rest_framework.response import Response
from .settings import (
    JWT_AUTH_COOKIE,
    JWT_AUTH_REFRESH_COOKIE,
    JWT_AUTH_SAMESITE,
    JWT_AUTH_SECURE
)


@api_view()
def endpoint_list(request):
    return Response([
        'http://127.0.0.1:8000/profiles/',
        'http://127.0.0.1:8000/paintings/',
        'http://127.0.0.1:8000/comments/',
        'http://127.0.0.1:8000/observations/',
        'http://127.0.0.1:8000/followers/',
        'https://pp-5-drf-api-cb9dad6bdfdf.herokuapp.com/profiles/',
        'https://pp-5-drf-api-cb9dad6bdfdf.herokuapp.com/paintings/',
        'https://pp-5-drf-api-cb9dad6bdfdf.herokuapp.com/comments/',
        'https://pp-5-drf-api-cb9dad6bdfdf.herokuapp.com/observations/',
        'https://pp-5-drf-api-cb9dad6bdfdf.herokuapp.com/followers/',
    ])


# dj-rest-auth logout view fix
@api_view(['POST'])
def logout_route(request):
    response = Response()
    response.set_cookie(
        key=JWT_AUTH_COOKIE,
        value='',
        httponly=True,
        expires='Thu, 01 Jan 1970 00:00:00 GMT',
        max_age=0,
        samesite=JWT_AUTH_SAMESITE,
        secure=JWT_AUTH_SECURE,
    )
    response.set_cookie(
        key=JWT_AUTH_REFRESH_COOKIE,
        value='',
        httponly=True,
        expires='Thu, 01 Jan 1970 00:00:00 GMT',
        max_age=0,
        samesite=JWT_AUTH_SAMESITE,
        secure=JWT_AUTH_SECURE,
    )
    return response
