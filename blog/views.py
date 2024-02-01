from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Blog
from .forms import BlogForm
import json
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def author():
    return HttpResponse("<p>This is app was made by <strong>Lynx Pardelle</strong>, you can watch my work on <a href='https://lynxpardelle.com' target='_blank' >lynxpardelle.com</a><p>")


def getBlogs(request, option=None, id=None, search=None):
    errStatus = 500
    try:
        # Read
        if request.method == 'GET':
            if option == 'all' or option == None:
                blogs = Blog.objects.all()
                blogs = list(blogs.values())
                blogs = list(map(lambda blog: {
                    'id': blog['id'],
                    'title': blog['title'],
                    'sub_title': blog['sub_title'],
                    'content': blog['content'],
                    'author': User.objects.get(id=blog['author_id']),
                    'date': blog['date'],
                    'image': blog['image'],
                }, blogs)
                )
                print('blogs:')
                print(blogs)
                return render(request, 'blogs.html', {'blogs': blogs})
            elif option == 'one':
                if not id:
                    errStatus = 400
                    raise Exception('Missing id')
                print(id)
                blog = Blog.objects.get(id=id)
                print(blog)
                return render(request, 'blog.html', {'blog': blog})
            elif option == 'search':
                blogs = Blog.objects.filter(title__icontains=search)
                return render(request, 'blogs.html', {'blogs': list(blogs.values())})
            else:
                raise Exception('Invalid option')
        else:
            return JsonResponse({'message': 'Invalid method:' + request.method})
    except Exception as e:
        print('An exception occurred')
        return render(request, 'error.html', {
            'status': errStatus,
            'statusMessage': 'Error',
            'data': {
                'method': request.method,
                'path': request.path,
                'body': request.body.decode('utf-8'),
                'headers': dict(request.headers),
            },
            'message': "Error: %s" % e})


@login_required(login_url='/accounts/login')
def manipulateBlog(request, option=None, id=None, search=None):
    errStatus = 500
    print('request.method:', request.method)
    print('request.headers:', request.headers)
    print('request.path:', request.path)
    print('request.user:', request.user)
    print('option:', option)
    print('id:', id)
    print('search:', search)
    try:
        # Create
        if request.method == 'POST':
            form = BlogForm(request.POST, request.FILES)
            if form.is_valid():
                title = form.cleaned_data['title']
                sub_title = form.cleaned_data['sub_title']
                content = form.cleaned_data['content']
                print('request.POST:', request.POST)
                print('form.cleaned_data:', form.cleaned_data)
                print('request.FILES:', request.FILES)
                if form.cleaned_data.get('image'):
                    image = form.cleaned_data.get('image')
                    print('image:', image)
                elif request.FILES.get('image'):
                    image = request.FILES.get('image')
                    print('image:', image)
                elif request.POST.get('image'):
                    image = request.POST.get('image')
                    print('image:', image)
                else:
                    image = None
                    print('No image')
                author = request.user
                if not author:
                    author = User.objects.get(id=1)
                if not title or not sub_title or not content or not author:
                    errStatus = 400
                    raise Exception(
                        'Invalid form: missing fields or invalid data option for fields (title, sub_title, content, image, author) sended: ' + str(form.cleaned_data))
                if not id:
                    blog = Blog(title=title, sub_title=sub_title,
                                content=content, image=image,  author=author)
                else:
                    blog = Blog.objects.get(id=id)
                    blog.title = title
                    blog.sub_title = sub_title
                    blog.content = content
                    blog.image = image or blog.image
                    blog.author = author
                blog.save()
                print(blog)
                return render(request, 'blog.html', {'blog': blog, 'messages': ['Blog created successfully']})
            else:
                errStatus = 400
                raise Exception('Invalid form')
        # Read
        elif request.method == 'GET':
            if option == 'all' or option == None:
                blogs = Blog.objects.all()
                print('blogs:')
                print(list(blogs.values()))
                return render(request, 'blogs.html', {'blogs': list(blogs.values())})
            elif option == 'one':
                if not id:
                    errStatus = 400
                    raise Exception('Missing id')
                print(id)
                blog = Blog.objects.get(id=id)
                print(blog)
                return render(request, 'blog.html', {'blog': blog})
            elif option == 'user':
                user = request.user
                blogs = Blog.objects.filter(author=user)
                return render(request, 'blogs.html', {'blogs': list(blogs.values())})
            elif option == 'search':
                blogs = Blog.objects.filter(title__icontains=search)
                return render(request, 'blogs.html', {'blogs': list(blogs.values())})
            elif option == 'create':
                form = BlogForm()
                return render(request, 'blog_edit.html', {'form': form, 'option': 'create'})
            elif option == 'update':
                if not id:
                    errStatus = 400
                    raise Exception('Missing id')
                blog = Blog.objects.get(id=id)
                print(blog)
                form = BlogForm(initial={
                    'title': blog.title,
                    'sub_title': blog.sub_title,
                    'content': blog.content,
                    'image': blog.image,
                })
                return render(request, 'blog_edit.html', {'form': form, 'option': 'update', 'id': id})
            else:
                raise Exception('Invalid option')
        # Update
        elif request.method == 'PUT':
            data = request.body.decode('utf-8')
            print('data:')
            print(data)
            if not data:
                errStatus = 400
                raise Exception('Missing data')
            id = data['id']
            if not id:
                errStatus = 400
                raise Exception('Missing id')
            blog = Blog.objects.get(id=id)
            if not blog:
                errStatus = 404
                raise Exception('Blog not found')
            title = data['title'] | blog.title
            sub_title = data['sub_title'] | blog.sub_title
            content = data['content'] | blog.content
            image = data['image'] | blog.image
            blog.title = title
            blog.sub_title = sub_title
            blog.content = content
            blog.image = image
            blog.save()
            print(blog)
            return render(request, 'blog.html', {'blog': blog, 'messages': ['Blog updated successfully']})
        # Delete
        elif request.method == 'DELETE':
            if not id:
                errStatus = 400
                raise Exception('Missing id')
            blog = Blog.objects.get(id=id)
            if not blog:
                errStatus = 404
                raise Exception('Blog not found')
            blog.delete()
            return JsonResponse({'message': 'Blog deleted successfully'})
        elif request.method == 'OPTIONS':
            return JsonResponse({'message': 'Options'})
        else:
            return JsonResponse({'message': 'Invalid method' + request.method})
    except Exception as e:
        print('An exception occurred')
        return render(request, 'error.html', {
            'status': errStatus,
            'statusMessage': 'Error',
            'data': {
                'method': request.method,
                'path': request.path,
                'headers': dict(request.headers),
            },
            'message': "Error: %s" % e})


def uploadImage(request):
    errStatus = 500
    try:
        if request.method == 'POST':
            image = request.FILES['image']
            id = request.POST.get('id')
            if not id:
                errStatus = 400
                raise Exception('Missing id')
            blog = Blog.objects.get(id=id)
            if not blog:
                errStatus = 404
                raise Exception('Blog not found')
            blog.image = image
            blog.save()
            return JsonResponse({'message': 'Image uploaded successfully'})
        else:
            raise Exception('Invalid method')
    except Exception as e:
        print('An exception occurred')
        return render(request, 'core/error.html', {
            'status': errStatus,
            'statusMessage': 'Error',
            'data': {
                'method': request.method,
                'path': request.path,
                'body': request.body.decode('utf-8'),
                'headers': dict(request.headers),
            },
            'message': "Error: %s" % e})
