import imp
from django.urls import path
from .views import get_sum_of_polling_units, getPollByLGA, getPolls, get_pu_result

urlpatterns = [
    path('', get_pu_result, name='pu_result'),
    path('polls/', getPolls, name='polls'),
    path('poll_lga/<int:id>', getPollByLGA, name='poll_lga'),
    path('sum_polling_units/<int:id>', get_sum_of_polling_units, name='sum_polling_units')
]
