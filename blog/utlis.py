from api.models import Like




def post_like(post):
    return Like.objects.filter(post=post).count()