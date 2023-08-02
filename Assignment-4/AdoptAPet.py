'''
Keshav Shah

Question 9: Adopt A Pet
You receive a sequence of incoming people (to adopt pets) and animals (new additions to the shelter) one at a time.
Print the names and species of the pets as they are adopted out.

Maintaining Two Queues

Time Complexity: O(m*n) --> m pets to add to queue and n adoptions to check
Space Complexity: O(m*n) --> 2 queues made: one with m dogs and one with n cats

Process:
    - Make two queues, one for cat and one for dog
    - Append the animals from the input into the queue
    - Loop through the queue of adoptions and check if it is a person and see what animal they want
    - If there is that animal, give the oldest animal of that type, if not, give the oldest animal overall
    - If it is not a person, check if it is a dog or a cat and add it to the right queue

Time Spent: 35 minutes
'''

from collections import deque

def adopt_a_pet(pets, adoptions):
    dog = []
    cat = []
    output = []
    # put all dogs and cats in the array
    for name, animal, time in pets:
        if animal == 'dog':
            dog.append((time, name))
        else:
            cat.append((time, name))

    # sort from shortest to longest time
    dog.sort()
    cat.sort()
    dog = deque(dog)
    cat = deque(cat)

    for i in range(len(adoptions)):
        # people adopting
        if adoptions[i][1] == 'person':
            animal = adoptions[i][-1]
            # pick dog
            if (animal == 'dog' and len(dog) != 0 ) or (animal == 'cat' and len(cat) == 0):
                if dog:
                    pet = dog.pop()
                    output.append((pet[-1], 'dog'))

            # pick cat
            else:
                if cat:
                    pet = cat.popleft()
                    output.append((pet[-1], 'cat'))

        else:
            name, animal = adoptions[i][0], adoptions[i][1]
            if animal == 'dog':
                dog.append((time, name))
            else:
                cat.append((time, name))

    return output

def main():

    pets = [('Sadie', 'dog', 4),
            ('Woof', 'cat', 7),
            ('Chirpy', 'dog', 2),
            ('Lola', 'dog', 1)]

    adoptions = [('Bob', 'person', 'dog'),
                 ('Floofy', 'cat'),
                 ('Ji', 'person', 'cat'),
                 ('Sally', 'person', 'cat'),
                 ('Ali', 'person', 'cat')]

    print(adopt_a_pet(pets, adoptions))
    # Correctly Prints Output
    # [('Sadie', 'dog'), ('Woof', 'cat'), ('Floofy', 'cat'), ('Chirpy', 'dog')]

main()
