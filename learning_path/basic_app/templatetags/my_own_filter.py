from django import template

register = template.library()

#create decorator
@register.filter(name='cut') 

def cut(value,args):

    """
    This cut all values of argus string 

    """ 
    return value.replace(args,"")

#register.filter('cut',cut)