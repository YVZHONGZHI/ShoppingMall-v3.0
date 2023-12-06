from .logger import log
from .response import APIResponse
from rest_framework.views import exception_handler


def common_exception_handler(exc, context):
    log.error('view是:%s , 错误是%s' % (context['view'].__class__.__name__, str(exc)))
    ret = exception_handler(exc, context)
    if ret:
        return APIResponse(code=0, msg='error', result=ret.data)
    return APIResponse(code=0, msg='error', result=str(exc))