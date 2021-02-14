from django.urls import path
from .views import login,menuView
from .views.employee import usercreate,userserch
from .views.employee import EmployeeMstRegistView,EmployeeMstReferView,EmployeeMstUpdateView,EmployeeMstDeleteView

app_name = 'app_usweb'

urlpatterns = [
    # ログイン画面
    path('login/', login.Login.as_view(), name='login'),
    # ログアウト画面
    path('logout/', login.Logout.as_view(), name='logout'),
    # menu画面
    path('menu/', menuView.MenuView.as_view(), name='menu'),
    # 社員マスタ登録
    path('employee_mst_regist/', EmployeeMstRegistView.EmployeeMstRegistView.as_view(), name='employee_mst_regist'),
    # 社員マスタ検索
    path('employee_mst_refer/', EmployeeMstReferView.EmployeeMstReferView.as_view(), name='employee_mst_refer'),
    # 社員マスタ更新
    path('<str:pk>/employee_mst_update/', EmployeeMstUpdateView.EmployeeMstUpdateView.as_view(), name='employee_mst_update'),
    # 社員マスタ削除
    path('<str:pk>/employee_mst_delete/', EmployeeMstDeleteView.EmployeeMstDeleteView.as_view(), name='employee_mst_delete'),
    # ユーザ登録
    path('user_create/', usercreate.UserCreate.as_view(), name='user_create'),
    # ユーザ登録完了
    path('user_create/complete/', usercreate.UserCreateComplete.as_view(), name='user_create_complete'),
    # ユーザ検索
    path('reference', userserch.Reference.as_view(), name='reference'),
]