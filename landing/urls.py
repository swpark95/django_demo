from django.urls import path
from . import views

app_name='landing'
urlpatterns = [
    path('', views.index, name='home'),
    path('<int:month>/', views.months),
    #int:(month<-이걸 keyword arguments라고 한다. 이걸 먼저 지정해준다. 이걸 views.py의 month 함수에도 쓸텐데 거기서의 Parrmeter에도 똑같이 써야 한다.)
    path('<str:name>/', views.detail),
]