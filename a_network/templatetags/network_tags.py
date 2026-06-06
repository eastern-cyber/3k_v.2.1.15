from django import template
from ..models import Follow

register = template.Library()

@register.filter
def is_following(user, this_user):
    # Safe check for anonymous users
    if not user or not user.is_authenticated:
        return False
    
    # Optional: Check if this_user exists
    if not this_user:
        return False
        
    # If you also need to check if this_user is authenticated:
    # if not this_user.is_authenticated:
    #     return False
    
    try:
        return Follow.objects.filter(follower=user, following=this_user).exists()
    except Exception:
        return False
