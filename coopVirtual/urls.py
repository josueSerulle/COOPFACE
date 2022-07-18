from django.urls import path

from .views import HomeView, LoginView, UserView, LoanApplicationView, LoanCalculateView

urlpatterns = [
    # home and auth urls
    path('',        HomeView.index,         name='coop_virtual'),
    path('login',   LoginView.loginView,    name ='login'),
    path('logout',  LoginView.logoutView,   name = "logout"),
    
    #user urls
    path('profile',         UserView.editView,      name = "profile"),
    path('profile/update',  UserView.updateView,    name = "profile_update"),
    
    #loan application urls
    
    path('loand_application',           LoanApplicationView.indexView,  name = "loand_application"),
    path('loand_application/datatable', LoanApplicationView.datatable,  name = "loand_application_datatable"),
    path('loand_application/create',    LoanApplicationView.createView, name = "loand_application_create"),
    path('loand_application/insert',    LoanApplicationView.insertView, name = "loan_application_insert"),
    
    #loan calculate urls
    
    path('loan_calculate',              LoanCalculateView.indexView,            name = "loan_calculate_index"),
    path('loan_calculate/calculate',    LoanCalculateView.loandCalculateView,   name = "loan_calculate"),
]
