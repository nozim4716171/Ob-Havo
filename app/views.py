from django.shortcuts import render
from weather.ob_havo import Obhavo


def HomeView(request):
    if request.method == 'POST':
        user_word = request.POST.get('word')

        try:
            data = Obhavo(city=user_word).main()
            city = data['city']
            day = data['day']
            info = data['info']
            description = data['description']
            degree = data['degree']

            natija = (
                f"Siz so'ragan ob-havo {city} bo'ylab!\n"
                f"Kun: {day}\n"
                f"Holat: {info}\n"
                f"{description}\n"
                f"Temperatura: {degree}"
            )
        except KeyError:
            natija = "Ma'lumotlarni olishda xatolik yuz berdi. Iltimos, boshqa shahar nomini kiriting."

        return render(request, 'index.html', {'natija': natija})

    return render(request, 'index.html')
