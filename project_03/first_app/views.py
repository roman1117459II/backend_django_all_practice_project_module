from django.shortcuts import render
import datetime
# Create your views here.

def home(request):
    d = {'author': 'Zaima', 'age': 14, 'lst': ["Dhaka", "chattagram", "Sylhet", "Bandarban"], 'birthday': datetime.datetime.now(), 'val': '','courses': [

        {
            'id': 19,
            'name': 'python',
            'fee': 20

        },
        {
            'id': 28,
            'name': 'Django',
            'fee': 50
        },
        {
            'id': 32,
            'name': 'Flask',
            'fee': 40
        },

    ]}
    return  render(request, 'home.html', context= d)