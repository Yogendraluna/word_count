from django.urls import path
from count_app.views import user_interface, count_word

urlpatterns = [
    path('', user_interface, name='user_interface'),
    path('count/', count_word, name='count_word'),
]
