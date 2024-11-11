from django.shortcuts import render

def FacultyHomePage(request):
    return render(request, 'facultyapp/FacultyHomepage.html')
