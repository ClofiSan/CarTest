import requests
import time
# from django.views.decorators.csrf import csrf_exempt
url = '127.0.0.1/api/'
urlapi = 'regsiterUser'
data = {
    'UserID': 1,
    'PersonName': 'Ventura',
    'login_name': 'Ventura',
    'Password': '123456',
    'UserType': 'A',
}
# @csrf_exempt
def post():
    r = requests.post(url='http://127.0.0.1:8000/api/regsiterUser/',data=data)
    print(r)
    print(r.text)
if __name__ == '__main__':
    post()
