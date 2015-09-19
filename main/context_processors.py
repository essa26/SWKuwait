from main.models import Log
from main.forms import Blood


def main_menu(request):

    context = {}

    postform = CreatePost

    context['postform'] = postform

    return {'postform': postform}


