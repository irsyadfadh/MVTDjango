from django.shortcuts import render

def show_main(request):
    context = {
        'deskripsi': 'Berikut merupakan data pribadi mahasiswa kelas PBP semester gasal :',
        'name': 'Irsyad Fadhilah',
        'class': 'PBP B',
        'npm': '2206083363',
        'jurusan': 'Sistem Informasi',
        'angkatan': 'apollo 2022',
    }

    return render(request, "main.html", context)
# Create your views here.
