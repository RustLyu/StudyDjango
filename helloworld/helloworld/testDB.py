from TestModel.models import testmodel
from django.http import HttpResponse

def testDB(request):
    tm = testmodel(name='runoobdb')
    tm.save()
    return HttpResponse("<p>save ok</p>")