from django.shortcuts import render
from datetime import datetime

# Create your views here.
def home(request):
    return render(request, 'shop/home.html', {'current_date': str(datetime.now())})

def item(request):
    return render(request, 'shop/item.html',{"name":"Item Page"})

def qg_sw_script(request):
    return render(request, 'shop/qg-sw.b50fd7673dfea26eca60.js', content_type='text/javascript')

from django.http import FileResponse

def custom_serve(request, path):
    response = FileResponse(open(path, 'rb'))
    response['Content-Type'] = 'text/javascript'
    return response

#TODO 
#qg-sw.b50fd7673dfea26eca60.js Content-Type is text/html and should be text/javascript. qg-sw.b50fd7673dfea26eca60.js file content is not correct.