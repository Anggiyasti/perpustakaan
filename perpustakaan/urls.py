"""perpustakaan URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from home import views as home_views
from peminjaman import views as peminjaman_views

urlpatterns = [
    url(r'^adminperpus/', admin.site.urls),
    url(r'^$', peminjaman_views.profil),
    url(r'^login/', home_views.login_view),
    url(r'^logout/', home_views.logout_view),
    url(r'^daftar_peminjaman/', peminjaman_views.daftar_peminjaman),
    url(r'^tambah_peminjaman/', peminjaman_views.tambah_peminjaman),
    url(r'^tambah_anggota/', peminjaman_views.tambah_anggota),
    url(r'^daftar_anggota/', peminjaman_views.daftar_anggota, name='daftar_anggota'),
    url(r'^tambah_buku/', peminjaman_views.tambah_buku),
    url(r'^daftar_buku/', peminjaman_views.daftar_buku),
    url(r'^tambah_coba/', peminjaman_views.tambah_coba),
    url(r'^ganti_foto/', peminjaman_views.ganti_foto),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
