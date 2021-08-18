from django.shortcuts import render, redirect
from .forms import UploadFileForm
from django.shortcuts import render
# import tensorflow as tf
import smtplib
import ssl
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import numpy as np
from .models import Files
from .forms import UploadFileForm, NewUserForm
import os
from datetime import date
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def upload(request):
    return render(request, 'upload.html')


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        name = request.POST['name']
        age = request.POST['age']
        if form.is_valid():
            files = form.cleaned_data['file']
            fi = request.FILES['file'].name
            today = date.today()
            fileND = fi.split('.', 1)
            imageFile = Files(image=files, name=name,
                              age=age, filename=f"{fileND[0]}.png", date=today.strftime("%Y-%m-%d"), user=request.user, gender=request.POST['gender'])
            imageFile.save()
        filename = f"/Users/deveshkedia/Desktop/Projects/Relativity/Relativity/MEDIABIN/media/{fi}"
        filenamesabc = f'{fi}.png'
        fileND = filenamesabc.split('.', 1)
        model = tf.keras.models.load_model(
            "/Users/deveshkedia/Desktop/Projects/Relativity/Relativity/src/Model")
        print(filename)
        predictions = model.predict(filename)
        print(np.where(predictions[0] == max(predictions[0])))
        result = np.where(predictions[0] == max(predictions[0]))
        report = result[0][0]
        fileND = filenamesabc.split('.', 1)
        os.remove(
            f"/Users/deveshkedia/Desktop/Projects/Relativity/Relativity/MEDIABIN/media/{fi}")
        return render(request, "scan.html", {"model": answer, 'file': fileND[0]})
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})


def about(request):
    return render(request, 'about.html')


def index(request):
    return render(request, "landing_page.html")


def contact(request):
    return render(request, "contact.html")


def sendFeedback(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        review = request.POST['review']
        sender_email = "kediadevesh123@gmail.com"  # Enter your address
        receiver_email = "kediadevesh123@gmail.com"  # Enter receiver address
        print(name, email, review)
        message = MIMEMultipart("alternative")
        message["Subject"] = "FEEDBACK COMING IN!!!!"
        message["From"] = email
        message["To"] = receiver_email
        port = 465
        smtp_server = "smtp.gmail.com"
        password = "Dkedia@3349"
        text = f"""\
            NAME:- {name}
            FEEDBACK :- {review}
        """
        part1 = MIMEText(text, "plain")
        message.attach(part1)
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
        return render(request, 'responseRecorded.html')
