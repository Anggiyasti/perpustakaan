from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings

from peminjaman.models import *
from peminjaman.forms import PeminjamanForm, AnggotaForm, BukuForm

# Create your views here.
@login_required(login_url=settings.LOGIN_URL)
def profil(request):
    petugas = Petugas.objects.get(id=request.session['petugas_id'])
    # select * from petugas where id = '1'
    # return render(request,'profil.html', {"petugas":petugas})
    return render(request,'new/profil.html', {"petugas":petugas})

@login_required(login_url=settings.LOGIN_URL)
def daftar_peminjaman(request):
    daftar_peminjaman = None

    if request.method == 'POST':
        bulan = request.POST['bulan']
        tahun = request.POST['tahun']
        daftar_peminjaman = Peminjaman.objects.filter(tgl_pinjam__year=tahun, tgl_pinjam__month=bulan)

    # return render(request, 'daftar_peminjaman.html', {'daftar_peminjaman':daftar_peminjaman})
    return render(request, 'new/daftar_peminjaman.html', {'daftar_peminjaman':daftar_peminjaman})

@login_required(login_url=settings.LOGIN_URL)
def daftar_anggota(request):
    daftar_anggota = Anggota.objects.all()

    # return render(request, 'daftar_peminjaman.html', {'daftar_peminjaman':daftar_peminjaman})
    return render(request, 'new/daftar_anggota.html', {'daftar_anggota':daftar_anggota})

@login_required(login_url=settings.LOGIN_URL)
def daftar_buku(request):
    daftar_buku = Buku.objects.all()

    return render(request, 'new/daftar_buku.html', {'daftar_buku':daftar_buku})

@login_required(login_url=settings.LOGIN_URL)
def tambah_anggota(request):
    if request.method == 'POST':
        form_data = request.POST
        form = AnggotaForm(form_data)
        if form.is_valid():
            anggota = Anggota(
                nrp = request.POST['nrp'],
                nama = request.POST['nama'],
                alamat = request.POST['alamat'],
                no_telp = request.POST['no_telp'],
            )

            anggota.save()
            return redirect('/daftar_anggota/')
    else:
        form = AnggotaForm()

    # return render(request, 'tambah_peminjaman.html', {'form':form})
    return render(request, 'new/tambah_anggota.html', {'form':form})

@login_required(login_url=settings.LOGIN_URL)
def tambah_buku(request):
    if request.method == 'POST':
        fom_data = request.POST
        form = BukuForm(fom_data)
        if form.is_valid():
            buku = Buku(
                no_buku = request.POST['no_buku'],
                judul_buku = request.POST['judul_buku'],
                pengarang = request.POST['pengarang'],
                jenis_buku = request.POST['jenis_buku'],
            )
        buku.save()
        return redirect('/daftar_buku/')
    else:
        form = BukuForm()

    return render(request, 'new/tambah_buku.html', {'form':form})

@login_required(login_url=settings.LOGIN_URL)
def tambah_peminjaman(request):
    if request.method == 'POST':
        form_data = request.POST
        try:
            anggota = Anggota.objects.get(id=request.POST.get('nrp'))
        except Anggota.DoesNotExist:
            anggota = None
        try:
            buku = Buku.objects.get(id=request.POST.get('no_buku'))
        except Buku.DoesNotExist:
            buku = None

        form = PeminjamanForm(form_data)
        if form.is_valid():
            peminjaman = Peminjaman(
                nrp = anggota,
                no_buku = buku,
                tgl_pinjam = request.POST['tgl_pinjam'],
                tgl_kembali = request.POST['tgl_kembali'],
            )

            peminjaman.save()
            return redirect('/daftar_peminjaman/')
    else:
        form = PeminjamanForm()

    return render(request, 'new/tambah_peminjaman.html', {'form':form})
    # return render(request, 'tambah_peminjaman.html', {'form':form})


@login_required(login_url=settings.LOGIN_URL)
def tambah_coba(request):
    if request.method == 'POST':
            anggota = Anggota(
                nrp = request.POST['nrp'],
                nama = request.POST['nama'],
                alamat = request.POST['alamat'],
                no_telp = request.POST['no_telp'],
            )

            anggota.save()
            return redirect('/daftar_anggota/')

    # return render(request, 'tambah_peminjaman.html', {'form':form})
    return render(request, 'new/coba.html')

@login_required(login_url=settings.LOGIN_URL)
def ganti_foto(request):
    p = Petugas.objects.get(id=request.session['petugas_id'])
    p.foto = request.FILES['files']
    p.save()

    return redirect('/')
