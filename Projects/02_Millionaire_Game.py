questions=[["Who is shah rukh khan?", "WWE Wrestler", "Actor", "Plumber", "Astronaut",2],          

["What is the capital of France?", "Berlin", "Madrid", "Paris", "Rome", 3],

["Which planet is known as the Red Planet?", "Venus", "Mars", "Jupiter", "Saturn", 2],

["Who invented the light bulb?", "Isaac Newton", "Nikola Tesla", "Albert Einstein", "Thomas Edison", 4],

["What is the largest mammal on Earth?", "Elephant", "Giraffe", "Blue Whale", "Tiger", 3],

["Which element has the chemical symbol 'O'?", "Oxygen", "Gold", "Iron", "Silver", 1],

["Which country is known for the Great Wall?", "India", "Egypt", "China", "Mexico", 3],

["Who wrote 'Romeo and Juliet'?", "Charles Dickens", "William Shakespeare", "Leo Tolstoy", "Mark Twain", 2],

["Which organ pumps blood in the human body?", "Brain", "Lungs", "Heart", "Liver", 3],

["Which is the fastest land animal?", "Cheetah", "Lion", "Horse", "Tiger", 1]
]


prizes = [70000000,50000000,10000000,5000000,2500000,100000,50000,25000,10000,1.00000000000000000]


i=0
for question in questions:
    
    print(question[0])
    print(f"a. {question[1]}")
    print(f"b. {question[2]}")
    print(f"c. {question[3]}")
    print(f"d. {question[4]}")
#checking answer
    a = int(input("Enter your answer . 1 for a/ 2 for b/ 3 for c/ 4 for d\n"))
    if(question[5] == a):
        print("Correct answer")
    else:
        print(f"Incorrect, the correct answer was {question[0]}")
        print("Better Luck next Time!")
        break

    
    print(f"you won{prizes[i]}")
    i +=1
