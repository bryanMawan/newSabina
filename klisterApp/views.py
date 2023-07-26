from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import formPage
from .forms import formPageForm
from django.views.generic import CreateView
from .excel import add_row_to_excel, excel_password

main_path = None  # Retrieve the first instance of the formPage model
message = None


# Create your views here.
class formPageView(CreateView):
    model = formPage
    fields = ["name", "age", "stadsdel", "idrott", "önskad_idrott", "in_a_union"]
    template_name = 'home.html'
    success_url = reverse_lazy('DayListView')

    def form_valid(self, form):
        # Create the dictionary with field names and values
        data = {field: form.cleaned_data[field] for field in form.Meta.fields}

        # Print the dictionary to the terminal
        print(data)

        return super().form_valid(form)
     

def create_form(request):
    global message
    addRowConfirmation = None
    if main_path:
        filePath = main_path.split("/")[-1]  # Retrieve the filePath attribute from the formPage instance
    else:
        filePath = "None"
    is_error = message and message.startswith(" ")
    if request.method == 'POST':
        form = formPageForm(request.POST)
        print("posting")
        if form.is_valid():
            klisterData = {
                'name': form.cleaned_data['name'],
                'age': form.cleaned_data['age'],
                'stadsdel': form.cleaned_data['stadsdel'],
                'idrott': form.cleaned_data['idrott'],
                'önskad_idrott': form.cleaned_data['önskad_idrott'],
                'in_a_union': form.cleaned_data['in_a_union'],
            }
            print(klisterData)
            add_row_to_excel(filePath, klisterData)
            addRowConfirmation = klisterData['name'] + '(' + str(klisterData['age']) + ')' + " row added!"
            
            return render(request, 'success.html', {'data': klisterData, 'filePath': filePath, 'message': message, 'is_error': is_error, addRowConfirmation: 'addRowConfirmation'})
    else:
        form = formPageForm()

    return render(request, 'home.html', {'form': form, 'filePath': filePath, 'message': message, 'is_error': is_error})


def change_filepath(request):
    global main_path  # Declare main_path as a global variable
    global message

    if request.method == 'POST':
        password = request.POST.get('password')
        # Custom authentication logic for the password
        if password == excel_password:

            # Authentication successful
            main_path = request.POST.get('file_path')
            message = 'File updated successfully.'
            # messages.success(request, 'File path updated successfully.')
            print(message)
            return HttpResponseRedirect("/")
        else:
            # Authentication failed
            message = " " + 'Invalid password. Please try again.'
            print(message)
            # messages.error(request, 'Invalid password. Please try again.')
            return HttpResponseRedirect("/")


def change_password(request):
    global main_path  # Declare main_path as a global variable
    global message
    global excel_password

    if request.method == 'POST':
        old_password = request.POST.get('old_password')
        new_password = request.POST.get('new_password')
        confirmed_password = request.POST.get('confirmed_password')

        # Custom authentication logic for the password
        if old_password != excel_password:

            # Send error message
            message = ' Old password does not match!'
            # messages.success(request, 'File path updated successfully.')
            print(message)
            return HttpResponseRedirect("/")
        elif new_password != confirmed_password:
            # Authentication failed
            message = " " + 'New passwords do not match!'
            print(message)
            # messages.error(request, 'Invalid password. Please try again.')
            return HttpResponseRedirect("/")
        else:
            excel_password = new_password
            message = 'Password changed succesfully!'
            print(message)
            # messages.error(request, 'Invalid password. Please try again.')
            return HttpResponseRedirect("/")


