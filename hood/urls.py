
from django.conf.urls import url,include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^accounts/',include('registration.backends.simple.urls')),
    # url(r'^logout/$',views.logout, {"next_page":'/'},name="logout"),
    # url(r'^tinymce',include('tinymce.urls')),
]
