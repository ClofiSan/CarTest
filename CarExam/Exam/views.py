from .models import *
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from django.shortcuts import render
postForResiterStudent = {
    # 用户和用户登录名
    'UserID': '',
    'PersonName':'',
    'pin':'',
    'phone':''

}
postForResiterUser = {
    'UserID':'',
    'PersonName':'',
    'login_name':'',
    'Password':'',
    'UserType':'',
}
# 注册考生发送的数据格式

# @csrf_exempt
def RegsiterUserAPI(request):
    if request.method == 'POST':
        # if Users.objects.get(user_id=request.Post.get('UserID')) is not None:
        #     return JsonResponse({'msg':'error:already existed'})
        # user = Users(
        #     user_id=request.Post.get('UserID'),
        #     user_name=request.Post.get('PersonName'),
        #     login_name=request.Post.get('login_name'),
        #     password=request.Post.get('Password'),
        #     user_type=request.Post.get('UserType'),
        #     sts='A'
        # )
        # user.save()
        user_id = request.POST.get('UserID'),
        user_name = request.POST.get('PersonName'),
        login_name = request.POST.get('login_name'),
        password = request.POST.get('Password'),
        user_type = request.POST.get('UserType'),
        print(user_id[0])
        Users.objects.create(
            # user_id=user_id[0],
            # user_name=user_name[0],
            # login_name=login_name[0],
            # password=password[0],
            # user_type=user_type[0],
            user_id=request.POST.get('UserID'),
            user_name=request.POST.get('PersonName'),
            login_name=request.POST.get('login_name'),
            password=request.POST.get('Password'),
            user_type=request.POST.get('UserType'),
            sts='A',
        )
        return JsonResponse({
            'UserID': user_id,
            'PersonName': user_name,
            'login_name': login_name,
            'Password': password,
            'UserType': user_type,
        })


        # user.save()
        # return HttpResponse(content='register successfully')
    else:return JsonResponse({'msg':'error:method error'})
    # if request.method == 'GET':
    #     return JsonResponse(postForResiterUser)
# 如何序列化
def RegsiterStudentAPI(request):
    # 注册一个新的User,返回准考证件号码
    if request.method == 'POST':
        # 判断是否已经注册
        if Student.objects.get(id=request.data['UserID']) is not None:
            return HttpResponse(content='student already exist')

        student = Student(
            id=request.data['UserID'],
            name=request.data['PersonName'],
            pin=request.data['pin'],
            phone=request.data['phone']
        )
        student.save()
    return HttpResponse(content='register successfully')
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



