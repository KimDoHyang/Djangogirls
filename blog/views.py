import os

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
from django.utils import timezone


def post_list(request):
    template = loader.get_template('blog/post_list.html')
    context = {}
    content = template.render(context, request)


    # views_file_path = os.path.abspath(__file__)
    # blog_app_path = os.path.dirname(views_file_path)
    # app_dir = os.path.dirname(blog_app_path)
    # templates_path = os.path.join(app_dir, 'templates', 'blog', 'post_list.html')
    #
    # with open(templates_path, 'rt') as f:
    #     content = f.read()

    # #or 파일객체 직접 사용 후 close
    # f = open(templates_path, 'rt')
    # content = f.read()
    # f.close()
    #
    # #파일 객체 변수에 할당하지 않고 사용
    # content = open(templates_path, 'rt').read()
    """
    
    :param request: 실제 HTTP요청에 대한 정보를 가진 객체
    :return:
    """
    # 현재 지역에 맞는 날짜&시간 객체 할당
    # current_time = timezone.now()
    return HttpResponse(content
        # '<html>'
        # '<body>'
        # '<h1>Post List</h1>'
        # '<p>{}</p>'
        # '</body>'
        # '</html>'.format(
        #     # 날짜&시간 객체가 가진 정보를 문자열로 변환
        #     current_time.strftime('%Y, %m, %d<br>%H:%M:%S')
        # )
    )