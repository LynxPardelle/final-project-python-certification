from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .forms import MessageForm
from .models import Message
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def author():
    return HttpResponse("<p>This is app was made by <strong>Lynx Pardelle</strong>, you can watch my work on <a href='https://lynxpardelle.com' target='_blank' >lynxpardelle.com</a><p>")


@login_required(login_url='/accounts/login')
def manageMessages(request):
    errStatus = 500
    try:
        # Create
        if request.method == 'POST':
            form = MessageForm(request.POST, request.FILES)
            if form.is_valid():
                content = form.cleaned_data['content']
                author = request.user
                if not author:
                    author = User.objects.get(id=1)
                if not content or not author:
                    errStatus = 400
                    raise Exception(
                        'Invalid form: missing fields or invalid data type for fields (content, author) sended: ' + str(form.cleaned_data))
                message = Message(content=content, author=author)
                message.save()
                messages = Message.objects.all()
                messages = messages.order_by('date')
                messages = list(messages.values())
                for message in messages:
                    message['author'] = User.objects.get(
                        id=message['author_id'])
                form = MessageForm()
                return render(request, 'messages.html', {'form': form, 'chat': messages})
            else:
                errStatus = 400
                raise Exception('Invalid form')
        # Read
        elif request.method == 'GET':
            type = request.GET.get('type')
            if type == 'all' or type == None:
                messages = Message.objects.all()
                messages = messages.order_by('-date')
                messages = list(messages.values())
                for message in messages:
                    message['author'] = User.objects.get(
                        id=message['author_id'])
                form = MessageForm()
                return render(request, 'messages.html', {'form': form, 'chat': messages})
            # elif type == 'one':
                # id = request.GET.get('id')
                # if not id:
                #   errStatus = 400
                #   raise Exception('Missing id')
                # message = Message.objects.get(id=id)
                # return render(request, 'messages/message.html', {'message': message})
            # elif type == 'user':
                # user = request.user
                # messages = Message.objects.filter(author=user)
                # return render(request, 'messages/messages.html', {'messages': list(messages.values())})
            # elif type == 'search':
                # search = request.GET.get('search')
                # messages = Message.objects.filter(content__icontains=search)
                # return render(request, 'messages/messages.html', {'messages': list(messages.values())})
            # elif type == 'create':
                # form = MessageForm()
                # return render(request, 'messages/form.html', {'form': form, 'type': 'create'})
            # elif type == 'update':
                # id = request.GET.get('id')
                # if not id:
                # errStatus = 400
                # raise Exception('Missing id')
                # message = Message.objects.get(id=id)
                # form = MessageForm(instance=message)
                # return render(request, 'messages/form.html', {'form': form, 'type': 'update', 'id': id})
            else:
                raise Exception('Invalid type')
    except Exception as e:
        return JsonResponse({'message': str(e)}, status=errStatus)
