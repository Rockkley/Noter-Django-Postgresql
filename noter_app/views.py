from django.shortcuts import render, redirect
from .forms import NoteForm
from .models import Note
from django.core.paginator import Paginator
# Create your views here.
import tgbot
import asyncio

def note_list(request):

    paginator = Paginator(Note.objects.all(), 6)
    page = request.GET.get('page')
    notes = paginator.get_page(page)
    nums = "x" * notes.paginator.num_pages
    count = Note.objects.all().count()
    context = {'note_list': Note.objects.all(), 'notes': notes, "nums":nums, "count":count}
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
            note = Note.objects.all()
            asyncio.run(tgbot.send(
                f'Note written - {str(list(note)[-1].id)} : {str(list(note)[-1].title)}'
                f'\nCategory: {str(list(note)[-1].category)}'))


        return redirect('/list/')


def note_delete(request, id):
    note = Note.objects.get(pk=id)
    note.delete()
    asyncio.run(tgbot.send(f'Note deleted - {id} : {note.title} '))
    return redirect('/list/')


def note_open(request, id):

    note = Note.objects.get(pk=id)
    return render(request, 'noter_app/note_view.html', {'note': note})

