from django.shortcuts import render, redirect
from django.contrib.auth.decorators import  login_required
from django.http import Http404

from .models import Topic, Note
from .forms import TopicForm, NoteForm

# Create your views here.

def index(request):
    # Головна сторінка-привітання
    return render(request,'online_notes/index.html')

@login_required
def topics (request):
    # Відображення усіх тем, створених користувачем
    # Показуються лише теми, де власник - цей користувач
    topics=Topic.objects.filter(owner=request.user).order_by('date_added')
    context={'topics':topics}
    return render(request,'online_notes/topics.html', context)

@login_required
def topic(request,topic_id):
    # Відображення однієї теми та усіх нотаток у ній
    topic=Topic.objects.get(id=topic_id)
    # Перевірка, чи користувач є власником цієї теми
    if topic.owner != request.user:
        raise Http404
    notes=topic.note_set.order_by('-date_added')
    context={'topic':topic,'notes':notes}
    return render(request,'online_notes/topic.html', context)

@login_required
def new_topic(request):
    # Створення нової теми
    # Перевірка на тип запиту
    if request.method != 'POST':
        form=TopicForm()
    else:
        form=TopicForm(data=request.POST)
        if form.is_valid():
            new_topic=form.save(commit=False)
            new_topic.owner=request.user
            form.save()
            return redirect('online_notes:topics')

    context={'form':form}
    return render(request,'online_notes/new_topic.html',context)

@login_required
def new_note(request,topic_id):
    # Створення нової нотатки в існуючій темі
    topic=Topic.objects.get(id=topic_id)
    # Перевірка на тип запиту
    if request.method !='POST':
        form=NoteForm()
    else:
        form = NoteForm(data=request.POST)
        if form.is_valid():
            new_note=form.save(commit=False)
            new_note.topic=topic
            new_note.save()
            return redirect('online_notes:topic',topic_id=topic_id)

    context={'topic':topic,'form':form}
    return render(request,'online_notes/new_note.html',context)


@login_required
def edit_note(request,note_id):
    # Редагування існуючої нотатки
    note=Note.objects.get(id=note_id)
    topic=note.topic
    # Перевірка, чи користувач є власником цієї теми
    if topic.owner != request.user:
        raise Http404
    # Перевірка на тип запиту
    if request.method != 'POST':
        # Якщо запит не POST, вставити в форму текст нередагованої нотатки
        form=NoteForm(instance=note)
    else:
        # Якщо запит POST, опрацювати дані
        form= NoteForm(instance=note,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('online_notes:topic', topic_id=topic.id)

    context={'note':note,'topic':topic, 'form':form}
    return render(request,'online_notes/edit_note.html',context)