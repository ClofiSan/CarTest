from .models import *
from django.http import HttpResponse

from django.db.models import Count
from django.views.decorators.csrf import csrf_exempt
import json
def JsonResponse(data):
    return HttpResponse({
        json.dumps(data,ensure_ascii=False)
    },content_type="application/json,charset=utf-8")

from django.shortcuts import render
postForResiterStudent = {
    # 用户和用户登录名
    'UserID': '',
    'PersonName':'',
    'Pin':'',
    'Phone':''
}
postForResiterUser = {
    'UserID':'',
    'PersonName':'',
    'LoginName':'',
    'Password':'',
    'UserType':'',
}
postForUserLogin = {
    'LoginName':'',
    'Password':''
}
postForStudentLogin = {
    'UserID':''
}
# 注册考生发送的数据格式
content_type ='application/json'
charset = 'utf-8'
# @csrf_exempt
def RegsiterUserAPI(request):
    if request.method == 'POST':
        LoginName = request.POST.get('LoginName')
        PersonName = request.POST.get('PersonName')
        psw = request.POST.get('Password')
        UserType = request.POST.get('UserType')
        if (not LoginName) or (not PersonName) or (not psw) or (not UserType):
            return JsonResponse({
                'code':400,
                'message':'请输入完整数据'
            })
        if Users.objects.filter(login_name=LoginName).count() != 0:
            return JsonResponse({
                'code':400,
                'message':'用户名已经被使用了'
            })
        count = Users.objects.aggregate(Count('user_id'))['user_id__count']+1
        user = Users(
            user_id= count,
            user_name=PersonName,
            login_name=LoginName,
            password=psw,
            user_type=UserType,
            sts='A',
        )
        user.save()
        return JsonResponse({
            'code': 200,
            'message': '注册成功！',
        })
    else:
        return JsonResponse({
            'code':400,
            'message':'请使用post方法'
        })
    # if request.method == 'GET':
    #     return JsonResponse(postForResiterUser)
# 如何序列化
def UserLoginAPI(request):
    if request.method == 'POST':
        LoginName = request.POST.get('LoginName')
        psw = request.POST.get('Password')
        # 校验是否正确
        if (not LoginName) or (not psw):
            return JsonResponse({
                'code': 400,
                'message':'请输入完整数据'
            })
        # 是否存在这个用户
        if Users.objects.filter(login_name=LoginName).count() == 0:
            return JsonResponse({
                'code': 400,
                'message': '用户不存在'
            })
        # 校验密码
        user = Users.objects.get(login_name=LoginName)
        if user.password != psw:
            return JsonResponse({
                'code':400,
                'message': '密码错误'
            })
        # user = Users.objects.get(login_name=request.POST.get('LoginName'))
        return JsonResponse({
            # 本地校验userType是否为S，如果不为S直接进入注册
            'code': 200,
            'message': '登录成功！',
            'UserID':user.user_id,
            'PersonName': user.user_name,
            'LoginName': user.login_name,
            'UserType':user.user_type
        })
    else:
        return JsonResponse({
            'code': 400,
            'message': '请使用post方法'
        })

def RegsiterStudentAPI(request):
    # 注册一个新的Student
    # 因为只有是Users才能成为Student所以不用验证
    if request.method == 'POST':

        UserID = request.POST.get('UserID')
        PersonName = request.POST.get('PersonName')
        Pin = request.POST.get('Pin')
        Phone = request.POST.get('Phone')
        # 判断输入数据是否存在
        if (not PersonName) or (not Pin) or (not Phone):
            return JsonResponse({
                'code': 400,
                'message': '请输入完整数据'
            })
        # 判断是否已经注册为Student
        if Student.objects.filter(id=UserID).count() != 0:
            return JsonResponse({
                'code': 400,
                'message': '已经是考生了'
            })
        student = Student(
            id=UserID,
            name=PersonName,
            pin=Pin,
            phone=Phone
        )
        student.save()
        return JsonResponse({
                'code':200,
                'message':'注册成功'
            })
    else:
        return JsonResponse({
            'code': 400,
            'message': '请用POST方法'
        })

def StudentLoginAPI(request):
    if request.method == 'POST':
        UserID = request.POST.get('UserID')
        # 校验是否正确
        if (not UserID):
            return JsonResponse({
                'code': 400,
                'message': '请输入完整数据'
            })
        # 是否存在这个用户
        if Student.objects.filter(id=UserID).count() == 0:
            return JsonResponse({
                'code': 400,
                'message': '用户不存在'
            })
        # 其实考生登录成功之后要返回考试信息的
        ExamineList = GetStudentExam(UserID)
        return JsonResponse({
            # 本地校验userType是否为S，如果不为S直接进入注册
            'code': 200,
            'message': '考生登录成功！',
            'Examines':ExamineList#考试信息列表
        })
    else:
        return JsonResponse({
            'code': 400,
            'message': '请使用post方法'
        })

def RegsiterExamAPI(request):
    # 为学生注册考试
    return JsonResponse()


def GetStudentExam(StudentID):
    # 获得考生的考试信息
    ExamineList = []
    return ExamineList


def JustForTest(request):
    if request.method == 'POST':
        LoginName = request.POST.get('LoginName')
        if not LoginName:
            return JsonResponse({
                'msg':'error what'
            })
        return JsonResponse({
            'msg':LoginName
        })
    if request.method == 'GET':
        try:
            user = Users.objects.get(user_id=2)
        except Users.DoesNotExist:
            return JsonResponse({
                'msg': 'null'
            })
        return JsonResponse({
            'msg':user.login_name
        })
# def LoginUserAPI(request):
#     # 用户登录
#     user = UserLogin()
#     return render(request,'re_user_data.html',locals())
#
# def RegsiterStudentAPI(request):
# #     注册成为考生，如果有未完成的考试就不允许注册
#     if request.method == 'POST':
# #         找到考生ID查找相关的,别忘了序列化
#         examine = Examine.objects.get(student=request.data['UserID'] )
#
#
# def LoginStudentAPI(request):
# #     考生登录，如果数据库没有考试信息就生成考试信息并返回考试信息
# #     否则就进入是否考试页面
#
#
#
#
#
# def ExamineAPI(request):
# # 前置条件：拥有用户名，考生ID
# # 事件：触发了‘我要考试按钮’，首先发送自己信息进入到考试界面
#     if request.method =='GET':
#
#     if request.method == 'POST':
#
#
#
#
#
# initEmPwd = 123456
# def createExamine(studentID):
#     # 获得考试信息
#     # 如何随机获取准考证
#     paper = createPaper()
#     examine = Examine(
#         id = Examine.objects.all().length + 1,
#         em_in = studentID + ,
#         em_pwd =initEmPwd,
#         student = studentID,
#         paper = paper.paper_id,
#         em_date = datetime.date()
#     )
#     examine.save()
#     return examine
#
#
#
#
# def createPaper():
#     questions = Questions()
#     # 直接新建了试卷
#     paper = Paper(paper_id=1,question_id_seq=questions.id_seq,
#                   key_seq=questions.key_seq)
#     paper.save()
#     return paper
#
# class Questions():
#     paperID = ''
#     id_seq = ''
#     key_seq = ''
#     def __init__(self):
#         self.createQuestionList()
#
#     def createQuestionList(self):
#         #随机获得问题的列表
#



