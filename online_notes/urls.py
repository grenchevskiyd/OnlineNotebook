'''Defines URL patterns for online_notes'''

from django.urls import path

from . import views

app_name='online_notes'
urlpatterns=[
    # Головна сторінка-привітання
    path('',views.index,name='index'),
    # Сторінка з переліком усіх створених тем
    path('topics/', views.topics, name='topics'),
    # Сторінка створення нової теми
    path('new_topic/',views.new_topic, name='new_topic'),
    # Сторінка однієї обраної теми
    path('topics/<int:topic_id>/',views.topic,name='topic'),
    
    # Сторінка створення нової нотатки
    path('new_note/<int:topic_id>/',views.new_note,name='new_note'),
    # Сторінка редагування нотатки
    path('edit_note/<int:note_id>/',views.edit_note,name='edit_note'),
]