from django import template

register = template.Library()


@register.filter(name='user_belongs_to_group')
def user_belongs_to_group(user, group_name):
    return user.groups.filter(name=group_name).exists()
