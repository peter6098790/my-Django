from django.shortcuts import render
from .clawer import EPA
# Create your views here.

def index(request):
    epa = EPA()
    #epa = EPA(request.POST.get("city_name"))

    context = {
        "results": epa.scrape()
    }
    return render(request, "webClawer/index.html",context)

