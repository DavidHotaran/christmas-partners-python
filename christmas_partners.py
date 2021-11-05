import random

class Person:
    '''Class container which describes name and spouse (optional) of a person'''

    def __init__(self, name, spouse=None):
        self.name = name
        self.spouse = spouse

    def __repr__(self):
        return(f'(Person name={self.name} spouse={self.spouse})')


people = [
    Person('david', 'lydia'),
    Person('lydia', 'david'),
    Person('caleb', 'krista'),
    Person('krista', 'caleb'),
    Person('destiny', 'travis'),
    Person('travis', 'destiny'),
    Person('josiah', 'chanel'),
    Person('chanel', 'josiah'),
    Person('abigal', 'derrick'),
    Person('derrick', 'abigal'),
    Person('josh'),
    Person('levi'),
    Person('luke')
]


def get_partners():
    '''Shuffle list of people, then iterate through people, make sure person
    chosen at random is not the same person, or spouse of person.'''

    random.shuffle(people)
    partners = []
    chosen = []

    for person in people:
        avail = [p for p in people if p.name !=
                 person.name and p.spouse != person.name and p.name not in chosen]

        if len(avail) == 0:
            break

        other = random.choice(avail)
        partners.append([f'{person.name} HAS {other.name}'])
        chosen.append(other.name)
    
    '''There are scenarios where 1 or more people will be left over,
    in this case, a list will return the names, and the method will be called again.'''
    not_chosen = [p for p in people if p.name not in chosen]

    return partners, not_chosen


if __name__ == '__main__':
    
    partners, not_chosen = get_partners()

    '''If we have remaining people from the list, go again until everyone has a partner'''
    while len(not_chosen) > 0:
        print('going again')
        partners, not_chosen = get_partners()

    assert len(partners) == 13
    assert len(not_chosen) == 0
    
    for i in partners:
        print(i[0])
