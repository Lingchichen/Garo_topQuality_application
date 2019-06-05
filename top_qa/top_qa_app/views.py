from django.http import HttpResponse,HttpRequest,Http404
from django.template import loader
from django.shortcuts import render_to_response
from top_qa_app.models import Contact,User
from  django.shortcuts import render
from django.db.models import Q
from django.contrib import messages
from django.http import HttpResponseRedirect,HttpResponseNotFound,response
from django.db import models
from django.contrib.auth import authenticate, login
from pip._vendor.requests import sessions
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render


#admin interface
def create_admin(request):
    template=loader.get_template('top_qa_app/admin_login.html')
    return HttpResponse(template.render({} ,request))
#admin_valid
def admin_valid(request):
    msg="Incorrect password or login name"
    if request.method =="POST":
        username=request.POST.get('login_name')
        password=request.POST.get('password')
        if User.objects.filter(Q(user_name=(str(username)))&Q(password=password)&Q(is_admin=True)).exists():
            #save id to session
            id=User.objects.filter(Q(user_name=(str(username)))&Q(password=password)&Q(is_admin=True)).values('id')[0]['id']
            request.session['id']=id
            request.session['password']=password
            request.session['isAdmin']=True
            # user's session cookie will expire when the user's Web browser is closed.
            request.session.set_expiry(0)
            #login successfully,redirect to '/contact/'

            return HttpResponseRedirect('/admin-login/select-user/')
        else:
            return render(request,'top_qa_app/admin_login.html', {'msg':msg})

def user_select(request):
    msg="you don't have the authority, please login first"
    template = loader.get_template('top_qa_app/admin_login.html')
    if  User.objects.filter(id=str(request.session['id']), password=str(request.session['password']),is_admin=True).exists():
        contact=User.objects.all()
        temp=loader.get_template('top_qa_app/user_select.html')
        return HttpResponse(temp.render({'contact':contact} ,request))
    else:
        return HttpResponseNotFound(template.render({'msg':msg}, request))

def user_delete(request,id):
    msg="you don't have the authority, please login first"
    template = loader.get_template('top_qa_app/admin_login.html')
    try:
        if  User.objects.filter(id=str(request.session['id']), password=str(request.session['password']),is_admin=True).exists():
            data = User.objects.filter(id=id)
            data.delete()
            return HttpResponseRedirect('/admin-login/select-user/')
    except:
        return HttpResponseNotFound(template.render({'msg':msg}, request))

def user_save(request,id):
    msg="you don't have the authority, please login first"
    template = loader.get_template('top_qa_app/user_login.html')
    username_msg="Your username cannot be empty"
    password_msg="Your password canno be empty"
    if  User.objects.filter(id=str(request.session['id']), password=str(request.session['password']),is_admin=True).exists():
        if request.method == "GET":
            data = User.objects.filter(id=id)
            element=data[0]
            print(element)
            element.user_name = request.GET.get('username')
            element.password = request.GET.get('password')
            print(element.user_name)
            temp=loader.get_template('top_qa_app/user_edit.html')
            if element.user_name =="" and element.password=="":
                return HttpResponse(temp.render({'username_msg':username_msg,'password_msg':username_msg,'contact':data} ,request))
            else:
                if element.user_name =="":
                    return HttpResponse(temp.render({'username_msg':username_msg,'contact':data} ,request))
                if element.password == "":
                    return HttpResponse(temp.render({'password_msg':username_msg,'contact':data} ,request))
            if request.GET.get('canedit') =='on':
                print(request.GET.get('canedit'))
                element.can_edit=True;
            else:
                print(request.GET.get('canedit'))
                element.can_edit=False;
            print (element.can_edit)
            if request.GET.get('canadd') =='on':
                element.can_add=True;
            else:
                element.can_add=False;

            element.save()
            return HttpResponseRedirect('/admin-login/select-user/')

def create_edit(request,id):
    msg="you don't have the authority, please login first"
    admin='not admin'
    template = loader.get_template('top_qa_app/user_login.html')
    if  User.objects.filter(id=str(request.session['id']), password=str(request.session['password']),is_admin=True).exists():
        temp=loader.get_template('top_qa_app/user_edit.html')
        contact = User.objects.filter(id=id)
        #admin
        if contact[0].id==request.session['id']:
            return HttpResponse(temp.render({'contact':contact} ,request))
        else:
            return HttpResponse(temp.render({'contact':contact,'not_admin':admin} ,request))
    else:
        return HttpResponseNotFound(template.render({'msg':msg}, request))

def user_create(request):
    msg="you don't have the authority, please login first"
    template = loader.get_template('top_qa_app/user_login.html')
    try:
        if User.objects.filter(id=str(request.session['id']), password=str(request.session['password'])).exists():
            temp=loader.get_template('top_qa_app/user_create.html')
            return HttpResponse(temp.render({},request))
    except:
        return HttpResponseNotFound(template.render({'msg':msg}, request))

def user_cancel(request):
    msg="you don't have the authority, please login first"
    template = loader.get_template('top_qa_app/user_login.html')
    try:
        if User.objects.filter(id=str(request.session['id']), password=str(request.session['password'])).exists():
            return HttpResponseRedirect('/admin-login/select-user/')
    except:
        return HttpResponseNotFound(template.render({'msg':msg}, request))

def newuser_save(request):
    msg="you don't have the authority, please login first"
    template = loader.get_template('top_qa_app/user_login.html')
    username_msg="Your username cannot be empty"
    password_msg="Your password canno be empty"
    if User.objects.filter(id=str(request.session['id']), password=str(request.session['password'])).exists():
        if request.method == "POST":
            user_name = request.POST.get('username')
            print(user_name)
            password = request.POST.get('password')
            temp=loader.get_template('top_qa_app/user_create.html')
            if user_name =="" and password =="":
                return HttpResponse(temp.render({'username_msg':username_msg,'password_msg':password_msg},request))
            else:
                if user_name =="":
                    return HttpResponse(temp.render({'username_msg':username_msg},request))
                elif password == "":
                    return HttpResponse(temp.render({'password_msg':username_msg},request))

            if request.POST.get('canedit') =='on':
                can_edit=True;
            else:
                can_edit=False;
            print (can_edit)

            if request.POST.get('canadd') =='on':
                can_add=True;
            else:
                can_add=False;
            print (can_add)

            if request.POST.get('isadmin') =='on':
                is_admin=True;
            else:
                is_admin=False;
            print (can_edit)
            print (is_admin)
            print (is_admin)
            new_contact=User(user_name=user_name,password=password,
                                can_edit=can_edit,can_add=can_add,
                                is_admin=is_admin)
            new_contact.save()
            return HttpResponseRedirect('/admin-login/select-user/')
        else:
            raise Http404('PAGE NOT FOUND')
    else:
        return HttpResponseNotFound(template.render({'msg':msg}, request))

#user login

def login_valid(request):
    if request.method =="POST":
        username=request.POST.get('login_name')
        password=request.POST.get('password')
        msg="Incorrect password or login name"
        if User.objects.filter(Q(user_name=(str(username)))&Q(password=password)).exists():
            id=User.objects.filter(Q(user_name=(str(username)))&Q(password=password)&Q(is_admin=True)).values('id')[0]['id']
            request.session['id']=id
            #remeber username
            #session[user_name
            #         password ]
            request.session['username']=username
            request.session['password']=password
            # user's session cookie will expire when the user's Web browser is closed.
            request.session.set_expiry(0)

            #login successfully,redirect to '/contact/'
            return HttpResponseRedirect('/contact/')

        else:
            #display error message
            return render(request,'top_qa_app/user_login.html', {'msg':msg})
    else:
        raise Http404('PAGE NOT FOUND')

def logout(request):
    try:
        del request.session['username']
        del request.session['password']
    except KeyError:
        pass
    return HttpResponse("You're logged out.")

def login(request):
    template=loader.get_template('top_qa_app/user_login.html')
    return HttpResponse(template.render({} ,request))

def contact(request):
    msg="you don't have the authority, please login first"
    template = loader.get_template('top_qa_app/user_login.html')
    try:
        if User.objects.filter(id=str(request.session['id']), password=str(request.session['password'])).exists():
            temp=loader.get_template('top_qa_app/contacts.html')
            return HttpResponse(temp.render({},request))
    except:
        return HttpResponseNotFound(template.render({'msg':msg}, request))



def result_contact(request):
    msg="you don't have the authority, please login fist"
    no_result='Your Search Not Found,Please Try Another Search'
    template = loader.get_template('top_qa_app/user_login.html')
    if User.objects.filter(id=str(request.session['id']), password=str(request.session['password'])).exists():
        user=request.GET.get('username')
        cat=request.GET.get('category')
        contact_list = Contact.objects.filter(Q(last_name__contains=(str(user)))|Q(first_name__contains=str(user))).order_by('last_name')[:10]
        print(contact_list)
        print (len(contact_list))
        if len(contact_list)==0:
            return render(request, 'top_qa_app/contact_result.html', {'no_result': no_result})
        else:
            paginator = Paginator(contact_list, 10) # Show 25 contacts per page
            page = request.GET.get('page')
            contacts = paginator.get_page(page)
            return render(request, 'top_qa_app/contact_result.html', {'contacts': contacts})
    else:
        return HttpResponseNotFound(template.render({'msg':msg}, request))

def result_contact_all(request):
    msg="you don't have the authority, please login fist"
    template = loader.get_template('top_qa_app/user_login.html')
    if User.objects.filter(id=str(request.session['id']), password=str(request.session['password'])).exists():
        if request.method == "GET":
            user=request.GET.get('username')
            cat=request.GET.get('category')
            contact_list = Contact.objects.all()[:10]
            paginator = Paginator(contact_list, 10) # Show 10 contacts per page
            page = request.GET.get('page')
            contacts = paginator.get_page(page)
            return render(request, 'top_qa_app/contact_result_all.html', {'contacts': contacts})
    else:
        return HttpResponseNotFound(template.render({'msg':msg}, request))

def create_contact(request):
    msg="you don't have the authority, please login first"
    template = loader.get_template('top_qa_app/user_login.html')
    login_name=request.session['username']
    try:
        if User.objects.filter(id=str(request.session['id']), password=str(request.session['password'])).exists():
            temp=loader.get_template('top_qa_app/contact_add.html')
            return HttpResponse(temp.render({'login_name':login_name},request))
    except:
        return HttpResponseNotFound(template.render({'msg':msg}, request))



def add(request):
    msg="you don't have the authority, please login first"
    error_msg="there are multiple fields required to be filled in"
    first_name_msg="first name cannot be empty"
    last_name_msg="last name cannot be empty"
    job_title_msg="job title cannot be empty"
    company_name_msg="company name cannot be empty"
    email_msg="email  cannot be empty"
    phone_msg="phone  cannot be empty"
    sourced_by_msg="sourced by field cannot be empty"
    source_type_msg="source type cannot be empty"
    template = loader.get_template('top_qa_app/user_login.html')
    if User.objects.filter(id=str(request.session['id']), password=str(request.session['password'])).exists():
        if request.method == "POST":
            first_name = request.POST.get('FirstName')
            last_name = request.POST.get('LastName')
            job_title = request.POST.get('JobTitle')
            company_name = request.POST.get('CompanyName')
            email = request.POST.get('Emaiil')
            phone = request.POST.get('Phone')
            category = request.POST.get('Category')
            contact_type = request.POST.get('ContactType')
            source = request.POST.get('Source')
            sourced_by = request.POST.get('SourcedBy')
            source_type = request.POST.get('SourceType')
            other_information = request.POST.get('OtherInformation')
            listed = request.POST.get('listed')
            check=[]
            if request.POST.get('DoNotEmail') =='on':
                doNotEmail=True;
            else:
                doNotEmail=False;

            if first_name =="":
                check.append(first_name_msg)
            if last_name=="":
                check.append(last_name_msg)
            if job_title=="":
                check.append(job_title_msg)
            if company_name=="":
                check.append(company_name_msg)
            if email=="":
                check.append(email_msg)
            if phone=="":
                check.append(phone_msg)
            if sourced_by=="":
                check.append(sourced_by_msg)
            if source_type =="":
                check.append(source_type_msg)
            if len(check) == 0:
                new_contact=Contact(first_name=first_name,last_name=last_name,
                                    job_title=job_title,company_name=company_name,
                                    email=email,phone=phone,category=category,
                                    contact_type=contact_type,source=source,
                                    sourced_by=sourced_by,source_type=source_type,
                                    other_information=other_information,
                                    listed=listed,doNotEmail=doNotEmail)
                new_contact.save()
                return HttpResponseRedirect('/contact/result_all/')
            else:
                if len(check)<=3:
                    t=loader.get_template('top_qa_app/contact_add.html')
                    return HttpResponse(t.render({'check_msg':check},request))
                else:
                    temp=loader.get_template('top_qa_app/contact_add.html')
                    return HttpResponse(temp.render({'error_msg':error_msg},request))

        else:
            raise Http404('PAGE NOT FOUND')
    else:
        return HttpResponseNotFound(template.render({'msg':msg}, request))

def edit_contact(request,id):
    msg="you don't have the authority, please login first"
    template = loader.get_template('top_qa_app/user_login.html')
    if  User.objects.filter(id=str(request.session['id']), password=str(request.session['password'])).exists():
        temp=loader.get_template('top_qa_app/contact_edit.html')
        data = Contact.objects.filter(id=id)

        return HttpResponse(temp.render({'contact':data},request))


#/contact/edit/, save,delete,update
def save(request,id):
    msg="you don't have the authority, please login first"

    template = loader.get_template('top_qa_app/user_login.html')
    if  User.objects.filter(id=str(request.session['id']), password=str(request.session['password'])).exists():
        if request.method == "GET":
            data = Contact.objects.filter(id=id)
            element=data[0]
            element.last_name = request.GET.get('LastName')
            print(element.last_name)
            element.job_title = request.GET.get('JobTitle')
            element.company_name = request.GET.get('CompanyName')
            element.email = request.GET.get('Emaiil')
            element.phone = request.GET.get('Phone')
            element.category = request.GET.get('Category')
            element.contact_type = request.GET.get('ContactType')
            element.source = request.GET.get('Source')
            element.sourced_by = request.GET.get('SourcedBy')
            element.source_type = request.GET.get('SourceType')
            element.other_information = request.GET.get('OtherInformation')
            element.listed = request.GET.get('listed')
            #if element.last_name=="" element.job_title element.company_name element.email element.phone element.category element.contact_type
            if request.GET.get('DoNotEmail') =='on':
                element.doNotEmail = True;
            else:
                element.doNotEmail = False;
            print(element.first_name)
            element.save()
            return HttpResponseRedirect('/contact/result_all/')

def delete(request,id):
    print('check')
    print(id)
    msg="you don't have the authority, please login first"
    template = loader.get_template('top_qa_app/user_login.html')
    try:
        if  User.objects.filter(id=str(request.session['id']), password=str(request.session['password'])).exists():
            if request.method == "GET":
                data = Contact.objects.filter(id=id)
                print(data)
                data.delete()
                return HttpResponseRedirect('/contact/result_all/')
    except:
        return HttpResponseNotFound(template.render({'msg':msg}, request))


def cancel(request):
    if request.method=="GET":
        print("this is cancel")
        return HttpResponseRedirect('/contact/result_all/')
