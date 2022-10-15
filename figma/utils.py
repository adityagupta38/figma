from .models import User


def user_registered(uname):
    try:
        User.objects.get(username=uname)
        return True
    except:
        return False


def user_authenticated(uname,pwd):
    user = User.objects.get(username=uname)
    password = user.password
    if password == pwd:
        return True
    else:
        return False

