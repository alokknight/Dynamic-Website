from django.shortcuts import render, HttpResponse
from datetime import datetime
from app1.models import Contact, Tutorial
from django.contrib import messages

# Create your views here.


def index(request):
    tur1=Tutorial()
    tur1.name="python"
    tur1.img='sunsetgirl.jpg'
    tur1.desc="bam bam bhole!!"
    tur1.price=7859
    tur1.offer=True

    tur2=Tutorial()
    tur2.name="machine learning"
    tur2.img='kedarnath.jpg'
    tur2.desc="jai mata di!!"
    tur2.price=8000
    tur2.offer=False

    tur3=Tutorial()
    tur3.name="Artificial Intelligence"
    tur3.img="charbagh.jpg"
    tur3.desc="charbagh station:: most busy station."
    tur3.price=9000
    tur3.offer=True

    tur4=Tutorial()
    tur4.name="C"
    tur4.img='charbagh2.jpg'
    tur4.desc="charbagh"
    tur4.price=24564
    tur4.offer=False

    tur6=Tutorial()
    tur6.name="C++"
    tur6.img='lko9.jpg'
    tur6.desc="jai mata di!!"
    tur6.price=8000
    tur6.offer=False

    tur7=Tutorial()
    tur7.name="JAVA"
    tur7.img='waterfall.jpg'
    tur7.desc="the place of iit bombay"
    tur7.price=9000
    tur7.offer=False

    tur8=Tutorial()
    tur8.name="vector"
    tur8.img='ML1.gif'
    tur8.desc="i am vector2"
    tur8.price=24564
    tur8.offer=False

    tur9=Tutorial()
    tur9.name="sky"
    tur9.img="lko8.jpg"
    tur9.desc="sky never cry!! I'm telling a lie."
    tur9.price=2456
    tur9.offer=True

    turs=[tur1,tur2,tur3,tur4,tur6,tur7,tur8,tur9]
    return render(request,'index.html', {'turs':turs} )

def tutindex(request):
    tuts=Tutorial.objects.all()
    return render(request,'tutindex.html', {'tuts':tuts} )

def about(request):
    context = {
        'variable1': "i am c_variable1",
        "variable2": "i am c_second variable2"
    }
    return render(request, 'about.html',context)

def services(request):
    return render(request, 'turistingo.html')

def contact(request):
    if  request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get("phone")
        desc=request.POST.get('desc')
        contact=Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request, "your message have been sent...!!")
    return render(request, 'contact.html')
    #return HttpResponse("this is contact page")

def projects(request):
    return render(request,'projects.html')


def blogs(request):
    return render(request,'blogs.html')


# from web1.utils import get_db_handle, get_collection_handle
# db_handle, mongo_client = get_db_handle(DATABASE_NAME, DATABASE_HOST, DATABASE_PORT, USERNAME, PASSWORD)
# collection_handle = get_collection_handle(db_handle, REGIONS_COLLECTION)
# collection_handle.find({...})
# collection_handle.insert({...})
# collection_handle.update({...})

#by using pymongo

'''
from pymongo import MongoClient
def get_db_handle(db_name, host, port, username, password):
    client = MongoClient(host=host,
                         port=int(port),
                         username=username,
                         password=password
                        )
    db_handle = client[db_name]
    return db_handle, client


def get_collection_handle(db_handle, collection_name):
    return db_handle[collection_name]




from project.utils import get_db_handle, get_collection_handle
db_handle, mongo_client = get_db_handle(DATABASE_NAME, DATABASE_HOST, DATABASE_PORT, USERNAME, PASSWORD)
collection_handle = get_collection_handle(db_handle, REGIONS_COLLECTION)
collection_hadle.find({...})
collection_handle.insert({...})
collection_handle.update({...})

'''

