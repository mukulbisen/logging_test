from django.urls import path
from app1.views import Info, Debug, Error, UserBasedLogging

urlpatterns = [
    path('info', Info.as_view(), name='info'),
    path('error', Error.as_view(), name='error'),
    path('debug', Debug.as_view(), name='debug'),
    path('user_based_logging', UserBasedLogging.as_view(), name='user_based_logging'),
]
