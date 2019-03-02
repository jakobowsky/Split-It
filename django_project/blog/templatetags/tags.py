from django import template
from promotion.models import Brand, Promotion, Category
register = template.Library()


# @register.inclusion_tag('blog/base.html', takes_context=True)
# def best_promotions(context):
#     promotions = Promotion.objects.all()
#     return {
#         'proms': context[promotions]
#     }
#     # return {

#     # }
#     #return {context[promotions]}
#     return context#{'promotions2': context[promotions]}

@register.simple_tag
def best_promos():
        return Promotion.objects.all()[:7]


@register.simple_tag
def best_brands():
        return Brand.objects.all()[:7]


@register.simple_tag
def best_categories():
        return Category.objects.all()[:7]
