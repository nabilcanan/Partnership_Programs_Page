# myapp/views.py

from django.http import JsonResponse
from django.shortcuts import render
import sys
from subprocess import Popen, PIPE


def index(request):
    return render(request, 'myapp/index.html')


def run_creation_contract(request):
    try:
        # Use the sys.executable to ensure you're using the same Python interpreter
        # that's running Django to execute your script.
        process = Popen([sys.executable, 'P:/Partnership_Python_Projects/Creation/Sorting_Creation_Updated/main.py'],
                        stdout=PIPE, stderr=PIPE)
        stdout, stderr = process.communicate()

        if process.returncode == 0:
            # Success
            return JsonResponse({'message': 'Creation Contract Program executed successfully'})
        else:
            # Error
            return JsonResponse({'message': 'Error running script', 'error': stderr.decode()}, status=500)
    except Exception as e:
        return JsonResponse({'message': str(e)}, status=500)
