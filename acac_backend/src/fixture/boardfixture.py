import factory
import random
from fixture.userfixture import UserProfileFactory
from fixture.facultyfixture import FacultyFactory

COLOUR = ["yellow", "black", "purple", "red", "orange", "green", '#084594', '#2171b5', '#4292c6', '#6baed6', '#9ecae1',
          '#c6dbef', '#deebf7', '#f7fbff'
          ]
SKIN = [
    'white-skin', 'black-skin', 'cyan-skin', 'mdb-skin', 'deep-purple-skin', 'navy-blue-skin', 'pink-skin',
    'indigo-skin', 'light-blue-skin', 'grey-skin']


class BoardFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'main.Board'
        django_get_or_create = ('name', 'description', 'secretary', 'custom_html', 'slug', 'is_active', 'year',)

    name = factory.Faker('sentence', nb_words=4)
    description = factory.Faker('sentence', nb_words=30)
    cover = factory.django.ImageField(color=random.choice(COLOUR))
    skin = random.choice(SKIN)
    secretary = factory.SubFactory(UserProfileFactory)
    vice_president = factory.SubFactory(UserProfileFactory)
    president = factory.SubFactory(FacultyFactory)
    # gallery = models.ForeignKey(Gallery, blank=True, null=True, on_delete=models.SET_NULL,
    custom_html = factory.Faker('sentence', nb_words=20)
    slug = factory.Sequence(lambda n: 'board-%d' % n)
    is_active = True
    year = random.randint(2009, 2018)
