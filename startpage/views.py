from django.shortcuts import render
from startpage.forms import ContactForm
from django.core.mail import send_mail
from django.http import HttpResponseRedirect

def start_page(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            subject = "{} wysłał/a prośbę o kontakt".format(cd['contact_name'])
            content = "Dane do kontaktu:\n{}\nNumer telefonu: {}," \
                      "\nE-mail: {}".format(cd['contact_name'],cd['contact_number'], cd['contact_email'])
            send_mail(subject, content, 'krzysiex92@gmail.com', ['krzysiex92@gmail.com', ])
            return HttpResponseRedirect('/')
    else:
        form = ContactForm()
    return render(request, 'startpage/index.html', {'form': form})

