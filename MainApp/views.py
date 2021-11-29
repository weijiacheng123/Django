from django.shortcuts import render

from .models import Topic

# Create your views here.
def index(request):
    # get post may on interview
    return render(request, 'MainApp/index.html')

def topics(request):
    topics = Topic.objects.order_by('date_added')

    context = {'topics':topics}

    return render(request, 'MainApp/topics.html', context)

def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)

    entries = topic.entry_set.all()

    context = {'topic':topic, 'entries':entries}

    return render(request, 'MainApp/topic.html', context)