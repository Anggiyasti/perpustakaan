from django.contrib import admin
from peminjaman.models import *

# Register your models here.
class AnggotaAdmin (admin.ModelAdmin):
    list_display = ['nrp','nama', 'alamat', 'no_telp']
    list_filter = ()
    search_fields = ['nrp', 'nama']
    list_per_page = 25

admin.site.register(Anggota, AnggotaAdmin)

class BukuAdmin (admin.ModelAdmin):
    list_display = ['no_buku','judul_buku', 'pengarang', 'jenis_buku']
    list_filter = ['jenis_buku']
    search_fields = ['no_buku', 'judul_buku']
    list_per_page = 25

admin.site.register(Buku, BukuAdmin)

class PeminjamanAdmin (admin.ModelAdmin):
    list_display = ['nrp','no_buku', 'tgl_pinjam', 'tgl_kembali']
    list_filter = ['tgl_pinjam']
    search_fields = ['nrp', 'no_buku']
    list_per_page = 25

admin.site.register(Peminjaman, PeminjamanAdmin)

class PetugasAdmin (admin.ModelAdmin):
    list_display = ['nama','jabatan', 'foto']
    list_filter = ['jabatan']
    search_fields = ['nama', 'jabatan']
    list_per_page = 25

admin.site.register(Petugas, PetugasAdmin)

class AkunAdmin (admin.ModelAdmin):
    list_display = ['akun','petugas', 'jenis_akun']
    list_filter = ['jenis_akun']
    search_fields = []
    list_per_page = 25

admin.site.register(Akun, AkunAdmin)