from django.shortcuts import render
import subprocess

def index(request):
    #https://www.hacksplaining.com/exercises/command-execution
    if request.method == 'POST':
        input = request.POST.get('ip')
        print(input)
        command = 'nslookup '+input
        print(command)
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            output = result.stdout
            success_message = "Command executed successfully."
        else:
            output = result.stderr
            success_message = "Error executing the command."
        print(result)
       
        context = {  
            'output': output,
            'success': success_message
        }
        return render(request,'index.html', context)