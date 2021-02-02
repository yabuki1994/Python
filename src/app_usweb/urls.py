from django.urls import path
from app_usweb import views
from .views import login
from app_usweb.views import menuView
from .views.employee import usercreate
from .views.employee import userserch
from .views.employee import EmployeeInfoRegistView

app_name = 'app_usweb'

urlpatterns = [
    # ログイン画面
    path('login/', login.Login.as_view(), name='login'),
    # ログアウト画面
    path('logout/', login.Logout.as_view(), name='logout'),
    # menu画面
    path('menu/', menuView.MenuView.as_view(), name='menu'),
    # 社員マスタ登録
    path('employee_info_regist/', EmployeeInfoRegistView.EmployeeInfoRegistView.as_view(), name='employee_info_regist'),
    # ユーザ登録
    path('user_create/', usercreate.UserCreate.as_view(), name='user_create'),
    # ユーザ登録完了
    path('user_create/complete/', usercreate.UserCreateComplete.as_view(), name='user_create_complete'),
    # ユーザ検索
    path('reference', userserch.Reference.as_view(), name='reference'),
]