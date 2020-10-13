from django import template
from comments.forms import CommentForm

register = template.Library()

@register.inclusion_tag('comments/inclusions/_form.html', takes_context=True)
def show_comment_form(context, post, form=None):
    if form is None:
        form = CommentForm()
    return {
        # 将模板变量 form post 传入模板 _form.html 中
        'form' : form,
        'post' : post,
    }

@register.inclusion_tag('comments/inclusions/_list.html', takes_context=True)
def show_comments(context, post):
    comment_list = post.comment_set.all().order_by('-created_time')
    comment_count = comment_list.count()
    return {
        'comment_count' : comment_count,
        'comment_list' : comment_list,
    }