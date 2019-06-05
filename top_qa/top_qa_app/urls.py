from django.urls import path

from . import views

urlpatterns = [

    path('contact/',views.contact,name='contact'),
    path('contact/result/' ,views.result_contact,name='result_contact'),
    path('contact/result_all/' ,views.result_contact_all,name='result_contact_all'),
    path('contact/new/',views.create_contact,name='create_contact'),
    path('contact/add/',views.add,name='add'),
    path('contact/edit/<int:id>/',views.edit_contact,name='edit_contact'),
    path('login/',views.login_valid,name='login_valid'),
    path('admin-login/valid',views.admin_valid,name='admin_valid'),
    path('admin-login/select-user/',views.user_select,name='user_select'),
    path('admin-login/',views.create_admin,name='create_admin'),
    path('admin-login/select-user/',views.user_cancel,name='user_cancel'),
    path('admin-login/edit_user/<int:id>/',views.create_edit,name='create_edit'),
    path('contact/user_delete/<int:id>/',views.user_delete,name='user_delete'),
    path('contact/user_save/<int:id>/',views.user_save,name='user_save'),
    path('contact/save/<int:id>/',views.save,name='save'),
    path('contact/delete/<int:id>/',views.delete,name='delete'),
    path('contact/cancel/',views.cancel,name='cancel'),
    path('admin-login/user_create/',views.user_create,name='user_create'),
    path('admin-login/user_save/',views.newuser_save,name='newuser_save'),
    #path('login/%20/login/',views.user_login_error)
    path('', views.login, name='login'),

]
