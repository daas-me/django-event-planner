from django.shortcuts import render, redirect, get_object_or_404
from .models import Event
from .forms import EventForm

def event_list(request):
    events = Event.objects.all()
    return render(request, "events/event_list.html", {"events": events})

def event_create(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("event_list")
    else:
        form = EventForm()
    return render(request, "events/event_form.html", {"form": form})

def event_delete(request, pk):
    event = get_object_or_404(Event, pk=pk)
    event.delete()
    return redirect('event_list')
