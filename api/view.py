from rest_framework.decorators import api_view
from rest_framework import permissions
from django.http import HttpResponse


@api_view(['GET'])
def image_view(request, file_name):
    image_data = open('media/uploads/items_image/' + file_name, 'rb').read()
    ext = file_name.split('.')[1]
    return HttpResponse(image_data, content_type='image/' + ext)