from django.urls import path
from app_usweb import views

app_name = 'app_usweb'

urlpatterns = [
    # ログイン画面
    path('login/', views.Login.as_view(), name='login'),
    # ログアウト画面
    path('logout/', views.Logout.as_view(), name='logout'),
    # menu画面
    path('menu/', views.Menu.as_view(), name='menu'),
    # ユーザ登録
    path('user_create/', views.UserCreate.as_view(), name='user_create'),
    # ユーザ登録完了
    path('user_create/complete/', views.UserCreateComplete.as_view(), name='user_create_complete'),
    # ユーザ検索
    path('reference', views.Reference.as_view(), name='reference'),
]