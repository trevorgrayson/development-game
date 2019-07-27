from players import Player


class Location:
    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
        self._mayor = kwargs.get('mayor')

    @property
    def mayor(self):
        return Player.find(self._mayor)
        
    def __str__(self):
        return self.name


LOCATIONS = {
    'iah': Location(name='texas', mayor='cack'),
    'lax': Location(name='los angeles', mayor='trevor'),
    'ewr': Location(name='new jersey', mayor='paul'),
    'jfk': Location(name='new york', mayor='brian'),
    'dca': Location(name='washington dc', mayor='tex')
}
