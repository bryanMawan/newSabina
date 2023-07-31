from django.urls import reverse
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import password, SpreadsheetId
from .forms import formPageForm
from django.views.generic import CreateView
from .excel import add_row_to_google_sheets, extract_key_from_url, get_sheet_name
from django.views.generic import TemplateView


main_path = None  # Retrieve the first instance of the formPage model
message = None


class SuccessView(TemplateView):
    template_name = 'success.html'


def create_form(request):
    global message
    addRowConfirmation = None
    # Set a default value for filePath
    spreadsheet_id = None

    # Retrieve the file path from the FilePath model
    try:
        spreadSheet_instance = SpreadsheetId.objects.get(pk=1)  # Assuming the FilePath instance has primary key 1
        spreadsheet_id = spreadSheet_instance.IDString
    except SpreadsheetId.DoesNotExist:
        pass  # Handle the case when the FilePath instance does not exist
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
            try:
                add_row_to_google_sheets(spreadsheet_id, klisterData)
                addRowConfirmation = klisterData['name'] + '(' + str(klisterData['age']) + ')' + " row added!"
                # Redirect to the success URL using reverse
                success_url = reverse('success')
                return redirect(success_url)
            except Exception as e:
                if "Read-only file system" in str(e):
                    message = " " + "Error: You do not have permission to write to this file"
                else:
                    message = " " + f"An error occurred: {str(e)}"
                return redirect('home')  # Redirect back to the form page with the error message

    else:
        form = formPageForm()

    return render(request, 'home.html', {'form': form, 'spreadsheet_id': get_sheet_name(spreadsheet_id), 'message': message, 'is_error': is_error})


def change_filepath(request):
    global message

    if request.method == 'POST':
        entered_password = request.POST.get('password')
        try:
            password_instance = password.objects.get(pk=1)  # Assuming the password instance has primary key 1
        except password.DoesNotExist:
            message = " " + "Password instance does not exist."
            return HttpResponseRedirect("/")

        if entered_password != password_instance.password:
            message = " " + "Invalid password. Please try again."
            return HttpResponseRedirect("/")
        else:
            spreadsheet_link = request.POST.get('spreadsheet_link')
            # Update or create the FilePath instance
            file_path_instance, created = SpreadsheetId.objects.update_or_create(pk=1, defaults={'IDString': extract_key_from_url(spreadsheet_link)})
            message = 'File updated successfully.'
            return HttpResponseRedirect("/")


def change_password(request):
    global main_path  # Declare main_path as a global variable
    global message
    global excel_password
    if request.method == 'POST':
        old_password = request.POST.get('old_password')
        new_password = request.POST.get('new_password')
        confirmed_password = request.POST.get('confirmed_password')

        # Retrieve the password instance from the database
        try:
            password_instance = password.objects.get(pk=1)  # Assuming the password instance has primary key 1
        except password.DoesNotExist:
            # If the password instance doesn't exist, create a new one with the provided new_password
            password_instance = password(password=new_password)
            password_instance.save()

        # Custom authentication logic for the password
        if old_password != password_instance.password:
            message = " " + 'Old password does not match!'
            return HttpResponseRedirect("/")
        elif new_password != confirmed_password:
            message = " " + 'New passwords do not match!'
            return HttpResponseRedirect("/")
        else:
            password_instance.password = new_password
            password_instance.save()
            message = 'Password changed successfully!'
            return HttpResponseRedirect("/")


"""def modalErrorMessage(messageString):
    # Handle when the password instance does not exist.
    message = " " + messageString
    return HttpResponseRedirect("/")

def modalSuccessMessage(message, messageString):
    # Handle when the password instance does not exist.
    message = " " + messageString
    return HttpResponseRedirect("/")"""
