from django import  template
register = template.Library()

@register.simple_tag
def get_parte_discount(quantity, price, discount):
    return quantity * price * (100 - discount) / 100;