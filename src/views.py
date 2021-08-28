from django.shortcuts import render, redirect
from .forms import UploadFileForm
from django.shortcuts import render
import tensorflow as tf
# import kerass
import smtplib
import ssl
import base64
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import numpy as np
from .models import Files
from .forms import UploadFileForm
import os
from datetime import date
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def upload(request):
    return render(request, 'upload.html')


def about(request):
    return render(request, '/Users/deveshkedia/Desktop/Projects/AIIJC/The-Logical-Order/src/template/about.html')


def index(request):
    return render(request, "landing_page.html")


def contact(request):
    return render(request, "contact.html")


def sendFeedback(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        review = request.POST['review']
        sender_email = "kediadevesh123@gmail.com"
        receiver_email = "kediadevesh123@gmail.com"
        password = "Dkedia@3349"

        message = MIMEMultipart("alternative")
        message["Subject"] = "HEY FEEDBACK COMMING IN!!!"
        message["From"] = email
        message["To"] = receiver_email

        # Create the plain-text and HTML version of your message
        text = f"""\
            FEEDBACK 
            FROM :- 
                NAME - {name}
                FEEDBACK - {review}
                EMAIL- {email}
        """
        html = f"""\
        <html>
        <body>
            <h3>FEEDBACK</h1>
                <h3>FROM :- </h3>
                   <h3> NAME - {name}</h3>
                   <h3> FEEDBACK - {review}</h3>
                   <h3> EMAIL- {email}</h3>
        </body>
        </html>
        """
        part1 = MIMEText(text, "plain")
        part2 = MIMEText(html, "html")
        message.attach(part1)
        message.attach(part2)
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(
                sender_email, receiver_email, message.as_string()
            )
        return render(request, 'responseRecorded.html')


def post(request):
    if request.POST['uploadedFile'] == '':
        form = UploadFileForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            print("ISALID")
            files = form.cleaned_data['image']
            fi = request.FILES['image'].name
            print(fi)
            today = date.today()
            fileND = fi.split('.', 1)
            imageFile = Files(image=files,
                              filename=f"{fi}", date=today.strftime("%Y-%m-%d"))
            imageFile.save()
            filename = f"/Users/deveshkedia/Desktop/Projects/Relativity/Relativity/MEDIABIN/media/{fi}"
            filenamesabc = f'{fi}.png'
            fileND = filenamesabc.split('.', 1)
            model = tf.keras.models.load_model(
                "/Users/deveshkedia/Desktop/Projects/AIIJC/WEB/The-Logical-Order/src/Model")
            print(filename)
            predictions = model.predict(filename)
            print(np.where(predictions[0] == max(predictions[0])))
            result = np.where(predictions[0] == max(predictions[0]))
            report = result[0][0]
            fileND = filenamesabc.split('.', 1)
            os.remove(
                f"/Users/deveshkedia/Desktop/Projects/Relativity/Relativity/MEDIABIN/media/{fi}")
            return render(request, "scan.html", {"model": report, 'file': fileND[0]})
        else:
            form = UploadFileForm()
            return render(request, 'upload.html', {'form': form})
    else:
        raw_data = request.POST['uploadedFile']
        img_data = raw_data.split(',', 1)
        # print(img_data[1])
        import base64
        imgdata = base64.b64decode(img_data[1])
        fi = f"/Users/deveshkedia/Desktop/Projects/AIIJC/The-Logical-Order/MEDIABIN/media/{request.POST['data']}"
        with open(fi, 'wb') as f:
            f.write(imgdata)
        filename = f"/Users/deveshkedia/Desktop/Projects/Relativity/Relativity/MEDIABIN/media/{fi}"
        filenamesabc = fi
        fileND = filenamesabc.split('.', 1)
        model = tf.keras.models.load_model(
            "/Users/deveshkedia/Desktop/Projects/AIIJC/WEB/The-Logical-Order/src/Model")
        print(filename)
        predictions = model.predict(filename)
        print(np.where(predictions[0] == max(predictions[0])))
        result = np.where(predictions[0] == max(predictions[0]))
        report = result[0][0]
        fileND = filenamesabc.split('.', 1)
        os.remove(
            f"/Users/deveshkedia/Desktop/Projects/Relativity/Relativity/MEDIABIN/media/{fi}")
        return render(request, "scan.html", {"model": report, 'file': fileND[0]})
    return render(request, 'hello.htnl')


def home(request):
    return render(request, 'landing_page_without_animation.html')
