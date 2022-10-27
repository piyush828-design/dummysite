from . import views
from django.urls import path

urlpatterns = [
    path('postComment',views.postComment,name='postComment'),
    path('',views.blogHome,name='blogHome'),
    path('<str:slug>',views.blogPost,name='blogPost')
    #ai to post a comment
   
]

