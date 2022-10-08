
from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render

from .models import Contents

# Create your views here.


def home_view(request, *args, **kwargs):
    # return HttpResponse("<h1>good job</h1>")
    return render(request, "pages/home.html",context={}, status=200)


def tweet_list_view(request, *args, **kwargs):
    
    qs = Contents.objects.all()

    tweets_list = [ {"id":x.id,"content":x.content} for x in qs]
    
    data = {
        "response":tweets_list
    }

    return JsonResponse(data,status=200)


def tweet_detail_view(request, tweet_id, *args, **kwargs):
    data ={
        "id": tweet_id,
    }
    status = 200
    try:
        obj = Contents.objects.get(id=tweet_id)
        data['content'] = obj.content
        
    except Exception as err:
        # return HttpResponse(f"Tweet id : {tweet_id} not found.")
        # raise Http404

        status = 404
        data['message'] = 'Tweet not Fount'

    

    return JsonResponse(data, status=status)
