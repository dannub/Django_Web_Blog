from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$',views.index,name="index"),
    url(r'^post/(?P<slugInput>[\w-]+)/$',views.detailPost,name="detail"),
    url(r'^create/$',views.create,name="create"),
    url(r'^update/(?P<update_id>[0-9])/$',views.update,name="update"), 
    url(r'^delete/(?P<delete_id>[0-9])/$',views.delete,name="delete"),
     url(r'^category/(?P<categoryInput>[\w-]+)/$',views.categoryPost,name="category"),
    
]