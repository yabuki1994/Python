from django import template
from ..models import employee
import logging

register = template.Library()
# ログ設定
logger = logging.getLogger(__name__)

@register.simple_tag
def url_replace(request, field, value):
    dict_ = request.GET.copy()
    dict_[field] = value
    return dict_.urlencode()

@register.simple_tag
def get_employee_label(value):
    """
    社員モデルのキーからラベル値を取得する。

    Parameters
    ----------
    value : String
        対象の社員モデルのキー値。

    Returns
    -------
    ret : String
        対象の社員モデルのラベル値。
    """
    meta_fields  = employee._meta.get_fields()
    ret = ""
    for i, meta_field in enumerate(meta_fields):
        if meta_field.name == value:
            ret = meta_field.verbose_name

    # output log
    logger.debug("key : {0} -> label : {1}".format(value, ret))
    return ret