from django.urls import path
from app_usweb import views
from .views import login
from .views import menu
from .views.employee import usercreate
from .views.employee import userserch

app_name = 'app_usweb'

urlpatterns = [
    # ログイン画面
    path('login/', login.Login.as_view(), name='login'),
    # ログアウト画面
    path('logout/', login.Logout.as_view(), name='logout'),
    # menu画面
    path('menu/', menu.Menu.as_view(), name='menu'),
    # ユーザ登録
    path('user_create/', usercreate.UserCreate.as_view(), name='user_create'),
    # ユーザ登録完了
    path('user_create/complete/', usercreate.UserCreateComplete.as_view(), name='user_create_complete'),
    # ユーザ検索
    path('reference', userserch.Reference.as_view(), name='reference'),
]