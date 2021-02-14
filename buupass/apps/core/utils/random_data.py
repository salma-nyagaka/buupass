import unicodedata

from faker import Factory

from carryforme.apps.account.models import Address, User

fake = Factory.create()


def create_address():
    address = Address.objects.create(
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        street_address_1=fake.street_address(),
        city=fake.city(),
        postal_code=fake.postcode(),
        country=fake.country_code())
    return address


def create_fake_user():
    address = create_address()
    email = get_email(address.first_name, address.last_name)

    user = User.objects.create_user(username=address.first_name, email=email,
                                    password='password')

    user.addresses.add(address)
    user.is_active = True
    user.save()
    return user


def get_email(first_name, last_name):
    _first = unicodedata.normalize('NFD', first_name).encode('ascii', 'ignore')
    _last = unicodedata.normalize('NFD', last_name).encode('ascii', 'ignore')
    return '%s.%s@example.com' % (
        _first.lower().decode('utf-8'), _last.lower().decode('utf-8'))


def create_users(how_many=10):
    for dummy in range(how_many):
        user = create_fake_user()
        yield 'User: %s' % (user.email,)
