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
# @csrf_exempt
def post():
    r = requests.post(
        url='http://127.0.0.1:8000/api/StudentLogin/',
        data=StudentLoginData)
    print(r)
    print(r.text)
if __name__ == '__main__':
    post()