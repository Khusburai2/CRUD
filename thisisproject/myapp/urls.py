# myapp/urls.py
from django.conf.urls.static import static
from django.urls import path
from django.conf import settings
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('blog/', views.Blogs, name="Blog"),
    path('blog/update_blog/<int:blog_id>', views.update_blog, name="update_blog"),
    path('blog/create_blog/',views.create_blog, name = 'create_blog'),
    path('blog/delete_blog/<int:blog_id>',views.delete_blog, name = 'delete_blog'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.CustomLoginView.as_view(), name='login'),

]   
if  settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    
