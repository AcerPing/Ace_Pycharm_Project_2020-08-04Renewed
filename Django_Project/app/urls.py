"""account_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

'''
Regular Expression:
^ : 以什麼為開頭
$ : 以什麼為結尾
. : 任意字元
+ : 一個字元以上
? : 是否有某個字元出現都可以
\d : 數字
() : 擷取符合的pattern
'''
from django.conf.urls import url
from django.contrib import admin
from app import views

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    # #url(r'^hello/', 'app.views.hello'),
    # url(r'^hello/', views.hello),
    url(r'^$', views.frontpage),
    url(r'^settings$', views.settings),
    url(r'^add_category$', views.addCategory),
    url(r'^delete_category/(?P<category>\w+)', views.deleteCategory),
    url(r'^add_record$', views.addRecord),
    url(r'^delete_record$', views.deleteRecord),
    ]
