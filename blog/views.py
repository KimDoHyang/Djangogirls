import os
from .models import Post

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render
# Create your views here.
from django.utils import timezone
import re


# def post_detail(request):
#     m = re.search(r'/posts/(?P<pk>\d+)/$', request.path)
#     pk = m.group('pk')
def post_detail(request, pk):
    post = Post.objects.get(id=pk)
    context = {
        'post': post,
    }
    # return HttpResponse(post.title)
    return render(
        request=request,
        template_name='blog/post_detail.html',
        context=context,
    )


def post_list(request):
    posts = Post.objects.order_by('created_date')
    # 템플릿을 가져온다
    # template = loader.get_template('blog/post_list.html')
    #해당 템플을 렌더링

    context = {
        'posts': posts
        # '<ul>' + ''.join([f'<li>{post.title}</li>' for post in posts]) + '</ul>',
    }
    # context = {'pokemon' : random.choice(['피카츄','파이리','꼬부기'])}
    # content = template.render(context, request)

    # views_file_path = os.path.abspath(__file__)
    # blog_app_path = os.path.dirname(views_file_path)
    # app_dir = os.path.dirname(blog_app_path)
    # templates_path = os.path.join(app_dir, 'templates', 'blog', 'post_list.html')

    # with open(templates_path, 'rt') as f:
    # content = f.read()

    # #or 파일객체 직접 사용 후 close
    # f = open(templates_path, 'rt')
    # content = f.read()
    # f.close()

    # #파일 객체 변수에 할당하지 않고 사용
    # content = open(templates_path, 'rt').read()
    """
    :param request: 실제 HTTP요청에 대한 정보를 가진 객체. urls.py(urlreslover에 등록된 패턴에 들어온 게 일치할 경우
    여기에서 받아 실행한다.
    :return:
    """
    # 현재 지역에 맞는 날짜&시간 객체 할당
    # current_time = timezone.now()
    # return HttpResponse(content
        # '<html>'
        # '<body>'
        # '<h1>Post List</h1>'
        # '<p>{}</p>'
        # '</body>'
        # '</html>'.format(
        #     # 날짜&시간 객체가 가진 정보를 문자열로 변환
        #     current_time.strftime('%Y, %m, %d<br>%H:%M:%S')

    # render 함수
    # 1번째 인수로 자신의 view의 첫번째 매개변수인 request를 전달
    # 2번째 인수로 템플릿 파일의 경로를 전달
    # 3번째 인수(선택)로 dict를 전달
    # > 템플릿 파일의 경로에 있는 HTML을 가져와서 {{변수}}와 같은 부분들에 동적으로 문자열을 생성
    # 생성된 결과를 HttpResponse로 돌려줌, 브라우저는 해당 결과를 받아 사용자에게 보여주게 됨.
    # loader.get_template > template.render > HttpResponse(content) == render함수
    # return render(request, 'blog/post_list.html', context)
    return render(
        request=request,
        template_name='blog/post_list.html',
        context=context,
    )


# 1. 사용자가 브라우저의 주소표시줄을 사용해서(또는 하이퍼링크) 특정 주소에 요청
# 2. 요청을 받은 서버는 해당 요청을 "어디선가" 동적으로 처리
# 3. "어디선가" 처리된 결과를 서버가 사용자에게 반환
# 4. 사용자는 요청한 결과를 브라우저에서 보게됨
#
#
# ~/projects/
#     django/
#         djangogirls-tutorial/
#             git설정 <- git remote add 주소를 git@ 으로 시작하는 주소로 추가
#             .gitignore 설정
#                 git, linux, macos, python, pycharm+all, jupyternotebook, django
#
#             pyenv virtualenv 3.6.6 fc-djangogirls
#             pyenv local fc-djangogirls
#
# PyCharm설치 (Pro, Community무관) -> djangogirls-tutorial/ 폴더를 열어주기\
# pycharm압축 푼 폴더로 이동 -> bin/폴더 이동 -> ./pycharm.sh로 실행
#
# ------------------------------
#
# PyCharm Interpreter
#
# Ubuntu
#     ~/.pyenv/versions/<가상환경명>/bin/python
# macOS
#     /usr/local/var/pyenv/versions/<가상환경명>/bin/python
#
# ----------------------------------
#
# 평문 -(특정키로 암호화)->   암호문 전송   -> (특정키로 복호화)-평문
#
# 개인키: id_rsa
# 공개키: id_rsa.pub
#
# 평문 -(개인키로 암호화)->  암호문 전송  -> (공개키로 복호화)-평문
#
#
# Bob / Alice
#
# Bob의 개인키
# Bob의 공개키
#
# Alice의 개인키
# Alice의 공개키
#
# --------------------------
#
# Bob이 Alice에게 통신요청
#
# 1. Bob이 Alice에게 공개키 요청
# 2. Bob이 평문을 Alice의 공개키로 암호화해서 전송
# 3. Alice는 Bob이 보낸 암호문을 자신의 개인키로 복호화
#
#
# -------------------------
#
# git 저장소에 명령을 보내기 전에, 특정 값을 자신의 개인키로 암호화
# GitHub서버에서는 받은 요청을 내가 올려놓은 공개키로 복호화 시도
# 성공한다면 -> 공개키를 올린 사람 본인을 입증할 수 있음
# username/password 물어보지 않고 명령 실행
#
# -------------------------
#
# http://(어떤도메인)/posts/
#     -> 블로그의 모든 Post목록
#
# http://(어떤도메인)/posts/1/
#     -> 1번 Post를 보여줌
#
#
# --------------------------
#
# Django project structure
#
# djangogirls-tutorial/ <-    프로젝트 폴더
#     app/                <-    Django폴더
#         config/            <-    Django설정 패키지
#             settings.py    <-    Django설정 모듈
#         manage.py        <-    Django유틸리티 모듈
#     .git
#     .gitignore
#     .python-version
#
#
# -------------------------
#
# MVC모델                Django
#
# Model        <->        Model (models.py)
# View        <->        Template
# Controller    <->        View (views.py)
#
# -------------------------
#
# runserver (웹 서버)
# Django application
#     urlresolver (config.urls)
#
#
# 127.0.0.1:8000 -> runserver -> urlresolver
#     -> r'^$'와 매치
#     -> 해당 요청을 blog.views.post_list에 보냄
#     -> 함수에서는 받은 요청을 처리한 결과를 리턴
#     -> 리턴된 결과는 브라우저에 표시


def post_create(request):
    if request.method == 'POST':
        # POST요청이 올 경우 새 글을 작성하고 원하는 페이지로 돌아가도록.
        title = request.POST['title']
        # request.POST > 딕셔너리
        text = request.POST['text']

        # objects.create() 메서드를 사용해서 새 POST 객체를 생성, DB에 저장.
        # create() 실행의 반환값은 'post'변수에 할당.
        # title, text는 request.POST에서 가져온 것.
        # author는 request.user
        # 리턴하는 결과는 같은 문자열이지만, 문자열을 생성할때 만들어진 Post객체('post'변수)의 title, text속성 사용.
        post = Post.objects.create(
            author=request.user,
            title=title,
            text=text,
        )
        next_path = '/blog-posts/'
        return HttpResponseRedirect(next_path)
        # return HttpResponse(f'제목: {title}<br>내용: {text}')
    else:
        return render(request, 'blog/post_create.html')
        # 전달할게 없으므로 그냥 context없이 전달해서 render
    '''
    Template : blog/post_create.html
    URL : /post/create/
    URL Name : post-create

    템플릿에 하나의 <form요소>를 구현
    input[name="title"]
    button[type="submit"]

    post_create.html을 보여주는 링크를 base.html에 구현
    {url} 태그를 사용할것.

    :param request:
    :return:
    '''
