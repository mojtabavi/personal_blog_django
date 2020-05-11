from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.

#first page of site
def home(request):
    context = {
        "articles" : [
            {
                "title" : "شرط جالب PSG برای موافقت با انتقال نیمار به بارسا",
                "description" : "بر اساس ادعای کالچو مرکاتو پاری سن ژرمن برای فروش نیمار به بارسلونا از این باشگاه درخواست دو بازیکن کرده است.",
                "img" : "https://static.farakav.com/files/pictures/thumb/01493144.jpg"
            },
            {
                "title" : "راه حل جدید بارسلونا و اینتر در مورد انتقال لائوتارو ",
                "description" : "بارسلونا و اینتر به راه حل جدیدی برای انتقال لائوتارو مارتینز به نوکمپ رسیده اند. ",
                "img" : "https://static.farakav.com/files/pictures/thumb/01478564.jpg"

            },
            {
                "title" : "بارسلونا، رقیب میلان در راه جذب مهاجم هلندی",
                "description" : "ه نظر می رسد که بارسلونا نیز به خرید ممفیس دیپای از لیون علاقه نشان داده است.",
                "img" : "https://static.farakav.com/files/pictures/thumb/01451478.jpg"

            },

        ]
    }
    return render(request, 'blog/home.html',context)

