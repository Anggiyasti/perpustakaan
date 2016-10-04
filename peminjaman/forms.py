from django.forms import ModelForm
from django import forms
from peminjaman.models import Peminjaman, Anggota, Buku

class AnggotaForm(ModelForm):
    # class meta untuk mendefinisikan ModelForm
    class Meta:
        model = Anggota
        fields = ['nrp', 'nama', 'alamat', 'no_telp','foto']
        # labels = {
        #     'nrp' : "NRP",
        #     'nama' : "Nama",
        #     'alamat' : "Alamat",
        #     'no_telp' : "No Telpon",
        #     'foto' : "Foto"
        # }
        widgets = {
            'alamat': forms.Textarea(attrs={ 'cols':50, 'rows': 10 }),
        }

    def __init__(self, data=None, *args, **kwargs):
        super(AnggotaForm, self).__init__(data, *args, **kwargs)
        # jenis_kelamin = forms.CharField(widget=forms.RadioSelect(
        #     attrs={
        #         'laki-laki':'Laki-laki',
        #         'perempuan':'Perempuan'
        #     }
        # ))

class BukuForm(ModelForm):
    # class meta untuk mendefinisikan ModelForm
    class Meta:
        model = Buku
        fields = ['no_buku', 'judul_buku', 'pengarang', 'jenis_buku']
        labels = {
            'no_buku' : "No Buku",
            'judul_buku' : "Judul Buku",
            'pengarang' : "Pengarang",
            'jenis_buku' : "Jenis Buku",
        }
        error_messages = {
            'no_buku' : {
                'required' : 'No Buku harus diisi'
            },
            'judul_buku' : {
                'required' : 'Judul Buku harus diisi'
            },
            'pengarang' : {
                'required' : 'Pengarang harus diisi'
            },
            'jenis_buku' : {
                'required' : 'Jenis Buku harus diisi'
            }
        }

class PeminjamanForm(ModelForm):
    # class meta untuk mendefinisikan ModelForm
    class Meta:
        model = Peminjaman
        fields = ['nrp', 'no_buku', 'tgl_pinjam', 'tgl_kembali']
        labels = {
            'nrp' : "NRP",
            'no_buku' : "No Buku",
            'tgl_pinjam' : "Tanggal Peminjaman",
            'tgl_kembali' : "Tanggal Pengembalian",
        }
        error_messages = {
            'nrp' : {
                'required' : 'NRP harus diisi'
            },
            'no_buku' : {
                'required' : 'No Buku harus diisi'
            },
            'tgl_pinjam' : {
                'required' : 'Tanggal Peminjaman harus diisi'
            },
            'tgl_kembali' : {
                'required' : 'Tanggal Pengembalian harus diisi'
            }
        }