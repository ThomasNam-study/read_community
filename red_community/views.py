from django.http import HttpResponse

from fcuser.models import Fcuser


def home(request):
    user_id = request.session.get('user')

    if user_id:
        #fcuser = Fcuser.objects.get(user_id)

        return HttpResponse(user_id)

    return HttpResponse('Home')