from .models import *
from django.http import HttpResponse
from django.http import JsonResponse
from django.db.models import Count
from django.views.decorators.csrf import csrf_exempt
import json

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

# @csrf_exempt
def RegsiterUserAPI(request):
    if request.method == 'POST':
        if Users.objects.get(login_name=request.POST.get('LoginName')) is not None:
             return JsonResponse({
                 'Status': 0,
                 'msg':'error:LoginName already existed'
             })
        count = Users.objects.aggregate(Count('user_id'))
        user = Users(
            user_id = count+1,
            user_name = request.POST.get('PersonName'),
            login_name = request.POST.get('LoginName'),
            password = request.POST.get('Password'),
            user_type = request.POST.get('UserType'),
            sts='A',
        )
        user.save()
        return JsonResponse({
            'Status':1,
            'msg':'Regsiter successful',
            'PersonName':user.user_name,
            'LoginName':user.login_name,
        })
    else:
        return JsonResponse({
            'Status':0,
            'msg':'error:method error'
        })
    # if request.method == 'GET':
    #     return JsonResponse(postForResiterUser)
# 如何序列化
def UserLoginAPI(request):
    if request.method == 'POST':
        psw = request.POST.get('Password')
        if Users.objects.get(login_name=request.POST.get('LoginName')) is None:
            return JsonResponse({
                'Status': 0,
                'msg': 'error:no LoginName'
            })
        if Users.objects.get(login_name=request.POST.get('LoginName')).password != psw:
            return JsonResponse({
                'Status':0,
                'msg': 'error:psw error'
            })
        user = Users.objects.get(login_name=request.POST.get('LoginName'))
        return JsonResponse({
            # 本地校验userType是否为S，如果不为S直接进入注册
            'Status': 1,
            'msg': 'Login successful',
            'UserID':user.user_id,
            'PersonName': user.user_name,
            'LoginName': user.login_name,
            'UserType':user.user_type
        })
    else:
        return JsonResponse({
            'Status': 0,
            'msg': 'error:method error'
        })

def RegsiterStudentAPI(request):
    # 注册一个新的Student
    # 因为只有是Users才能成为Student所以不用验证
    if request.method == 'POST':
        # 判断是否已经注册
        if Student.objects.get(id=request.POST.get('UserID')) is not None:
            return JsonResponse({
                 'Status': 0,
                 'msg':'error:UserID was already student'
             })

        student = Student(
            id=request.data['UserID'],
            name=request.data['PersonName'],
            pin=request.data['Pin'],
            phone=request.data['Phone']
        )
        student.save()
        Users.objects.get(user_id=request.data['UserID']).update(user_type='S')
        return JsonResponse({
                'Status':1,
                'msg':'Regsite Student successful',
                'PersonName':student.name,
            })
    else:
        return JsonResponse({
            'Status': 0,
            'msg': 'error:method error'
        })

def StudentLoginAPI(request):
#    根据UserID获得Student信息，UserType 为S
    if request.method == 'POST':
        if request.POST.get('UserType') != 'S':
            return JsonResponse({
                'Status':0,
                'msg':'you are not student',
            })
        student = Student.objects.get(id=request.POST.get('UserID'))
        return JsonResponse({
            'Status': 1,
            'msg':'Student Login successful'
        })
    else:
        return JsonResponse({
            'Status': 0,
            'msg': 'error:method error'
        })



def JustForTest(request):
    if request.method == 'POST':
        user = Users.objects.get(user_id=request.POST.get('LoginName'))
        print(user.user_name)
        return JsonResponse({
            'UserID': user.user_id,
            'PersonName': user.user_name,
            'LoginName': user.login_name,
            'Password': user.password,
            'UserType': user.user_type,
        })
    if request.method == 'GET':
        count = Users.objects.aggregate(Count('user_id'))
        return JsonResponse({
            'count':count
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



