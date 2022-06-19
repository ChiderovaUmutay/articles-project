from django.shortcuts import render


# Create your views here.

def index_view(request):
    query = request.GET.getlist("name", "rrrrrrrrr")
    print(query)
    context = {"name": query, "test": "lalal"}
    return render(request, "index.html", context)


def create_article(request):
    if request.method == "GET":
        return render(request, "create.html")
    else:
        user = {
            "name": "Test",
            "age": 25,
            "email": "test@mail.kg"
        }
        context = {
            "title": request.POST.get("title"),
            "author": request.POST.get("author"),
            "content": request.POST.get("content"),
            "user": user
        }
        return render(request, "article_view.html", context)
