from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
students = {
        1910709282211: {
            'Firstname': 'Marius',
            'Lastname': 'Ciurea',
            'Classes': ['Maths', 'Informatics', 'Physics']
        },
        1890709282211: {
            'Firstname': 'Dan',
            'Lastname': 'Chivu',
            'Classes': ['English', 'History', 'Geography']
        }
    }

def student_data(request):
    return JsonResponse(students)