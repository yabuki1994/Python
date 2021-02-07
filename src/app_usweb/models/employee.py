from django.db import models
from django.core.validators import MinLengthValidator, RegexValidator


class employee(models.Model):
    # 社員番号
    employee_cd = models.CharField(max_length=6,
                                                        primary_key=True,
                                                        validators=[MinLengthValidator(6, '6文字で入力してください'),
                                                        RegexValidator(r'^[0-9]*$', '数字で入力してください')],
                                                        verbose_name = u"社員番号")
    # 氏名
    employee_name = models.CharField(max_length=15, verbose_name = u"氏名")
    # カナ氏名
    employee_name_kana = models.CharField(max_length=30, blank=True, verbose_name = u"カナ氏名")
    # 入社年月
    hire_date_ym = models.DecimalField(max_digits=6, decimal_places=0, verbose_name = u"入社年月")
    # 趣味
    hobby = models.CharField(max_length=10, blank=True, verbose_name = u"趣味")
    # 保有資格１
    qualification1 = models.CharField(max_length=20, blank=True, verbose_name = u"保有資格１")
    # 保有資格2
    qualification2 = models.CharField(max_length=20, blank=True, verbose_name = u"保有資格2")
    # 保有資格3
    qualification3 = models.CharField(max_length=20, blank=True, verbose_name = u"保有資格3")
    # 登録日時
    regist_date = models.DateTimeField(auto_now_add=True, verbose_name = u"登録日時")
    # 最終更新日時
    update_date = models.DateTimeField(auto_now=True, verbose_name = u"最終更新日時")
    # 部署コード
    department_cd = models.DecimalField(max_digits=3, decimal_places=0, null=True, verbose_name = u"部署コード")
    # 役職コード
    position_cd = models.DecimalField(max_digits=2, decimal_places=0, null=True, verbose_name = u"役職コード")