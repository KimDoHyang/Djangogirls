from django.conf.urls import url
"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.contrib import admin
from django.conf.urls import url
from blog import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.post_list),
    # url(r'^posts/\d+/$', views.post_detail),
    url(r'^posts/(?P<pk>\d+)/$', views.post_detail)
    #위와 같은 경우, 그룹화를 시키게 되면 이 그룹화 한 것이 두번재 인수로서 전달되도록 한다.
    # 이 경우 request가 오면 post_detail(request, pk=<요청된 값>)으로 전달된다.

    # /posts/1/, /posts/777/, ...  <- 이 경우에 해당하는 정규표현식 패턴(/로 끝나야함)이
    # blog.views.post_detail 여기로 전달되도록 설정 및 뷰 함수 구현.
    # -> 이 뷰는 Post Detail이라는 문자열을 HttpResponse를 사용해 리턴
]
