import requests
import time
# from django.views.decorators.csrf import csrf_exempt
url = '127.0.0.1/api/'
urlapi = 'regsiterUser'
RegisterUserData = {
    'PersonName': '软柿子',
    'LoginName': 'Napoleon',
    'Password': '123456',
    'UserType':'A'
}
data = {
    'what':1
}
UserLoginData = {
    'LoginName': 'aaa',
    'Password': '123456',
}
RegisterStudentData = {
    'UserID':1,
    'PersonName':'Ventura',
    'Pin':'123456789123456789',
    'Phone':'17342016121'
}
StudentLoginData = {
    'UserID':5
}
backdata = {
    'ExamID': '',  # 考试ID
    'Score': '',  # 分数
    'EmDate': '',  # 考试时间
    'Status': ''  # 考试状态
}
RegsiterExamAPIData = {
    'UserID': 1
}
examLogindata1 = {
    'EmIn':'4W87ITG58U2F5PFS',
    'EmPwd':'FGFQGM0Q9U7TM99A'
}
examLogindata12={
    'EmIn':'4W87ITG58U2F5PFS',
    'EmPwd':''
}
getScoreData = {
    'ExamID':2,
    'Answer':'AACACBBAAABAABCAABBC'
}
# "4W87ITG58U2F5PFS", "EmPwd": "FGFQGM0Q9U7TM99A"
# @csrf_exempt
def post():
    r = requests.post(
        url='http://127.0.0.1:8000/api/JudgeMark/',
        data=getScoreData)
    print(r)
    print(r.text)
if __name__ == '__main__':
    post()
    # List = []
    # for i in range(100):
    #     List.append({
    #         'key':'name',
    #         'message':i
    #     })
    # print(List)
