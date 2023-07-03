from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    #url of home page
    path('', views.home, name='home'),
    #url of index page
    path("item/", views.item, name="item"),
    #url of qg-sw.b50fd7673dfea26eca60.js
    path("qg-sw.b50fd7673dfea26eca60.js", TemplateView.as_view(template_name="shop/qg-sw.b50fd7673dfea26eca60.js", content_type="text/javascript")),
]
