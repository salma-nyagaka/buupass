from carryforme.apps.account.models import User


def create_superuser(credentials):
    user, created = User.objects.get_or_create(
        email=credentials['email'], defaults={
            'is_active': True, 'is_staff': True, 'is_superuser': True})
    if created:
        user.set_password(credentials['password'])
        user.save()
        msg = 'Superuser - %(email)s/%(password)s' % credentials
    else:
        msg = 'Superuser already exists - %(email)s' % credentials
    return msg
