from django.shortcuts import render, redirect
from .forms import NoteForm
from .models import Note
# Create your views here.


def note_list(request):
    context = {'note_list': Note.objects.all()}
    return render(request, 'noter_app/note_list.html', context)


def note_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = NoteForm()
        else:
            note = Note.objects.get(pk=id)
            form = NoteForm(instance=note)
        return render(request, 'noter_app/note_form.html', {'form': form})
    else:
        if id == 0:
            form = NoteForm(request.POST)
        else:
            note = Note.objects.get(pk=id)
            form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
        return redirect('/list/')


def note_delete(request, id):
    note = Note.objects.get(pk=id)
    note.delete()
    return redirect('/list/')
