from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from .customusermanager import CustomUserManager

class User(AbstractBaseUser, PermissionsMixin):
    """カスタムユーザーモデル."""

    employee_cd = models.IntegerField(verbose_name = '社員番号', primary_key = True)
    email = models.EmailField(verbose_name = 'メール')
    first_name = models.CharField(verbose_name = '名', max_length=30)
    last_name = models.CharField(verbose_name = '姓', max_length=30)

    is_active = models.BooleanField(verbose_name = '有効フラグ', default=True )
    date_insert = models.DateTimeField(verbose_name = '登録日', default=timezone.now)
    date_update = models.DateTimeField(verbose_name = '更新日', default=timezone.now)

    objects = CustomUserManager()

    USERNAME_FIELD = 'employee_cd'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        """Return the first_name plus the last_name, with a space in
        between."""
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)

    @property
    def username(self):
        """username属性のゲッター

        他アプリケーションが、username属性にアクセスした場合に備えて定義
        メールアドレスを返す
        """
        return self.email