from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from blogs.models import BlogPost
from rest_framework import viewsets
from rest_framework import permissions
from blogs.serializer import UserSerializer, BlogSerializer
from .forms import BlogUploadForm
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import BlogPost
import datetime
from django.views.decorators.csrf import csrf_exempt


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class BlogViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [permissions.IsAuthenticated]

@csrf_exempt
def createblog(request):
    if request.method == 'POST':
        print ("POST")
        if request.POST.get('key') == 'update':
            id = request.POST.get('id')
            print("******************")
            comments = request.POST.get('comments')
            t = BlogPost.objects.get(id=id)
            t.comments = comments  # change field
            t.save() # this will update only
        else:

            title = request.POST.get('title')
            content = request.POST.get('body')
            image = request.POST.get('image')
            now_obj = datetime.datetime.now()
            now = now_obj.strftime("%Y-%m-%d %H:%M")
            blog = BlogPost(title=title, body=content,image=image,date_published=now,date_updated=now)
            blog.save()
    elif request.method == "PUT":
        print("PUT",request)
        
        # blog_update = BloPost.objects.filter(id=id).update(comments=comments)
        # blog_update.save()
    return JsonResponse({"result":"success"})
    # return render(request, 'registration/home.html', {'data': "success"})
  

    # return JsonResponse({"success": "success"}, status=200)
