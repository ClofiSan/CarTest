from .models import *
from django.http import HttpResponse
from django.db.models import Count
from django.db import connection, transaction
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers import serialize
from django.shortcuts import render
import json


def JsonResponse(data):
    return HttpResponse({
        json.dumps(data, ensure_ascii=False)
    }, content_type="application/json,charset=utf-8")



postForResiterStudent = {
    # 用户和用户登录名
    'UserID': '',
    'PersonName': '',
    'Pin': '',
    'Phone': ''
}
postForResiterUser = {
    'UserID': '',
    'PersonName': '',
    'LoginName': '',
    'Password': '',
    'UserType': '',
}
postForUserLogin = {
    'LoginName': '',
    'Password': ''
}
postForStudentLogin = {
    'UserID': ''
}
# 注册考生发送的数据格式
content_type = 'application/json'
charset = 'utf-8'



def getUserLoginPage(request):
    datas = {'title': '用户登录界面'}
    if request.method == 'GET':
        return render(request,'user_login_page.html',context=datas)

def  UserSuc(request):
    datas = {'title': '用户界面'}
    if request.method == 'POST':
        datas['loginName'] = request.POST['userName']
        datas['Password'] = request.POST['pw']
        if Users.objects.filter(login_name=datas['loginName']).count() == 0:
            datas['message'] = "用户不存在"
            return render(request, 'new.html', context=datas)
        print(2)  # 校验密码
        user = Users.objects.get(login_name=datas['loginName'])
        if user.password != datas['Password']:
            datas['message'] = "密码错误"
            return render(request, 'new.html', context=datas)
        print(3)
        datas['message'] = "登录成功！"
        return render(request, 'new.html', context=datas)


# @csrf_exempt
def RegsiterUserAPI(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        param = json.loads(data)
        LoginName = param['LoginName']
        PersonName = param['PersonName']
        psw = param['Password']
        UserType = param['UserType']
        if (not LoginName) or (not PersonName) or (not psw) or (not UserType):
            return JsonResponse({
                'code': 400,
                'message': '请输入完整数据'
            })
        if Users.objects.filter(login_name=LoginName).count() != 0:
            return JsonResponse({
                'code': 400,
                'message': '用户名已经被使用了'
            })
        count = Users.objects.aggregate(Count('user_id'))['user_id__count'] + 1
        user = Users(
            user_id=count,
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
            'code': 400,
            'message': '请使用post方法'
        })
    # if request.method == 'GET':
    #     return JsonResponse(postForResiterUser)


# 如何序列化
def UserLoginAPI(request):
    if request.method == 'POST':
        # 校验是否正确
        print(request.body)
        data = request.body.decode('utf-8')
        print(data)
        param = json.loads(data)
        LoginName = param["LoginName"]
        psw = param["Password"]
        if (not LoginName) or (not psw):
            return JsonResponse({
                'code': 400,
                'message': '请输入完整数据',
                # 'psw':request.body,
                # 's':request.data
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
                'code': 400,
                'message': '密码错误'
            })
        # user = Users.objects.get(login_name=request.POST.get('LoginName'))
        return JsonResponse({
            # 本地校验userType是否为S，如果不为S直接进入注册
            'code': 200,
            'message': '登录成功！',
            'UserID': user.user_id,
            'PersonName': user.user_name,
            'LoginName': user.login_name,
            'UserType': user.user_type
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
        data = request.body.decode('utf-8')
        param = json.loads(data)
        UserID = param['UserID']
        PersonName = param['PersonName']
        Pin = param['Pin']
        Phone = param['Phone']
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
            'code': 200,
            'message': '注册成功'
        })
    else:
        return JsonResponse({
            'code': 400,
            'message': '请用POST方法'
        })


def StudentLoginAPI(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        param = json.loads(data)
        UserID = param['UserID']
        # 校验是否正确
        if (not UserID):
            return JsonResponse({
                'code': 400,
                'message': '请输入完整数据'
            })
        # 是否存在这个用户
        if Student.objects.filter(id=UserID).count() == 0:
            return JsonResponse({
                'code': 401,
                'message': '考生不存在'
            })
        # 其实考生登录成功之后要返回考试信息的
        # ExamineList = GetStudentExam(UserID)
        student = Student.objects.get(id=UserID)
        return JsonResponse({
            # 本地校验userType是否为S，如果不为S直接进入注册
            'code': 200,
            'message': '考生登录成功！',
            'pin': student.pin,
            'phone': student.phone
            # 'Examines':ExamineList#考试信息列表
        })
    else:
        return JsonResponse({
            'code': 400,
            'message': '请使用post方法'
        })


def GetStudentExam(UserID):
    # 返回考生的考试信息,
    # 准考证号，考试时间，考试分数，点击进去可以看到考试的分数
    return


def RegsiterExamAPI(request):
    # @为学生注册考试
    # 创建考卷，记录进数据库
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        param = json.loads(data)
        print(type(param))
        studentID = param['UserID']
        if not studentID:
            return JsonResponse({
                'code': 400,
                'message': '请输入完整数据'
            })
        if Student.objects.filter(id=studentID).count() == 0:
            return JsonResponse({
                'code': 401,
                'message': '考生不存在'
            })
        examID = Examine.objects.aggregate(Count('id'))['id__count'] + 1
        CreateNewExam(examID, studentID)
        examine = Examine.objects.get(id=examID)
        return JsonResponse({
            'code': 200,
            'message': '注册新考试成功',
            'ExamID': examine.id,
            'EmIn': examine.em_in,
            'EmPwd': examine.em_pwd,
        })
    else:
        return JsonResponse({
            'code': 400,
            'message': '请使用post方法'
        })


def ExamLoginAPI(request):
    # 输入准考证号以登陆
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        print(data)
        param = json.loads(data)
        print(param)
        EmIn = param['EmIn']
        EmPwd = param['EmPwd']
        if (not EmIn) or (not EmPwd):
            return JsonResponse({
                'code': 400,
                'message': '请输入完整数据'
            })
        if Examine.objects.filter(em_in=EmIn).count() == 0:
            return JsonResponse({
                'code': 400,
                'message': '准考证号错误'
            })
        examine = Examine.objects.get(em_in=EmIn)
        if examine.em_pwd != EmPwd:
            return JsonResponse({
                'code': 400,
                'message': '准考密码错误'
            })
        paper = Paper.objects.get(paper_id=examine.paper_id)
        QuestionList = []
        for questionID in paper.question_id_seq.split('-'):
            if not questionID:
                break
            question = Question.objects.filter(question_id=questionID)
            # QuestionList.append({
            #     'QuestionBody':question.question_body,
            #     'QuestionForm':question.question_form,
            #     'BranchA':question.branch_a,
            #     'BranchB':question.branch_b,
            #     'BranchC':question.branch_c,
            #     'PicName':question.pic_name,
            #     'QuestionTypeID':question.question_type_id,
            #     'QuestionMark':question.question_mark
            # })
            QuestionListJsonData = serialize('json', question)
            QuestionListJsonData = json.loads(QuestionListJsonData)
            QuestionList.append(QuestionListJsonData)
        # questionID的序列的存储格式什么
        return JsonResponse({
            'code': 200,
            'message': '进入考试',
            'ExamID':examine.id,
            'QuestionList': QuestionList
        })


def CreateNewExam(examID, studentID):
    cursor = connection.cursor()
    cursor.callproc('PROC_GET_EXAM', [examID, studentID])
    cursor.close()


def JudgeMarkAPI(request):
    # 根据用户提交的请求判断用户所得的分
    # 这个时候服务端所得到的是一个答案和考试的id
    if request.method == 'POST':
        # 判断是否全部提交（留给前端）
        data = request.body.decode('utf-8')
        param = json.loads(data)
        ExamID = param['ExamID']
        Answer = param['Answer']
        examineValue = Examine.objects.filter(id=ExamID).values()
        paper = Paper.objects.filter(paper_id=examineValue[0]['paper_id']).values()
        # examine.answer = Answer
        score = 0
        key_seq = paper[0]['key_seq']
        for i in range(0, 20):
            if key_seq[i] == Answer[i]:
                score = score + 5
        examine = Examine.objects.get(id=ExamID)
        examine.answer = Answer
        examine.status = 'B'
        examine.score = score
        examine.save()
        return JsonResponse({
            'code': 200,
            'message': '已提交考试成绩',
            'score': score
        })
    else:
        return JsonResponse({
            'code': 400,
            'message': '请使用post方法'
        })


def JustForTest(request):
    # 测试函数
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        param = json.loads(data)
        LoginName = param['LoginName']
        if not LoginName:
            return JsonResponse({
                'msg': 'error what'
            })
        return JsonResponse({
            'msg': LoginName
        })
    if request.method == 'GET':
        ExamID = 2
        Answer = 'AACACBBAAABAABCAABBC'
        Answer = 'AACACBBAAABAABCAABBC'
        examine = Examine.objects.filter(id=ExamID).values()
        paper = Paper.objects.filter(paper_id=examine[0]['paper_id']).values()
        # examine.answer = Answer
        score = 0
        key_seq = paper[0]['key_seq']
        for i in range(0, 20):
            if key_seq[i] == Answer[i]:
                score = score + 5
        # examine.score = score
        return JsonResponse({
            'code': 200,
            'message': '已提交考试成绩',
            'score': score
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
