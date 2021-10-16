from django.conf.urls import url 
from demoapp import views 
 
urlpatterns = [ 
    url(r'^api/demoapp$',views.demoapp_list),
    url(r'^api/demoapp/(?P<pk>[0-9]+)$',views.demoapp_detail)
]