from django.urls import path
from .views import GetView, PostDataView1, PostDataView2, PostDataView4, SectionGetView

urlpatterns=[
    path('post/guide/', PostDataView1.as_view()),
    path('post/page/', PostDataView2.as_view()),
    path('post/section/', PostDataView4.as_view()),
    path('get/guidename/', GetView.as_view()),
    path('get/sections/', SectionGetView.as_view())
]


