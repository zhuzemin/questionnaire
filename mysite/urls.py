from django.conf.urls import *
from mysite.views import current_datetime
from django.contrib import admin
from mysite.books.views import search
from mysite.contact.views import contact
from mysite.exam.views import *
admin.autodiscover()

urlpatterns = [
    url('^time/$', current_datetime),
    url('^search/$', search),
    url(r'^admin/', admin.site.urls),
    url('^contact/$', contact),
    url('^exam/$', examView),
    url('^import/$', importView),
    url('^generate/$', generate),
    url('^ajax/exam_info/$', exam_info),
    url('^ajax/post_answer/$', post_answer),
]
