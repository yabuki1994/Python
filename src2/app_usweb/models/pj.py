from django.db import models


class pj(models.Model):
    # PJコード
    pj_cd = models.CharField(max_length=10, primary_key=True)
    # PJ名
    pj_name = models.CharField(max_length=30)
    # PJ名カナ
    pj_name_kana = models.SlugField(max_length=60, null=True)
    # 作業場所
    working_place = models.CharField(max_length=20, null=True)
    # 作業場所最寄駅
    station = models.CharField(max_length=20, null=True)
    # 契約期間（開始）
    contractPJ_s_date = models.CharField(max_length=10, null=True)
    # 契約期間（終了予定）
    contractPJ_e_date = models.CharField(max_length=10, null=True)
    # 表示フラグ
    disp_flg = models.DecimalField(max_digits=1, decimal_places=0)
    # 登録日時
    regist_date = models.DateTimeField(auto_now_add=True)
    # 最終更新日時
    update_date = models.DateTimeField(auto_now=True)
