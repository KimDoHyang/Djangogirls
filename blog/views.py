import os
from .models import Post

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
# Create your views here.
from django.utils import timezone



def post_list(request):
    posts = Post.objects.order_by('created_date')
    #템플릿을 가져온다
    # template = loader.get_template('blog/post_list.html')
    #해당 템플을 렌더링

    context = {
        'posts': posts
            # '<ul>' + ''.join([f'<li>{post.title}</li>' for post in posts]) + '</ul>',
    }
    #context = {'pokemon' : random.choice(['피카츄','파이리','꼬부기'])}
    # content = template.render(context, request)




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
    # return HttpResponse(content
        # '<html>'
        # '<body>'
        # '<h1>Post List</h1>'
        # '<p>{}</p>'
        # '</body>'
        # '</html>'.format(
        #     # 날짜&시간 객체가 가진 정보를 문자열로 변환
        #     current_time.strftime('%Y, %m, %d<br>%H:%M:%S')
        # )
    # )
    #render 함수
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

