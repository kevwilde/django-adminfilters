from project.models import Continent
from project.models import Language
from project.models import Country


def populate_db():
    if Country.objects.count() > 0:
        return
    europe = Continent(description='Europe')
    europe.save()
    america = Continent(description='America')
    america.save()
    english = Language(description='English')
    english.save()
    german = Language(description='German')
    german.save()
    french = Language(description='French')
    french.save()
    italian = Language(description='Italian')
    italian.save()
    countries = [
        ('Canada', america, [english, french, ]),
        ('France', europe, [french, ]),
        ('Switzerland', europe, [italian, french, german, ]),
        ('Italy', europe, [italian, ]),
        ('Germany', europe, [german, ]),
        ('England', europe, [english, ]),
        ('USA', america, [english, ]),
    ]
    for (description, continent, languages) in countries:
        obj = Country(description=description, continent=continent)
        obj.save()
        obj.languages = languages
        obj.save()
