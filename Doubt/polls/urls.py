from polls.views import *
from django.urls import path
from . import views
urlpatterns = [

	path('student/',views.StudentAPI, name='student'),
	path('doubt/',views.DoubtAPI, name='doubt')

]
app_name = 'polls'