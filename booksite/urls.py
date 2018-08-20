from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect


def home_page_redirect(request):
    return redirect('books/')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page_redirect),
    path('books/', include('books.urls')),
    path('about/', include('about.urls')),
    path('services/', include('services.urls')),
    path('contact/', include('contact.urls')),
    path('book-1/', include('book_1.urls')),
    path('book-2/', include('book_2.urls')),
    path('book-3/', include('book_3.urls')),
    path('book-4/', include('book_4.urls')),
    path('book-single/', include('book_single.urls')),
    path('blog/', include('blog.urls')),
    path('news/', include('news.urls')),
    path('blog-post/', include('blog_post.urls')),
    path('accounts/', include('accounts.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
