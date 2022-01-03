data = {
    'vertebrado': {
        'ave': {
            'carnivoro': 'aguia',
            'onivoro': 'pomba'
        },
        'mamifero': {
            'onivoro': 'homem',
            'herbivoro': 'vaca'
        }
    },
    'invertebrado': {
        'inseto': {
            'hematofago': 'pulga',
            'herbivoro': 'lagarta'
        },
        'anelideo': {
            'hematofago': 'sanguessuga',
            'onivoro': 'minhoca'
        }
    }
}

animals_categories = []
animals_categories.append(input())
animals_categories.append(input())
animals_categories.append(input())

try:
    animal = data[animals_categories[0]][animals_categories[1]][animals_categories[2]]
    print(animal)
except Exception as e:
    pass
