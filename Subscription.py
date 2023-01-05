from django.shortcuts import get_object_or_404

from pub.models import MySubscription, Post


def subscribe(user, pk) -> bool:
    post = get_object_or_404(Post, id=pk)
    MySubscription.objects.create(user=user, post=post)
    return True

def unsubscribe_post(request, pk) -> bool:
    post = get_object_or_404(Post, pk=pk)
    MySubscription.objects.delete(user=request.user, post=post)
    return True