from django.shortcuts import render
from app.models import profile
import pdfkit
from django.http import HttpResponse
from django.template import loader
import io
# Create your views here.
def accept(request):
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        phone=request.POST.get("mobile")
        about=request.POST.get("about")
        degree=request.POST.get("degree")
        university=request.POST.get("university")
        school=request.POST.get("school")
        previous_work=request.POST.get("previous_work")
        skills=request.POST.get("skills")
        Profile=profile(name=name,email=email,phone=phone,summary=about,
                        degree=degree,university=university,school=school,previous_work=previous_work,skills=skills)
        Profile.save()
    return render(request,'app/accept.html')
def resume(request,id):
    user_profile=profile.objects.get(id=id)
    template=loader.get_template('app/resume.html')
    html=template.render({'user_profile':user_profile})
    options={
    'page-size':'Letter',
    'encoding':"UTF-8",
     }
    config = pdfkit.configuration(
    wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')
    pdf=pdfkit.from_string(html,False,options=options,configuration=config)
    response=HttpResponse(pdf,content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="resume.pdf"'
    return response 
def list(request):
    profiles=profile.objects.all()
    return render(request,'app/list.html',{"profiles":profiles}) 