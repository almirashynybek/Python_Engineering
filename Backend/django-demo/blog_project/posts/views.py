from django.http import JsonResponse

from .models import Post

def index(request):

    first_post = Post.objects.all().first()

    return JsonResponse({'message': 'Hello, world!', 'title': first_post.title, 'body': first_post.body})



