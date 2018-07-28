from django.shortcuts import render

def post_list(request):
    print('post list is called')
    return render(request, 'blog/post_list.html', {})
