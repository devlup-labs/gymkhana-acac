import factory
import random

COLOUR = ["yellow", "black", "purple", "red", "orange", "green", '#084594', '#2171b5', '#4292c6', '#6baed6', '#9ecae1',
          '#c6dbef', '#deebf7', '#f7fbff'
          ]


class FacultyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'main.Faculty'

    name = factory.Faker('sentence', nb_words=2)
    email = factory.Faker('email')
    phone = random.randint(6000000000, 9999999999)
    avatar = factory.django.ImageField(color=random.choice(COLOUR))
    cover = factory.django.ImageField(color=random.choice(COLOUR))
