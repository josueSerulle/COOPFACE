from unicodedata import name
from django.urls import path

from admin.views import HomeView, LoginView, LoanApplicationView

urlpatterns = [
    # home and auth urls
    path('',        HomeView.index,         name='admin'),
    path('login',   LoginView.loginView,    name ='login_admin'),
    path('logout',  LoginView.logoutView,   name = "logout_admin"),
    
    # Loan Application Urls
    path('loan_application',                            LoanApplicationView.indexView,  name = "loan_application_admin"),
    path('loan_application/datatable',                  LoanApplicationView.datatable,  name = "loan_application_datatable"),
    path('loan_form/<int:loanApplicationId>',           LoanApplicationView.formView,   name = "loan_form_admin"),
    path('loan_form/insert/<int:loanApplicationId>',    LoanApplicationView.insertView, name = "loand_form_insert_admin"),
]
