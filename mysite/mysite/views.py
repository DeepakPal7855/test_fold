from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    data={
        'title': 'jome New',
        'clist': ['PHP','Python','JAVA'],
        'numbers': [],
        'student_details': [
            {'name':'pradeep', 'phone':76587654658},
            {'name':'ramesh', 'phone':87654321987},
            {'name':'suresh', 'phone':98765432109}
        
        ]
    }
    
    
    
    return render(request, "index.html", data)

def aboutus(request):
    return HttpResponse("Welcome tfjhgjo dd")

def Course(request):
    return HttpResponse("iusfkjdsijf ioufkdjsfl")

def Coursedetails(request,courseid):
    return HttpResponse(courseid)