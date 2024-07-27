from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def getmainpage(request): 
    msg = """
        <b>
            firstapp 내에 views.py의 mainpage가 호출되었습니다.
        </b>
    """
    return HttpResponse(msg)
def getmainpage_2(request): 
    msg = """
    <b>
        firsapp 내에 views.py의 mainpage_2가 호출되었습니다.
    </b>
    """
    return HttpResponse(msg)