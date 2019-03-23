
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^jet/', include('jet.urls', 'jet')),  
    # url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')), 
    url(r'^accounts/',include('registration.backends.simple.urls')),
    url(r'^logout/$',views.logout, {"next_page":'/'},name="logout"),
    url(r'^tinymce',include('tinymce.urls')),
]
