from django.urls import path
import MainApp.views as views

app_name = 'main'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('index/', views.index, name='index'),
    path('password/front/<str:username>/<int:role>/', views.forget_password_set_role, name='forget_password_set_role'),
    path('password/<str:username>/', views.forget_password, name='forget_password'),
    path('password/question/<str:username>/', views.forget_password_question, name='forget_password_question'),
    path('password/email/set/<str:token>/', views.set_new_password_email, name='set_new_password_email'),
    path('res/html/<path:path>/', views.render_static_html, name='res_render_html'),
    path('question/set/<str:username>/', views.set_user_question, name='set_new_question')
]
