
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def test_api(request):
    return JsonResponse({"resultType": "GetStudentPass", "msg": "UserMessage"})


# 提交注册表单，校验表单