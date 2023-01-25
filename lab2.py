def main():


    # TODO: Step 2 - Create a complex data structure
    about_me = {
        'full_name': 'Jaina Morjaria',
        'student_id': '10241552',
        'pizza toppings': [
            'Pepperoni',
            'Sausage',
            'Pineapple',
            'Rat Poison'
        ],
        'movies': [
            {
            'kill bill': 'thriller homage'
            },
            {
            'hot fuzz': 'police comedy'
            }
        ]
    }

    # TODO: Step 3 - Add another movie to the data structure
    
    about_me['movies'].insert(1, {'edgerunners': 'cyberpunk thriller'})


# TODO: Step 4 - Function that prints student name and ID	
def print_student_name_and_id(about_me):
   print(f"The {about_me['name'].title} is {about_me['id'].title}")
    
# TODO: Step 5 - Function that adds pizza toppings to data structure
def add_pizza_toppings(about_me, new_toppings):
    about_me['toppings'].extend(new_toppings)

    for i,p in about_me['toppings']:
        about_me['toppings'][i] = p.title()

        about_me['toppings'].sort()
        pass

# TODO: Step 6 - Function that prints bullet list of pizza toppings
def print_pizza_toppings(about_me):
   print("my favorite za' toppings are:")
   for p in about_me['toppings']:
    print(f'-{p}')

# TODO: Step 7 - Function that prints comma-separated list of movie genres
def print_movie_genres(about_me):
    for i,g in enumerate(about_me['movies']):
        if i < len(about_me['movies']) - 1:
            print(f'{g["movies"]}, ', end='')
        else:
            print(f'{g["movies"]}')



# TODO: Step 8 - Function that prints comma-separated list of movie titles
def print_movie_titles(movie_list, about_me):
    movies_titles = [g["movies"] for g in about_me['movies']]
    movies_csl = ', '.join(movies_titles)
    print(movies_csl)
    pass
    
if __name__ == '__main__':
    main()
