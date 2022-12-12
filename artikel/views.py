from django.shortcuts import render

from artikel.models import Cards
from django.http import JsonResponse
# Create your views here.
# disuruh ferry
def anxiety(request):
    context = {
        'user' : request.user,
        'title': 'Anxiety Disorder',
        'subtitle': 'gangguan mental dengan rasa cemas berlebih',
        'deskripsi': "Anxiety disorder adalah gangguan mental yang menyebabkan rasa cemas dan takut berlebih. Hal tersebut membuat Anda menjadi tidak semangat untuk melakukan kegiatan sehari-hari, termasuk hobi yang biasa digemari. Lebih lanjut, rasa cemas ini akan berlangsung intens dalam jangka waktu yang panjang. Seringkali dengan ketakutan ini membuat penderitanya cepat lemas secara fisik. WHO menyatakan jika terdapat 301 juta orang memiliki gangguan mental ini di dunia, dimana 58 juta penderita anxiety disorder adalah anak-anak dan remaja. Menurut data Kementerian Kesehatan RI, gangguan kecemasan berada di peringkat 2 dari 10 penyakit yang paling banyak diderita oleh masyarakat Indonesia dari tahun 1990-an sampai 2017.",
        "subpencegah":"Kecemasan yang Anda miliki dapat mengganggu keseharian jika tidak dicegah dengan pola hidup yang sehat. Maka dari itu, cara ini bisa dilakukan untuk menjaga mental Anda agar aman dari rasa cemas.",
        "tips": ["Tidur cukup.", "Aktif berolahraga.", "Melakukan meditasi untuk melatih pernapasan dan mengendalikan emosi.", "Mengatur pola makan sehat.", "Menghindari rokok dan alkohol.", "Membatasi jumlah konsumsi kafein, seperti kopi dan teh."]
    }

    return render(request, 'artikel.html',context)

#def ferry(request):
#     context = {
#         'user' : request.user,
#         'title': 'Anxiety Disorder',
#         'subtitle': 'gangguan mental dengan rasa cemas berlebih',
#         'deskripsi': "asd"
#     }
#     return render(request, 'artikel.html', context)

def addcard(request):
    if request.method == "POST":
        description = request.POST.get("description")
        task = Cards.objects.create(
            # user=request.user,
            desc=description,
        )
        return JsonResponse(
            {
                "pk": task.id,
                "fields": {
                    "description": task.description,
                },
            },
        )