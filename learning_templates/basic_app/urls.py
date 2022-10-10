from django.urls import path
from . import views #similar to from basic_app import views

# SET THE NAMESPACE, fot template tagging
app_name = 'basic_app'

urlpatterns=[
    path('relative/',views.relative,name='relative'),
    path('other/',views.other,name='other'),
]
