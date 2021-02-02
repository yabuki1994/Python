from django.db import models


class code(models.Model):
    # コード名
    code_name = models.CharField(max_length=20)
    # コード値
    code = models.CharField(max_length=7)
    # コード内容
    code_de = models.CharField(max_length=30, null=True)
    # 表示順
    sort = models.DecimalField(max_digits=2, decimal_places=0, null=True)

    class Meta:
        constraints = [
            # 複合ユニーク制約
            models.UniqueConstraint(fields=['code_name', 'code'], name='unique_booking'),
        ]

    def __str__(self):
        return self.code_de