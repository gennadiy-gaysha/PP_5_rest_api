from rest_framework.decorators import api_view
from rest_framework.response import Response

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

