
import time

scores = {"General Knowledge Quiz": {"Most Recent Simple Score": "[0/10]", "Best Simple Score": 0, "Most Recent Intermediate Score": "[0/10]", "Best Intermediate Score": 0, "Most Recent Advanced Score": "[0/10]", "Best Advanced Score": 0},
          "Video Games Quiz": {"Most Recent Simple Score": "[0/10]", "Best Simple Score": 0, "Most Recent Intermediate Score": "[0/10]", "Best Intermediate Score": 0, "Most Recent Advanced Score": "[0/10]", "Best Advanced Score": 0},
          "History Quiz": {"Most Recent Simple Score": "[0/10]", "Best Simple Score": 0, "Most Recent Intermediate Score": "[0/10]", "Best Intermediate Score": 0, "Most Recent Advanced Score": "[0/10]", "Best Advanced Score": 0},
          "Sports Quiz": {"Most Recent Simple Score": "[0/10]", "Best Simple Score": 0, "Most Recent Intermediate Score": "[0/10]", "Best Intermediate Score": 0, "Most Recent Advanced Score": "[0/10]", "Best Advanced Score": 0},
          "Movies Quiz": {"Most Recent Simple Score": "[0/10]", "Best Simple Score": 0, "Most Recent Intermediate Score": "[0/10]", "Best Intermediate Score": 0, "Most Recent Advanced Score": "[0/10]", "Best Advanced Score": 0},
          "Music Quiz": {"Most Recent Simple Score": "[0/10]", "Best Simple Score": 0, "Most Recent Intermediate Score": "[0/10]", "Best Intermediate Score": 0, "Most Recent Advanced Score": "[0/10]", "Best Advanced Score": 0}
 
          }
time.sleep(0.5)
print("\nWelcome to the quiz!")
time.sleep(0.5)

def start():

    try:
        print("\nPlease select which quiz you would like to test your knowledge with.")
        time.sleep(0.5)
        print("\n1. General Knowledge")
        time.sleep(0.2)
        print("2. Video Games")
        time.sleep(0.2)
        print("3. History")
        time.sleep(0.2)
        print("4. Sports")
        time.sleep(0.2)
        print("5. Movies")
        time.sleep(0.2)
        print("6. Music")
        time.sleep(0.2)
        print("7. Check Scores")
        time.sleep(0.2)
        print("8. Close Program")
        time.sleep(0.2)
        user_input = int(input("[1/7]: "))
        time.sleep(1)

        if user_input == 1:
            print("\nYou have chosen 1. General Knowledge.")
            time.sleep(0.5)
            difficulty_select(user_input)

        elif user_input == 2:
            print("\nYou have chosen 2. Video Games.")
            time.sleep(0.5)
            difficulty_select(user_input)
            
        elif user_input == 3:
            print("\nYou have chosen 3. History.")
            time.sleep(0.5)
            difficulty_select(user_input)
            
        elif user_input == 4:
            print("\nYou have chosen 4. Sports.")
            time.sleep(0.5)
            difficulty_select(user_input)
            
        elif user_input == 5:
            print("\nYou have chosen 5. Movies.")
            time.sleep(0.5)
            difficulty_select(user_input)
            
        elif user_input == 6:
            print("\nYou have chosen 6. Music.")
            time.sleep(0.5)
            difficulty_select(user_input)
        
        elif user_input == 7:
            print("\nYou have chosen 7. Check Scores.")
            time.sleep(0.5)
            totals(0, 0, 0, 0)
        
        elif user_input == 8:
            print("\nYou have chosen to close the program, Thank you for playing!")
            return
        else:
            print("\nYou need to choose between 1 and 7.")
            time.sleep(0.5)
            start()
    
    except ValueError as v:
        print(f"\nAn Error Occurred: {v}")
        time.sleep(1)
        print("You will be brought back to the start of the program. Please input a number between 1 and 7 to proceed.")
        time.sleep(2)
        start()
    except Exception as e:
        print(f"\nAn Error Occurred: {e}")
        time.sleep(1)
        print("The program will now restart, please ensure you follow the instructions properly.")
        time.sleep(2)
        start()

def difficulty_select(quiz):

    try:
        print("\nThere are three difficulties to pick from each containing 10 multiple choice questions with 5 possible choices each.")
        time.sleep(1)
        print("\nWhich difficulty would you like this quiz to be?")
        time.sleep(0.2)
        print("\n1. Simple")
        time.sleep(0.2)
        print("2. Intermediate")
        time.sleep(0.2)
        print("3. Advanced")
        time.sleep(0.2)
        difficulty = int(input("[1/3]: "))
        time.sleep(1)

        if difficulty == 1:
            print("\nYou have selected 1. Simple.")
            time.sleep(1)
            if quiz == 1:
                general_quiz(difficulty)
            elif quiz == 2:
                games_quiz(difficulty)
            elif quiz == 3:
                history_quiz(difficulty)
            elif quiz == 4:
                sports_quiz(difficulty)
            elif quiz == 5:
                movies_quiz(difficulty)
            elif quiz == 6:
                music_quiz(difficulty)

        elif difficulty == 2:
            print("\nYou have selected 2. Intermediate.")
            time.sleep(1)
            if quiz == 1:
                general_quiz(difficulty)
            elif quiz == 2:
                games_quiz(difficulty)
            elif quiz == 3:
                history_quiz(difficulty)
            elif quiz == 4:
                sports_quiz(difficulty)
            elif quiz == 5:
                movies_quiz(difficulty)
            elif quiz == 6:
                music_quiz(difficulty)

        elif difficulty == 3:
            print("\nYou have selected 3. Advanced.")
            time.sleep(1)
            if quiz == 1:
                general_quiz(difficulty)
            elif quiz == 2:
                games_quiz(difficulty)
            elif quiz == 3:
                history_quiz(difficulty)
            elif quiz == 4:
                sports_quiz(difficulty)
            elif quiz == 5:
                movies_quiz(difficulty)
            elif quiz == 6:
                music_quiz(difficulty)

        else:
            print("\nYou need to choose between 1 and 3.")
            time.sleep(0.5)
            difficulty_select(quiz)

    except ValueError as v:
        print(f"\nAn Error Occurred: {v}")
        time.sleep(1)
        print("You will be brought back to the diffiiculty selection. Please input a number between 1 and 3 to proceed.")
        time.sleep(2)
        difficulty_select(quiz)
    except Exception as e:
        print(f"\nAn Error Occurred: {e}")
        time.sleep(1)
        print("The program will now restart, please ensure you follow the instructions properly.")
        time.sleep(2)
        start()

def general_quiz(difficulty):
    
    simple_total = 0
    intermediate_total = 0
    advanced_total = 0

    try:
        if difficulty == 1:

            time.sleep(0.7)
            print("\nQuestion 1: What is the capital of France?")
            time.sleep(0.5)
            print("a) Rome")
            time.sleep(0.2)
            print("b) Paris")
            time.sleep(0.2)
            print("c) Madrid")
            time.sleep(0.2)
            print("d) Berlin")
            time.sleep(0.2)
            print("e) Lisbon")
            time.sleep(0.2)
            simple_answer1 = input("Answer [a/b/c/d/e]: ")
            simple_correct1 = "b"

            if simple_answer1.lower() == simple_correct1:
                simple_total += 1

            time.sleep(0.7)
            print("\nQuestion 2: Which planet is known as the Red Planet?")
            time.sleep(0.5)
            print("a) Earth")
            time.sleep(0.2)
            print("b) Venus")
            time.sleep(0.2)
            print("c) Mars")
            time.sleep(0.2)
            print("d) Jupiter")
            time.sleep(0.2)
            print("e) Saturn")
            time.sleep(0.2)
            simple_answer2 = input("Answer [a/b/c/d/e]: ")
            simple_correct2 = "c"

            if simple_answer2.lower() == simple_correct2:
                simple_total += 1

            time.sleep(0.7)
            print('\nQuestion 3: Who wrote the play "Romeo and Juliet"?')
            time.sleep(0.5)
            print("a) Charles Dickens")
            time.sleep(0.2)
            print("b) William Shakespeare")
            time.sleep(0.2)
            print("c) Mark Twain")
            time.sleep(0.2)
            print("d) Jane Austen")
            time.sleep(0.2)
            print("e) Leo Tolstoy")
            time.sleep(0.2)
            simple_answer3 = input("Answer [a/b/c/d/e]: ")
            simple_correct3 = "b"

            if simple_answer3.lower() == simple_correct3:
                simple_total += 1

            time.sleep(0.7)
            print("\nQuestion 4: What is the largest mammal in the world?")
            time.sleep(0.5)
            print("a) Elephant")
            time.sleep(0.2)
            print("b) Blue Whale")
            time.sleep(0.2)
            print("c) Giraffe")
            time.sleep(0.2)
            print("d) Hippopotamus")
            time.sleep(0.2)
            print("e) Great White Shark")
            time.sleep(0.2)
            simple_answer4 = input("Answer [a/b/c/d/e]: ")
            simple_correct4 = "b"

            if simple_answer4.lower() == simple_correct4:
                simple_total += 1

            time.sleep(0.7)
            print("\nQuestion 5: How many continents are there on Earth?")
            time.sleep(0.5)
            print("a) Five")
            time.sleep(0.2)
            print("b) Six")
            time.sleep(0.2)
            print("c) Seven")
            time.sleep(0.2)
            print("d) Eight")
            time.sleep(0.2)
            print("e) Four")
            time.sleep(0.2)
            simple_answer5 = input("Answer [a/b/c/d/e]: ")
            simple_correct5 = "c"

            if simple_answer5.lower() == simple_correct5:
                simple_total += 1

            time.sleep(0.7)
            print("\nQuestion 6: Which chemical element has the symbol 'O'?")
            time.sleep(0.5)
            print("a) Gold")
            time.sleep(0.2)
            print("b) Silver")
            time.sleep(0.2)
            print("c) Oxygen")
            time.sleep(0.2)
            print("d) Hydrogen")
            time.sleep(0.2)
            print("e) Carbon")
            time.sleep(0.2)
            simple_answer6 = input("Answer [a/b/c/d/e]: ")
            simple_correct6 = "c"

            if simple_answer6.lower() == simple_correct6:
                simple_total += 1
            
            time.sleep(0.7)
            print("\nQuestion 7: Who was the first man to walk on the moon?")
            time.sleep(0.5)
            print("a) Yuri Gagarin")
            time.sleep(0.2)
            print("b) Buzz Aldrin")
            time.sleep(0.2)
            print("c) Michael Collins")
            time.sleep(0.2)
            print("d) John Glenn")
            time.sleep(0.2)
            print("e) Neil Armstrong")
            time.sleep(0.2)
            simple_answer7 = input("Answer [a/b/c/d/e]: ")
            simple_correct7 = "e"

            if simple_answer7.lower() == simple_correct7:
                simple_total += 1

            time.sleep(0.7)
            print("\nQuestion 8: Which language is primarily spoken in Brazil?")
            time.sleep(0.5)
            print("a) Spanish")
            time.sleep(0.2)
            print("b) Portuguese")
            time.sleep(0.2)
            print("c) French")
            time.sleep(0.2)
            print("d) English")
            time.sleep(0.2)
            print("e) Italian")
            time.sleep(0.2)
            simple_answer8 = input("Answer [a/b/c/d/e]: ")
            simple_correct8 = "b"

            if simple_answer8.lower() == simple_correct8:
                simple_total += 1

            time.sleep(0.7)
            print("\nQuestion 9: What is the boiling point of water?")
            time.sleep(0.5)
            print("a) 50°C")
            time.sleep(0.2)
            print("b) 100°C")
            time.sleep(0.2)
            print("c) 150°C")
            time.sleep(0.2)
            print("d) 200°C")
            time.sleep(0.2)
            print("e) 0°C")
            time.sleep(0.2)
            simple_answer9 = input("Answer [a/b/c/d/e]: ")
            simple_correct9 = "b"

            if simple_answer9.lower() == simple_correct9:
                simple_total += 1

            time.sleep(0.7)
            print("\nQuestion 10: What is the largest organ in the human body?")
            time.sleep(0.5)
            print("a) Heart")
            time.sleep(0.2)
            print("b) Liver")
            time.sleep(0.2)
            print("c) Lungs")
            time.sleep(0.2)
            print("d) Skin")
            time.sleep(0.2)
            print("e) Brain")
            time.sleep(0.2)
            simple_answer10 = input("Answer [a/b/c/d/e]: ")
            simple_correct10 = "d"

            if simple_answer10.lower() == simple_correct10:
                simple_total += 1

            totals("general", simple_total, intermediate_total, advanced_total)

        elif difficulty == 2:

            time.sleep(0.7)
            print("\nQuestion 1: What is the longest river in the world")
            time.sleep(0.5)
            print("a) Amazon River")
            time.sleep(0.2)
            print("b) Nile River")
            time.sleep(0.2)
            print("c) Yangtze River")
            time.sleep(0.2)
            print("d) Mississippi River")
            time.sleep(0.2)
            print("e) Congo River")
            time.sleep(0.2)
            intermediate_answer1 = input("Answer [a/b/c/d/e]: ")
            intermediate_correct1 = "b"

            if intermediate_answer1.lower() == intermediate_correct1:
                intermediate_total += 1

            time.sleep(0.7)
            print("\nQuestion 2: Which element has the atomic number 1?")
            time.sleep(0.5)
            print("a) Helium")
            time.sleep(0.2)
            print("b) Carbon")
            time.sleep(0.2)
            print("c) Oxygen")
            time.sleep(0.2)
            print("d) Hydrogen")
            time.sleep(0.2)
            print("e) Nitrogen")
            time.sleep(0.2)
            intermediate_answer2 = input("Answer [a/b/c/d/e]: ")
            intermediate_correct2 = "d"

            if intermediate_answer2.lower() == intermediate_correct2:
                intermediate_total += 1

            time.sleep(0.7)
            print("\nQuestion 3: Which country is known as the Land of the Rising Sun?")
            time.sleep(0.5)
            print("a) China")
            time.sleep(0.2)
            print("b) Japan")
            time.sleep(0.2)
            print("c) South Korea")
            time.sleep(0.2)
            print("d) Thailand")
            time.sleep(0.2)
            print("e) Vietnam")
            time.sleep(0.2)
            intermediate_answer3 = input("Answer [a/b/c/d/e]: ")
            intermediate_correct3 = "b"

            if intermediate_answer3.lower() == intermediate_correct3:
                intermediate_total += 1

            time.sleep(0.7)
            print('\nQuestion 4: Which artist painted the "Mona Lisa"?')
            time.sleep(0.5)
            print("a) Vincent van Gogh")
            time.sleep(0.2)
            print("b) Pablo Picasso")
            time.sleep(0.2)
            print("c) Michelangelo")
            time.sleep(0.2)
            print("d) Leonardo da Vinci")
            time.sleep(0.2)
            print("e) Rembrandt")
            time.sleep(0.2)
            intermediate_answer4 = input("Answer [a/b/c/d/e]: ")
            intermediate_correct4 = "d"

            if intermediate_answer4.lower() == intermediate_correct4:
                intermediate_total += 1

            time.sleep(0.7)
            print("\nQuestion 5: What is the hardest natural substance on Earth?")
            time.sleep(0.5)
            print("a) Gold")
            time.sleep(0.2)
            print("b) Iron")
            time.sleep(0.2)
            print("c) Diamond")
            time.sleep(0.2)
            print("d) Platinum")
            time.sleep(0.2)
            print("e) Ruby")
            time.sleep(0.2)
            intermediate_answer5 = input("Answer [a/b/c/d/e]: ")
            intermediate_correct5 = "c"

            if intermediate_answer5.lower() == intermediate_correct5:
                intermediate_total += 1

            time.sleep(0.7)
            print("\nQuestion 6: Which country hosted the 2016 Summer Olympics?")
            time.sleep(0.5)
            print("a) China")
            time.sleep(0.2)
            print("b) United Kingdom")
            time.sleep(0.2)
            print("c) Brazil")
            time.sleep(0.2)
            print("d) Japan")
            time.sleep(0.2)
            print("e) Russia")
            time.sleep(0.2)
            intermediate_answer6 = input("Answer [a/b/c/d/e]: ")
            intermediate_correct6 = "c"

            if intermediate_answer6.lower() == intermediate_correct6:
                intermediate_total += 1
            
            time.sleep(0.7)
            print("\nQuestion 7: Who developed the theory of relativity?")
            time.sleep(0.5)
            print("a) Isaac Newton")
            time.sleep(0.2)
            print("b) Albert Einstein")
            time.sleep(0.2)
            print("c) Galileo Galilei")
            time.sleep(0.2)
            print("d) Stephen Hawking")
            time.sleep(0.2)
            print("e) Nikola Tesla")
            time.sleep(0.2)
            intermediate_answer7 = input("Answer [a/b/c/d/e]: ")
            intermediate_correct7 = "b"

            if intermediate_answer7.lower() == intermediate_correct7:
                intermediate_total += 1

            time.sleep(0.7)
            print('\nQuestion 8: Which novel begins with the line, "It was the best of times, it was the worst of times"?')
            time.sleep(0.5)
            print("a) War and Peace")
            time.sleep(0.2)
            print("b) Pride and Prejudice")
            time.sleep(0.2)
            print("c) The Great Gatsby")
            time.sleep(0.2)
            print("d) A Tale of Two Cities")
            time.sleep(0.2)
            print("e) Moby Dick")
            time.sleep(0.2)
            intermediate_answer8 = input("Answer [a/b/c/d/e]: ")
            intermediate_correct8 = "d"

            if intermediate_answer8.lower() == intermediate_correct8:
                intermediate_total += 1

            time.sleep(0.7)
            print("\nQuestion 9: What is the capital city of Australia?")
            time.sleep(0.5)
            print("a) Sydney")
            time.sleep(0.2)
            print("b) Melbourne")
            time.sleep(0.2)
            print("c) Brisbane")
            time.sleep(0.2)
            print("d) Perth")
            time.sleep(0.2)
            print("e) Canberra")
            time.sleep(0.2)
            intermediate_answer9 = input("Answer [a/b/c/d/e]: ")
            intermediate_correct9 = "e"

            if intermediate_answer9.lower() == intermediate_correct9:
                intermediate_total += 1

            time.sleep(0.7)
            print("\nQuestion 10: What is the smallest planet in our solar system?")
            time.sleep(0.5)
            print("a) Earth")
            time.sleep(0.2)
            print("b) Venus")
            time.sleep(0.2)
            print("c) Mars")
            time.sleep(0.2)
            print("d) Mercury")
            time.sleep(0.2)
            print("e) Pluto")
            time.sleep(0.2)
            intermediate_answer10 = input("Answer [a/b/c/d/e]: ")
            intermediate_correct10 = "d"

            if intermediate_answer10.lower() == intermediate_correct10:
                intermediate_total += 1

            totals("general", simple_total, intermediate_total, advanced_total)

        elif difficulty == 3:
            
            time.sleep(0.7)
            print("\nQuestion 1: Which scientist is known for the laws of planetary motion?")
            time.sleep(0.5)
            print("a) Isaac Newton")
            time.sleep(0.2)
            print("b) Galileo Galilei")
            time.sleep(0.2)
            print("c) Johannes Kepler")
            time.sleep(0.2)
            print("d) Albert Einstein")
            time.sleep(0.2)
            print("e) Niels Bohr")
            time.sleep(0.2)
            advanced_answer1 = input("Answer [a/b/c/d/e]: ")
            advanced_correct1 = "c"

            if advanced_answer1.lower() == advanced_correct1:
                advanced_total += 1

            time.sleep(0.7)
            print("\nQuestion 2: Who was the first person to reach the South Pole?")
            time.sleep(0.5)
            print("a) Robert Falcon Scott")
            time.sleep(0.2)
            print("b) Ernest Shackleton")
            time.sleep(0.2)
            print("c) Roald Amundsen")
            time.sleep(0.2)
            print("d) Edmund Hillary")
            time.sleep(0.2)
            print("e) Richard Byrd")
            time.sleep(0.2)
            advanced_answer2 = input("Answer [a/b/c/d/e]: ")
            advanced_correct2 = "c"

            if advanced_answer2.lower() == advanced_correct2:
                advanced_total += 1

            time.sleep(0.7)
            print('\nQuestion 3: Which composer wrote the "Moonlight Sonata"?')
            time.sleep(0.5)
            print("a) Ludwig van Beethoven")
            time.sleep(0.2)
            print("b) Wolfgang Amadeus Mozart")
            time.sleep(0.2)
            print("c) Johann Sebastian Bach")
            time.sleep(0.2)
            print("d) Franz Schubert")
            time.sleep(0.2)
            print("e) Frédéric Chopin")
            time.sleep(0.2)
            advanced_answer3 = input("Answer [a/b/c/d/e]: ")
            advanced_correct3 = "a"

            if advanced_answer3.lower() == advanced_correct3:
                advanced_total += 1

            time.sleep(0.7)
            print("\nQuestion 4: Which philosopher is known for his method of questioning to achieve deeper understanding, known as the Socratic method?")
            time.sleep(0.5)
            print("a) Aristotle")
            time.sleep(0.2)
            print("b) Socrates")
            time.sleep(0.2)
            print("c) Plato")
            time.sleep(0.2)
            print("d) Descartes")
            time.sleep(0.2)
            print("e) Confucius")
            time.sleep(0.2)
            advanced_answer4 = input("Answer [a/b/c/d/e]: ")
            advanced_correct4 = "b"

            if advanced_answer4.lower() == advanced_correct4:
                advanced_total += 1

            time.sleep(0.7)
            print("\nQuestion 5: In which year did the Titanic sink?")
            time.sleep(0.5)
            print("a) 1905")
            time.sleep(0.2)
            print("b) 1908")
            time.sleep(0.2)
            print("c) 1912")
            time.sleep(0.2)
            print("d) 1915")
            time.sleep(0.2)
            print("e) 1918")
            time.sleep(0.2)
            advanced_answer5 = input("Answer [a/b/c/d/e]: ")
            advanced_correct5 = "c"

            if advanced_answer5.lower() == advanced_correct5:
                advanced_total += 1

            time.sleep(0.7)
            print("\nQuestion 6: Which element is represented by the symbol 'W'?")
            time.sleep(0.5)
            print("a) Tungsten")
            time.sleep(0.2)
            print("b) Tin")
            time.sleep(0.2)
            print("c) Silver")
            time.sleep(0.2)
            print("d) Uranium")
            time.sleep(0.2)
            print("e) Zinc")
            time.sleep(0.2)
            advanced_answer6 = input("Answer [a/b/c/d/e]: ")
            advanced_correct6 = "a"

            if advanced_answer6.lower() == advanced_correct6:
                advanced_total += 1
            
            time.sleep(0.7)
            print("\nQuestion 7: What is the capital of Canada?")
            time.sleep(0.5)
            print("a) Toronto")
            time.sleep(0.2)
            print("b) Vancouver")
            time.sleep(0.2)
            print("c) Montreal")
            time.sleep(0.2)
            print("d) Ottawa")
            time.sleep(0.2)
            print("e) Calgary")
            time.sleep(0.2)
            advanced_answer7 = input("Answer [a/b/c/d/e]: ")
            advanced_correct7 = "d"

            if advanced_answer7.lower() == advanced_correct7:
                advanced_total += 1

            time.sleep(0.7)
            print("\nQuestion 8: Which war was fought between the houses of Lancaster and York?")
            time.sleep(0.5)
            print("a) The Hundred Years' War")
            time.sleep(0.2)
            print("b) The War of the Roses")
            time.sleep(0.2)
            print("c) The English Civil War")
            time.sleep(0.2)
            print("d) The Anglo-Saxon War")
            time.sleep(0.2)
            print("e) The Glorious Revolution")
            time.sleep(0.2)
            advanced_answer8 = input("Answer [a/b/c/d/e]: ")
            advanced_correct8 = "b"

            if advanced_answer8.lower() == advanced_correct8:
                advanced_total += 1

            time.sleep(0.7)
            print("\nQuestion 9: What is the longest mountain range in the world?")
            time.sleep(0.5)
            print("a) Himalayas")
            time.sleep(0.2)
            print("b) Rockies")
            time.sleep(0.2)
            print("c) Andes")
            time.sleep(0.2)
            print("d) Alps")
            time.sleep(0.2)
            print("e) Appalachian")
            time.sleep(0.2)
            advanced_answer9 = input("Answer [a/b/c/d/e]: ")
            advanced_correct9 = "c"

            if advanced_answer9.lower() == advanced_correct9:
                advanced_total += 1

            time.sleep(0.7)
            print("\nQuestion 10: Which ancient civilization built the city of Machu Picchu?")
            time.sleep(0.5)
            print("a) Mayans")
            time.sleep(0.2)
            print("b) Aztecs")
            time.sleep(0.2)
            print("c) Incas")
            time.sleep(0.2)
            print("d) Toltecs")
            time.sleep(0.2)
            print("e) Olmecs")
            time.sleep(0.2)
            advanced_answer10 = input("Answer [a/b/c/d/e]: ")
            advanced_correct10 = "c"

            if advanced_answer10.lower() == advanced_correct10:
                advanced_total += 1

            totals("general", simple_total, intermediate_total, advanced_total)

    except ValueError as v:
        print(f"\nAn Error Occurred: {v}")
        time.sleep(1)
        print("You will be brought back to the start of the quiz. Please input either a,b,c,d,e as your answer to continue.")
        time.sleep(2)
        general_quiz(difficulty)
    except Exception as e:
        print(f"\nAn Error Occurred: {e}")
        time.sleep(1)
        print("The program will now restart, please ensure you follow the instructions properly.")
        time.sleep(2)
        start()




def games_quiz(difficulty):

    simple_total = 0
    intermediate_total = 0
    advanced_total = 0

    try:
        if difficulty == 1:

            time.sleep(0.7)
            print("\nQuestion 1: Which character is known as the mascot of Nintendo?")
            time.sleep(0.5)
            print("a) Link")
            time.sleep(0.2)
            print("b) Donkey Kong")
            time.sleep(0.2)
            print("c) Mario")
            time.sleep(0.2)
            print("d) Samus")
            time.sleep(0.2)
            print("e) Pikachu")
            time.sleep(0.2)
            simple_answer1 = input("Answer [a/b/c/d/e]: ")
            simple_correct1 = "c"

            if simple_answer1.lower() == simple_correct1:
                simple_total += 1

            time.sleep(0.7)
            print("\nQuestion 2: What is the main character's name in The Legend of Zelda series?")
            time.sleep(0.5)
            print("a) Zelda")
            time.sleep(0.2)
            print("b) Link")
            time.sleep(0.2)
            print("c) Ganon")
            time.sleep(0.2)
            print("d) Navi")
            time.sleep(0.2)
            print("e) Sheik")
            time.sleep(0.2)
            simple_answer2 = input("Answer [a/b/c/d/e]: ")
            simple_correct2 = "b"

            if simple_answer2.lower() == simple_correct2:
                simple_total += 1

            time.sleep(0.7)
            print("\nQuestion 3: What game popularized the battle royale genre?")
            time.sleep(0.5)
            print("a) Fortnite")
            time.sleep(0.2)
            print("b) Apex Legends")
            time.sleep(0.2)
            print("c) PUBG (PlayerUnknown's Battlegrounds)")
            time.sleep(0.2)
            print("d) Call of Duty: Warzone")
            time.sleep(0.2)
            print("e) H1Z1")
            time.sleep(0.2)
            simple_answer3 = input("Answer [a/b/c/d/e]: ")
            simple_correct3 = "c"

            if simple_answer3.lower() == simple_correct3:
                simple_total += 1

            time.sleep(0.7)
            print("\nQuestion 4: Which company developed the PlayStation console?")
            time.sleep(0.5)
            print("a) Microsoft")
            time.sleep(0.2)
            print("b) Sony")
            time.sleep(0.2)
            print("c) Nintendo")
            time.sleep(0.2)
            print("d) Sega")
            time.sleep(0.2)
            print("e) Atari")
            time.sleep(0.2)
            simple_answer4 = input("Answer [a/b/c/d/e]: ")
            simple_correct4 = "b"

            if simple_answer4.lower() == simple_correct4:
                simple_total += 1

            time.sleep(0.7)
            print("\nQuestion 5: In which game do players compete to build and manage a farm?")
            time.sleep(0.5)
            print("a) Minecraft")
            time.sleep(0.2)
            print("b) Stardew Valley")
            time.sleep(0.2)
            print("c) Animal Crossing")
            time.sleep(0.2)
            print("d) The Sims")
            time.sleep(0.2)
            print("e) FarmVille")
            time.sleep(0.2)
            simple_answer5 = input("Answer [a/b/c/d/e]: ")
            simple_correct5 = "c"

            if simple_answer5.lower() == simple_correct5:
                simple_total += 1

            time.sleep(0.7)
            print("\nQuestion 6: What color is the ring around the Xbox 360 power button when it is fully functional?")
            time.sleep(0.5)
            print("a) Red")
            time.sleep(0.2)
            print("b) Green")
            time.sleep(0.2)
            print("c) Yellow")
            time.sleep(0.2)
            print("d) Blue")
            time.sleep(0.2)
            print("e) White")
            time.sleep(0.2)
            simple_answer6 = input("Answer [a/b/c/d/e]: ")
            simple_correct6 = "b"

            if simple_answer6.lower() == simple_correct6:
                simple_total += 1
            
            time.sleep(0.7)
            print("\nQuestion 7: Which game features the characters Ryu and Ken?")
            time.sleep(0.5)
            print("a) Mortal Kombat")
            time.sleep(0.2)
            print("b) Tekken")
            time.sleep(0.2)
            print("c) Street Fighter")
            time.sleep(0.2)
            print("d) King of Fighters")
            time.sleep(0.2)
            print("e) Super Smash Bros.")
            time.sleep(0.2)
            simple_answer7 = input("Answer [a/b/c/d/e]: ")
            simple_correct7 = "b"

            if simple_answer7.lower() == simple_correct7:
                simple_total += 1

            time.sleep(0.7)
            print("\nQuestion 8: Which game series features a hidden blade as a signature weapon?")
            time.sleep(0.5)
            print("a) God of War")
            time.sleep(0.2)
            print("b) Dark Souls")
            time.sleep(0.2)
            print("c) Assassin's Creed")
            time.sleep(0.2)
            print("d) Devil May Cry")
            time.sleep(0.2)
            print("e) Metal Gear Solid")
            time.sleep(0.2)
            simple_answer8 = input("Answer [a/b/c/d/e]: ")
            simple_correct8 = "c"

            if simple_answer8.lower() == simple_correct8:
                simple_total += 1

            time.sleep(0.7)
            print("\nQuestion 9: What is the name of the main protagonist in the Halo series?")
            time.sleep(0.5)
            print("a) Arbiter")
            time.sleep(0.2)
            print("b) Master Chief")
            time.sleep(0.2)
            print("c) Cortana")
            time.sleep(0.2)
            print("d) Noble Six")
            time.sleep(0.2)
            print("e) Sergeant Johnson")
            time.sleep(0.2)
            simple_answer9 = input("Answer [a/b/c/d/e]: ")
            simple_correct9 = "c"

            if simple_answer9.lower() == simple_correct9:
                simple_total += 1

            time.sleep(0.7)
            print("\nQuestion 10: Which video game features the fictional city of Vice City?")
            time.sleep(0.5)
            print("a) Grand Theft Auto V")
            time.sleep(0.2)
            print("b) Grand Theft Auto: San Andreas")
            time.sleep(0.2)
            print("c) Grand Theft Auto: Vice City")
            time.sleep(0.2)
            print("d) Grand Theft Auto IV")
            time.sleep(0.2)
            print("e) Grand Theft Auto III")
            time.sleep(0.2)
            simple_answer10 = input("Answer [a/b/c/d/e]: ")
            simple_correct10 = "b"

            if simple_answer10.lower() == simple_correct10:
                simple_total += 1

            totals("game", simple_total, intermediate_total, advanced_total)

        elif difficulty == 2:

            time.sleep(0.7)
            print("\nQuestion 1: Which game is considered to have created the genre of first-person shooters?")
            time.sleep(0.5)
            print("a) Doom")
            time.sleep(0.2)
            print("b) Wolfenstein 3D")
            time.sleep(0.2)
            print("c) Quake")
            time.sleep(0.2)
            print("d) Duke Nukem 3D")
            time.sleep(0.2)
            print("e) Half-Life")
            time.sleep(0.2)
            intermediate_answer1 = input("Answer [a/b/c/d/e]: ")
            intermediate_correct1 = "b"

            if intermediate_answer1.lower() == intermediate_correct1:
                intermediate_total += 1

            time.sleep(0.7)
            print("\nQuestion 2: Which character is known as the 'Blue Blur'?")
            time.sleep(0.5)
            print("a) Mega Man")
            time.sleep(0.2)
            print("b) Sonic the Hedgehog")
            time.sleep(0.2)
            print("c) Crash Bandicoot")
            time.sleep(0.2)
            print("d) Pac-Man")
            time.sleep(0.2)
            print("e) Samus Aran")
            time.sleep(0.2)
            intermediate_answer2 = input("Answer [a/b/c/d/e]: ")
            intermediate_correct2 = "b"

            if intermediate_answer2.lower() == intermediate_correct2:
                intermediate_total += 1

            time.sleep(0.7)
            print("\nQuestion 3: What year was the original PlayStation released?")
            time.sleep(0.5)
            print("a) 1992")
            time.sleep(0.2)
            print("b) 1994")
            time.sleep(0.2)
            print("c) 1996")
            time.sleep(0.2)
            print("d) 1998")
            time.sleep(0.2)
            print("e) 2000")
            time.sleep(0.2)
            intermediate_answer3 = input("Answer [a/b/c/d/e]: ")
            intermediate_correct3 = "b"

            if intermediate_answer3.lower() == intermediate_correct3:
                intermediate_total += 1

            time.sleep(0.7)
            print("\nQuestion 4: Which game developer is responsible for the creation of The Sims series?")
            time.sleep(0.5)
            print("a) Bethesda")
            time.sleep(0.2)
            print("b) EA Maxis")
            time.sleep(0.2)
            print("c) Bungie")
            time.sleep(0.2)
            print("d) Rockstar Games")
            time.sleep(0.2)
            print("e) Valve")
            time.sleep(0.2)
            intermediate_answer4 = input("Answer [a/b/c/d/e]: ")
            intermediate_correct4 = "b"

            if intermediate_answer4.lower() == intermediate_correct4:
                intermediate_total += 1

            time.sleep(0.7)
            print("\nQuestion 5: What is the name of the protagonist in the Metroid series?")
            time.sleep(0.5)
            print("a) Lara Croft")
            time.sleep(0.2)
            print("b) Jill Valentine")
            time.sleep(0.2)
            print("c) Samus Aran")
            time.sleep(0.2)
            print("d) Ada Wong")
            time.sleep(0.2)
            print("e) Chun-Li")
            time.sleep(0.2)
            intermediate_answer5 = input("Answer [a/b/c/d/e]: ")
            intermediate_correct5 = "c"

            if intermediate_answer5.lower() == intermediate_correct5:
                intermediate_total += 1

            time.sleep(0.7)
            print("\nQuestion 6: In which game do players catch creatures in Poké Balls?")
            time.sleep(0.5)
            print("a) Digimon")
            time.sleep(0.2)
            print("b) Pokémon")
            time.sleep(0.2)
            print("c) Yu-Gi-Oh!")
            time.sleep(0.2)
            print("d) Beyblade")
            time.sleep(0.2)
            print("e) Animal Crossing")
            time.sleep(0.2)
            intermediate_answer6 = input("Answer [a/b/c/d/e]: ")
            intermediate_correct6 = "b"

            if intermediate_answer6.lower() == intermediate_correct6:
                intermediate_total += 1
            
            time.sleep(0.7)
            print("\nQuestion 7: What is the highest-selling video game of all time as of 2023?")
            time.sleep(0.5)
            print("a) Tetris")
            time.sleep(0.2)
            print("b) Minecraft")
            time.sleep(0.2)
            print("c) Grand Theft Auto V")
            time.sleep(0.2)
            print("d) Wii Sports")
            time.sleep(0.2)
            print("e) Fortnite")
            time.sleep(0.2)
            intermediate_answer7 = input("Answer [a/b/c/d/e]: ")
            intermediate_correct7 = "b"

            if intermediate_answer7.lower() == intermediate_correct7:
                intermediate_total += 1

            time.sleep(0.7)
            print("\nQuestion 8: In the game Portal, what is the name of the AI antagonist?")
            time.sleep(0.5)
            print("a) HAL 9000")
            time.sleep(0.2)
            print("b) SHODAN")
            time.sleep(0.2)
            print("c) GLaDOS")
            time.sleep(0.2)
            print("d) Wheatley")
            time.sleep(0.2)
            print("e) Cortana")
            time.sleep(0.2)
            intermediate_answer8 = input("Answer [a/b/c/d/e]: ")
            intermediate_correct8 = "c"

            if intermediate_answer8.lower() == intermediate_correct8:
                intermediate_total += 1

            time.sleep(0.7)
            print("\nQuestion 9: Which game features a character named Geralt of Rivia?")
            time.sleep(0.5)
            print("a) Dark Souls")
            time.sleep(0.2)
            print("b) The Elder Scrolls")
            time.sleep(0.2)
            print("c) The Witcher")
            time.sleep(0.2)
            print("d) Dragon Age")
            time.sleep(0.2)
            print("e) Bloodborne")
            time.sleep(0.2)
            intermediate_answer9 = input("Answer [a/b/c/d/e]: ")
            intermediate_correct9 = "c"

            if intermediate_answer9.lower() == intermediate_correct9:
                intermediate_total += 1

            time.sleep(0.7)
            print("\nQuestion 10: Which company developed the game series 'Halo'?")
            time.sleep(0.5)
            print("a) Infinity Ward")
            time.sleep(0.2)
            print("b) Bungie")
            time.sleep(0.2)
            print("c) Epic Games")
            time.sleep(0.2)
            print("d) DICE")
            time.sleep(0.2)
            print("e) Ubisoft")
            time.sleep(0.2)
            intermediate_answer10 = input("Answer [a/b/c/d/e]: ")
            intermediate_correct10 = "b"

            if intermediate_answer10.lower() == intermediate_correct10:
                intermediate_total += 1

            totals("game", simple_total, intermediate_total, advanced_total)

        elif difficulty == 3:
            
            time.sleep(0.7)
            print("\nQuestion 1: Which character from the 'Metal Gear Solid' series is known for the phrase 'Kept you waiting, huh?'")
            time.sleep(0.5)
            print("a) Raiden")
            time.sleep(0.2)
            print("b) Big Boss")
            time.sleep(0.2)
            print("c) Solid Snake")
            time.sleep(0.2)
            print("d) Revolver Ocelot")
            time.sleep(0.2)
            print("e) Gray Fox")
            time.sleep(0.2)
            advanced_answer1 = input("Answer [a/b/c/d/e]: ")
            advanced_correct1 = "c"

            if advanced_answer1.lower() == advanced_correct1:
                advanced_total += 1

            time.sleep(0.7)
            print("\nQuestion 2: What is the name of the planet in the 'Mass Effect' series that serves as Commander Shepard's home?")
            time.sleep(0.5)
            print("a) Palaven")
            time.sleep(0.2)
            print("b) Earth")
            time.sleep(0.2)
            print("c) Thessia")
            time.sleep(0.2)
            print("d) Eden Prime")
            time.sleep(0.2)
            print("e) Tuchanka")
            time.sleep(0.2)
            advanced_answer2 = input("Answer [a/b/c/d/e]: ")
            advanced_correct2 = "b"

            if advanced_answer2.lower() == advanced_correct2:
                advanced_total += 1

            time.sleep(0.7)
            print("\nQuestion 3: Which game in the 'Final Fantasy' series was the first to feature fully 3D graphics?")
            time.sleep(0.5)
            print("a) Final Fantasy VII")
            time.sleep(0.2)
            print("b) Final Fantasy VIII")
            time.sleep(0.2)
            print("c) Final Fantasy IX")
            time.sleep(0.2)
            print("d) Final Fantasy X")
            time.sleep(0.2)
            print("e) Final Fantasy VI")
            time.sleep(0.2)
            advanced_answer3 = input("Answer [a/b/c/d/e]: ")
            advanced_correct3 = "a"

            if advanced_answer3.lower() == advanced_correct3:
                advanced_total += 1

            time.sleep(0.7)
            print("\nQuestion 4: In 'The Legend of Zelda: Ocarina of Time', what item is used to open the Door of Time?")
            time.sleep(0.5)
            print("a) Hookshot")
            time.sleep(0.2)
            print("b) Bombs")
            time.sleep(0.2)
            print("c) Ocarina of Time")
            time.sleep(0.2)
            print("d) Master Sword")
            time.sleep(0.2)
            print("e) Light Arrow")
            time.sleep(0.2)
            advanced_answer4 = input("Answer [a/b/c/d/e]: ")
            advanced_correct4 = "c"

            if advanced_answer4.lower() == advanced_correct4:
                advanced_total += 1

            time.sleep(0.7)
            print("\nQuestion 5: Which game is famous for the phrase 'The cake is a lie'?")
            time.sleep(0.5)
            print("a) Portal")
            time.sleep(0.2)
            print("b) Half-Life 2")
            time.sleep(0.2)
            print("c) Bioshock")
            time.sleep(0.2)
            print("d) Fallout 3")
            time.sleep(0.2)
            print("e) Silent Hill 2")
            time.sleep(0.2)
            advanced_answer5 = input("Answer [a/b/c/d/e]: ")
            advanced_correct5 = "a"

            if advanced_answer5.lower() == advanced_correct5:
                advanced_total += 1

            time.sleep(0.7)
            print("\nQuestion 6: Who is the main antagonist in the 'Dark Souls' series?")
            time.sleep(0.5)
            print("a) Ornstein and Smough")
            time.sleep(0.2)
            print("b) The Nameless King")
            time.sleep(0.2)
            print("c) Gwyn, Lord of Cinder")
            time.sleep(0.2)
            print("d) Manus, Father of the Abyss")
            time.sleep(0.2)
            print("e) Artorias the Abysswalker")
            time.sleep(0.2)
            advanced_answer6 = input("Answer [a/b/c/d/e]: ")
            advanced_correct6 = "c"

            if advanced_answer6.lower() == advanced_correct6:
                advanced_total += 1
            
            time.sleep(0.7)
            print("\nQuestion 7: Which game features the city of Rapture, an underwater utopia?")
            time.sleep(0.5)
            print("a) Subnautica")
            time.sleep(0.2)
            print("b) Bioshock")
            time.sleep(0.2)
            print("c) The Outer Worlds")
            time.sleep(0.2)
            print("d) Half-Life")
            time.sleep(0.2)
            print("e) Dishonored")
            time.sleep(0.2)
            advanced_answer7 = input("Answer [a/b/c/d/e]: ")
            advanced_correct7 = "b"

            if advanced_answer7.lower() == advanced_correct7:
                advanced_total += 1

            time.sleep(0.7)
            print("\nQuestion 8: In 'Bloodborne', what is the name of the first boss players encounter?")
            time.sleep(0.5)
            print("a) Cleric Beast")
            time.sleep(0.2)
            print("b) Father Gascoigne")
            time.sleep(0.2)
            print("c) Vicar Amelia")
            time.sleep(0.2)
            print("d) Rom, the Vacuous Spider")
            time.sleep(0.2)
            print("e) Mergo's Wet Nurse")
            time.sleep(0.2)
            advanced_answer8 = input("Answer [a/b/c/d/e]: ")
            advanced_correct8 = "a"

            if advanced_answer8.lower() == advanced_correct8:
                advanced_total += 1

            time.sleep(0.7)
            print("\nQuestion 9: Which game introduced the character Sephiroth?")
            time.sleep(0.5)
            print("a) Kingdom Hearts")
            time.sleep(0.2)
            print("b) Final Fantasy VI")
            time.sleep(0.2)
            print("c) Final Fantasy VII")
            time.sleep(0.2)
            print("d) Chrono Trigger")
            time.sleep(0.2)
            print("e) Dragon Quest")
            time.sleep(0.2)
            advanced_answer9 = input("Answer [a/b/c/d/e]: ")
            advanced_correct9 = "c"

            if advanced_answer9.lower() == advanced_correct9:
                advanced_total += 1

            time.sleep(0.7)
            print("\nQuestion 10: In which game do you play as a hunter fighting against grotesque beasts in a Victorian-era setting?")
            time.sleep(0.5)
            print("a) Dark Souls")
            time.sleep(0.2)
            print("b) Bloodborne")
            time.sleep(0.2)
            print("c) Resident Evil")
            time.sleep(0.2)
            print("d) Castlevania")
            time.sleep(0.2)
            print("e) The Evil Within")
            time.sleep(0.2)
            advanced_answer10 = input("Answer [a/b/c/d/e]: ")
            advanced_correct10 = "b"

            if advanced_answer10.lower() == advanced_correct10:
                advanced_total += 1

            totals("game", simple_total, intermediate_total, advanced_total)

    except ValueError as v:
        print(f"\nAn Error Occurred: {v}")
        time.sleep(1)
        print("You will be brought back to the start of the quiz. Please input either a,b,c,d,e as your answer to continue.")
        time.sleep(2)
        general_quiz(difficulty)
    except Exception as e:
        print(f"\nAn Error Occurred: {e}")
        time.sleep(1)
        print("The program will now restart, please ensure you follow the instructions properly.")
        time.sleep(2)
        start()

def history_quiz(difficulty):
    
    simple_total = 0
    intermediate_total = 0
    advanced_total = 0

    try:
        if difficulty == 1:

            time.sleep(0.7)
            print("\nQuestion 1: Who was the first President of the United States?")
            time.sleep(0.5)
            print("a) Thomas Jefferson")
            time.sleep(0.2)
            print("b) George Washington")
            time.sleep(0.2)
            print("c) John Adams")
            time.sleep(0.2)
            print("d) James Madison")
            time.sleep(0.2)
            print("e) Abraham Lincoln")
            time.sleep(0.2)
            simple_answer1 = input("Answer [a/b/c/d/e]: ")
            simple_correct1 = "b"

            if simple_answer1.lower() == simple_correct1:
                simple_total += 1

            time.sleep(0.7)
            print("\nQuestion 2: What year did World War II end?")
            time.sleep(0.5)
            print("a) 1939")
            time.sleep(0.2)
            print("b) 1942")
            time.sleep(0.2)
            print("c) 1945")
            time.sleep(0.2)
            print("d) 1947")
            time.sleep(0.2)
            print("e) 1950")
            time.sleep(0.2)
            simple_answer2 = input("Answer [a/b/c/d/e]: ")
            simple_correct2 = "c"

            if simple_answer2.lower() == simple_correct2:
                simple_total += 1

            time.sleep(0.7)
            print("\nQuestion 3: Who was known as the 'Maid of Orléans' and led French troops during the Hundred Years' War?")
            time.sleep(0.5)
            print("a) Catherine the Great")
            time.sleep(0.2)
            print("b) Joan of Arc")
            time.sleep(0.2)
            print("c) Marie Antoinette")
            time.sleep(0.2)
            print("d) Eleanor of Aquitaine")
            time.sleep(0.2)
            print("e) Isabella I")
            time.sleep(0.2)
            simple_answer3 = input("Answer [a/b/c/d/e]: ")
            simple_correct3 = "b"

            if simple_answer3.lower() == simple_correct3:
                simple_total += 1

            time.sleep(0.7)
            print("\nQuestion 4: What ancient civilization built the Pyramids of Giza?")
            time.sleep(0.5)
            print("a) The Romans")
            time.sleep(0.2)
            print("b) The Mesopotamians")
            time.sleep(0.2)
            print("c) The Egyptians")
            time.sleep(0.2)
            print("d) The Greeks")
            time.sleep(0.2)
            print("e) The Mayans")
            time.sleep(0.2)
            simple_answer4 = input("Answer [a/b/c/d/e]: ")
            simple_correct4 = "c"

            if simple_answer4.lower() == simple_correct4:
                simple_total += 1

            time.sleep(0.7)
            print("\nQuestion 5: Which explorer is credited with discovering America in 1492?")
            time.sleep(0.5)
            print("a) Ferdinand Magellan")
            time.sleep(0.2)
            print("b) Vasco da Gama")
            time.sleep(0.2)
            print("c) Christopher Columbus")
            time.sleep(0.2)
            print("d) Hernán Cortés")
            time.sleep(0.2)
            print("e) Marco Polo")
            time.sleep(0.2)
            simple_answer5 = input("Answer [a/b/c/d/e]: ")
            simple_correct5 = "c"

            if simple_answer5.lower() == simple_correct5:
                simple_total += 1

            time.sleep(0.7)
            print("\nQuestion 6: What was the name of the ship that transported the Pilgrims to America in 1620?")
            time.sleep(0.5)
            print("a) Santa Maria")
            time.sleep(0.2)
            print("b) Mayflower")
            time.sleep(0.2)
            print("c) Endeavour")
            time.sleep(0.2)
            print("d) Beagle")
            time.sleep(0.2)
            print("e) Victory")
            time.sleep(0.2)
            simple_answer6 = input("Answer [a/b/c/d/e]: ")
            simple_correct6 = "b"

            if simple_answer6.lower() == simple_correct6:
                simple_total += 1
            
            time.sleep(0.7)
            print("\nQuestion 7: Which war was fought between the North and South regions of the United States?")
            time.sleep(0.5)
            print("a) World War I")
            time.sleep(0.2)
            print("b) American Revolutionary War")
            time.sleep(0.2)
            print("c) American Civil War")
            time.sleep(0.2)
            print("d) War of 1812")
            time.sleep(0.2)
            print("e) Spanish-American War")
            time.sleep(0.2)
            simple_answer7 = input("Answer [a/b/c/d/e]: ")
            simple_correct7 = "c"

            if simple_answer7.lower() == simple_correct7:
                simple_total += 1

            time.sleep(0.7)
            print("\nQuestion 8: Who was the British Prime Minister during most of World War II?")
            time.sleep(0.5)
            print("a) Neville Chamberlain")
            time.sleep(0.2)
            print("b) Winston Churchill")
            time.sleep(0.2)
            print("c) Margaret Thatcher")
            time.sleep(0.2)
            print("d) Clement Attlee")
            time.sleep(0.2)
            print("e) Tony Blair")
            time.sleep(0.2)
            simple_answer8 = input("Answer [a/b/c/d/e]: ")
            simple_correct8 = "b"

            if simple_answer8.lower() == simple_correct8:
                simple_total += 1

            time.sleep(0.7)
            print("\nQuestion 9: Which empire was ruled by Julius Caesar?")
            time.sleep(0.5)
            print("a) The Egyptian Empire")
            time.sleep(0.2)
            print("b) The Greek Empire")
            time.sleep(0.2)
            print("c) The Roman Empire")
            time.sleep(0.2)
            print("d) The Ottoman Empire")
            time.sleep(0.2)
            print("e) The Byzantine Empire")
            time.sleep(0.2)
            simple_answer9 = input("Answer [a/b/c/d/e]: ")
            simple_correct9 = "c"

            if simple_answer9.lower() == simple_correct9:
                simple_total += 1

            time.sleep(0.7)
            print("\nQuestion 10: What wall divided East and West Berlin from 1961 to 1989?")
            time.sleep(0.5)
            print("a) The Iron Curtain")
            time.sleep(0.2)
            print("b) The Berlin Wall")
            time.sleep(0.2)
            print("c) The Great Wall")
            time.sleep(0.2)
            print("d) The Western Wall")
            time.sleep(0.2)
            print("e) The Bamboo Curtain")
            time.sleep(0.2)
            simple_answer10 = input("Answer [a/b/c/d/e]: ")
            simple_correct10 = "b"

            if simple_answer10.lower() == simple_correct10:
                simple_total += 1

            totals("history", simple_total, intermediate_total, advanced_total)

        elif difficulty == 2:

            time.sleep(0.7)
            print("\nQuestion 1: Which document was signed in 1215 that limited the power of the English monarchy?")
            time.sleep(0.5)
            print("a) The Bill of Rights")
            time.sleep(0.2)
            print("b) The Magna Carta")
            time.sleep(0.2)
            print("c) The Treaty of Versailles")
            time.sleep(0.2)
            print("d) The Declaration of Independence")
            time.sleep(0.2)
            print("e) The Edict of Nantes")
            time.sleep(0.2)
            intermediate_answer1 = input("Answer [a/b/c/d/e]: ")
            intermediate_correct1 = "b"

            if intermediate_answer1.lower() == intermediate_correct1:
                intermediate_total += 1

            time.sleep(0.7)
            print("\nQuestion 2: Who was the first Emperor of China?")
            time.sleep(0.5)
            print("a) Qin Shi Huang")
            time.sleep(0.2)
            print("b) Sun Yat-sen")
            time.sleep(0.2)
            print("c) Mao Zedong")
            time.sleep(0.2)
            print("d) Liu Bang")
            time.sleep(0.2)
            print("e) Zhu Yuanzhang")
            time.sleep(0.2)
            intermediate_answer2 = input("Answer [a/b/c/d/e]: ")
            intermediate_correct2 = "a"

            if intermediate_answer2.lower() == intermediate_correct2:
                intermediate_total += 1

            time.sleep(0.7)
            print("\nQuestion 3: The ancient city of Troy was located in which modern-day country?")
            time.sleep(0.5)
            print("a) Greece")
            time.sleep(0.2)
            print("b) Turkey")
            time.sleep(0.2)
            print("c) Italy")
            time.sleep(0.2)
            print("d) Egypt")
            time.sleep(0.2)
            print("e) Syria")
            time.sleep(0.2)
            intermediate_answer3 = input("Answer [a/b/c/d/e]: ")
            intermediate_correct3 = "b"

            if intermediate_answer3.lower() == intermediate_correct3:
                intermediate_total += 1

            time.sleep(0.7)
            print("\nQuestion 4: Who was the longest-reigning British monarch before Queen Elizabeth II?")
            time.sleep(0.5)
            print("a) King George III")
            time.sleep(0.2)
            print("b) Queen Victoria")
            time.sleep(0.2)
            print("c) King Henry VIII")
            time.sleep(0.2)
            print("d) Queen Elizabeth I")
            time.sleep(0.2)
            print("e) King Edward VII")
            time.sleep(0.2)
            intermediate_answer4 = input("Answer [a/b/c/d/e]: ")
            intermediate_correct4 = "b"

            if intermediate_answer4.lower() == intermediate_correct4:
                intermediate_total += 1

            time.sleep(0.7)
            print("\nQuestion 5: Which empire was known as the 'Empire on which the sun never sets'?")
            time.sleep(0.5)
            print("a) The Ottoman Empire")
            time.sleep(0.2)
            print("b) The Mongol Empire")
            time.sleep(0.2)
            print("c) The British Empire")
            time.sleep(0.2)
            print("d) The Roman Empire")
            time.sleep(0.2)
            print("e) The Spanish Empire")
            time.sleep(0.2)
            intermediate_answer5 = input("Answer [a/b/c/d/e]: ")
            intermediate_correct5 = "c"

            if intermediate_answer5.lower() == intermediate_correct5:
                intermediate_total += 1

            time.sleep(0.7)
            print("\nQuestion 6: What event is considered the start of the French Revolution?")
            time.sleep(0.5)
            print("a) The Reign of Terror")
            time.sleep(0.2)
            print("b) The Storming of the Bastille")
            time.sleep(0.2)
            print("c) The Tennis Court Oath")
            time.sleep(0.2)
            print("d) The Women's March on Versailles")
            time.sleep(0.2)
            print("e) The execution of Louis XVI")
            time.sleep(0.2)
            intermediate_answer6 = input("Answer [a/b/c/d/e]: ")
            intermediate_correct6 = "b"

            if intermediate_answer6.lower() == intermediate_correct6:
                intermediate_total += 1
            
            time.sleep(0.7)
            print("\nQuestion 7: Who was the leader of the Soviet Union during World War II?")
            time.sleep(0.5)
            print("a) Vladimir Lenin")
            time.sleep(0.2)
            print("b) Nikita Khrushchev")
            time.sleep(0.2)
            print("c) Joseph Stalin")
            time.sleep(0.2)
            print("d) Leon Trotsky")
            time.sleep(0.2)
            print("e) Mikhail Gorbachev")
            time.sleep(0.2)
            intermediate_answer7 = input("Answer [a/b/c/d/e]: ")
            intermediate_correct7 = "c"

            if intermediate_answer7.lower() == intermediate_correct7:
                intermediate_total += 1

            time.sleep(0.7)
            print("\nQuestion 8: Which battle is considered the turning point in the Pacific Theater during World War II?")
            time.sleep(0.5)
            print("a) Battle of Coral Sea")
            time.sleep(0.2)
            print("b) Battle of Midway")
            time.sleep(0.2)
            print("c) Battle of Guadalcanal")
            time.sleep(0.2)
            print("d) Battle of Leyte Gulf")
            time.sleep(0.2)
            print("e) Battle of Iwo Jima")
            time.sleep(0.2)
            intermediate_answer8 = input("Answer [a/b/c/d/e]: ")
            intermediate_correct8 = "b"

            if intermediate_answer8.lower() == intermediate_correct8:
                intermediate_total += 1

            time.sleep(0.7)
            print("\nQuestion 9: What was the primary purpose of the Berlin Conference of 1884-1885?")
            time.sleep(0.5)
            print("a) To divide the African continent among European powers")
            time.sleep(0.2)
            print("b) To establish rules for trade in Asia")
            time.sleep(0.2)
            print("c) To negotiate peace between Germany and France")
            time.sleep(0.2)
            print("d) To end the Opium Wars")
            time.sleep(0.2)
            print("e) To create the League of Nations")
            time.sleep(0.2)
            intermediate_answer9 = input("Answer [a/b/c/d/e]: ")
            intermediate_correct9 = "a"

            if intermediate_answer9.lower() == intermediate_correct9:
                intermediate_total += 1

            time.sleep(0.7)
            print("\nQuestion 10: Who was the first man to circumnavigate the globe?")
            time.sleep(0.5)
            print("a) Christopher Columbus")
            time.sleep(0.2)
            print("b) Vasco da Gama")
            time.sleep(0.2)
            print("c) Ferdinand Magellan")
            time.sleep(0.2)
            print("d) James Cook")
            time.sleep(0.2)
            print("e) Amerigo Vespucci")
            time.sleep(0.2)
            intermediate_answer10 = input("Answer [a/b/c/d/e]: ")
            intermediate_correct10 = "c"

            if intermediate_answer10.lower() == intermediate_correct10:
                intermediate_total += 1

            totals("history", simple_total, intermediate_total, advanced_total)

        elif difficulty == 3:
            
            time.sleep(0.7)
            print("\nQuestion 1: Which war was triggered by the assassination of Archduke Franz Ferdinand?")
            time.sleep(0.5)
            print("a) The Napoleonic Wars")
            time.sleep(0.2)
            print("b) World War I")
            time.sleep(0.2)
            print("c) World War II")
            time.sleep(0.2)
            print("d) The Franco-Prussian War")
            time.sleep(0.2)
            print("e) The Crimean War")
            time.sleep(0.2)
            advanced_answer1 = input("Answer [a/b/c/d/e]: ")
            advanced_correct1 = "b"

            if advanced_answer1.lower() == advanced_correct1:
                advanced_total += 1

            time.sleep(0.7)
            print("\nQuestion 2: Who was the first ruler to unite the Mongol tribes under his leadership?")
            time.sleep(0.5)
            print("a) Kublai Khan")
            time.sleep(0.2)
            print("b) Ogedei Khan")
            time.sleep(0.2)
            print("c) Genghis Khan")
            time.sleep(0.2)
            print("d) Batu Khan")
            time.sleep(0.2)
            print("e) Timur")
            time.sleep(0.2)
            advanced_answer2 = input("Answer [a/b/c/d/e]: ")
            advanced_correct2 = "c"

            if advanced_answer2.lower() == advanced_correct2:
                advanced_total += 1

            time.sleep(0.7)
            print("\nQuestion 3: What ancient law code is famous for the phrase 'an eye for an eye'?")
            time.sleep(0.5)
            print("a) The Ten Commandments")
            time.sleep(0.2)
            print("b) The Code of Hammurabi")
            time.sleep(0.2)
            print("c) The Twelve Tables")
            time.sleep(0.2)
            print("d) The Magna Carta")
            time.sleep(0.2)
            print("e) The Edicts of Ashoka")
            time.sleep(0.2)
            advanced_answer3 = input("Answer [a/b/c/d/e]: ")
            advanced_correct3 = "b"

            if advanced_answer3.lower() == advanced_correct3:
                advanced_total += 1

            time.sleep(0.7)
            print("\nQuestion 4: Which civilization is credited with the invention of writing?")
            time.sleep(0.5)
            print("a) The Egyptians")
            time.sleep(0.2)
            print("b) The Sumerians")
            time.sleep(0.2)
            print("c) The Phoenicians")
            time.sleep(0.2)
            print("d) The Greeks")
            time.sleep(0.2)
            print("e) The Chinese")
            time.sleep(0.2)
            advanced_answer4 = input("Answer [a/b/c/d/e]: ")
            advanced_correct4 = "b"

            if advanced_answer4.lower() == advanced_correct4:
                advanced_total += 1

            time.sleep(0.7)
            print("\nQuestion 5: Who was the principal author of the Declaration of Independence?")
            time.sleep(0.5)
            print("a) John Adams")
            time.sleep(0.2)
            print("b) Benjamin Franklin")
            time.sleep(0.2)
            print("c) Thomas Jefferson")
            time.sleep(0.2)
            print("d) James Madison")
            time.sleep(0.2)
            print("e) Alexander Hamilton")
            time.sleep(0.2)
            advanced_answer5 = input("Answer [a/b/c/d/e]: ")
            advanced_correct5 = "c"

            if advanced_answer5.lower() == advanced_correct5:
                advanced_total += 1

            time.sleep(0.7)
            print("\nQuestion 6: Which empire is known for constructing the ancient city of Machu Picchu?")
            time.sleep(0.5)
            print("a) The Aztec Empire")
            time.sleep(0.2)
            print("b) The Maya Empire")
            time.sleep(0.2)
            print("c) The Inca Empire")
            time.sleep(0.2)
            print("d) The Olmec Empire")
            time.sleep(0.2)
            print("e) The Toltec Empire")
            time.sleep(0.2)
            advanced_answer6 = input("Answer [a/b/c/d/e]: ")
            advanced_correct6 = "c"

            if advanced_answer6.lower() == advanced_correct6:
                advanced_total += 1
            
            time.sleep(0.7)
            print("\nQuestion 7: What was the primary goal of the Crusades?")
            time.sleep(0.5)
            print("a) To spread Christianity to the Americas")
            time.sleep(0.2)
            print("b) To reconquer Spain from the Moors")
            time.sleep(0.2)
            print("c) To recapture the Holy Land from Muslim control")
            time.sleep(0.2)
            print("d) To establish trade routes to Asia")
            time.sleep(0.2)
            print("e) To stop the spread of Protestantism in Europe")
            time.sleep(0.2)
            advanced_answer7 = input("Answer [a/b/c/d/e]: ")
            advanced_correct7 = "c"

            if advanced_answer7.lower() == advanced_correct7:
                advanced_total += 1

            time.sleep(0.7)
            print("\nQuestion 8: Who was the last emperor of Russia, overthrown in 1917?")
            time.sleep(0.5)
            print("a) Peter the Great")
            time.sleep(0.2)
            print("b) Nicholas II")
            time.sleep(0.2)
            print("c) Alexander II")
            time.sleep(0.2)
            print("d) Ivan the Terrible")
            time.sleep(0.2)
            print("e) Catherine the Great")
            time.sleep(0.2)
            advanced_answer8 = input("Answer [a/b/c/d/e]: ")
            advanced_correct8 = "b"

            if advanced_answer8.lower() == advanced_correct8:
                advanced_total += 1

            time.sleep(0.7)
            print("\nQuestion 9: What treaty ended World War I?")
            time.sleep(0.5)
            print("a) The Treaty of Paris")
            time.sleep(0.2)
            print("b) The Treaty of Tordesillas")
            time.sleep(0.2)
            print("c) The Treaty of Versailles")
            time.sleep(0.2)
            print("d) The Treaty of Utrecht")
            time.sleep(0.2)
            print("e) The Treaty of Brest-Litovsk")
            time.sleep(0.2)
            advanced_answer9 = input("Answer [a/b/c/d/e]: ")
            advanced_correct9 = "c"

            if advanced_answer9.lower() == advanced_correct9:
                advanced_total += 1

            time.sleep(0.7)
            print("\nQuestion 10: Who was the philosopher who tutored Alexander the Great?")
            time.sleep(0.5)
            print("a) Plato")
            time.sleep(0.2)
            print("b) Aristotle")
            time.sleep(0.2)
            print("c) Socrates")
            time.sleep(0.2)
            print("d) Heraclitus")
            time.sleep(0.2)
            print("e) Pythagoras")
            time.sleep(0.2)
            advanced_answer10 = input("Answer [a/b/c/d/e]: ")
            advanced_correct10 = "b"

            if advanced_answer10.lower() == advanced_correct10:
                advanced_total += 1

            totals("history", simple_total, intermediate_total, advanced_total)

    except ValueError as v:
        print(f"\nAn Error Occurred: {v}")
        time.sleep(1)
        print("You will be brought back to the start of the quiz. Please input either a,b,c,d,e as your answer to continue.")
        time.sleep(2)
        general_quiz(difficulty)
    except Exception as e:
        print(f"\nAn Error Occurred: {e}")
        time.sleep(1)
        print("The program will now restart, please ensure you follow the instructions properly.")
        time.sleep(2)
        start()

def sports_quiz(difficulty):
    
    simple_total = 0
    intermediate_total = 0
    advanced_total = 0

    try:
        if difficulty == 1:

            time.sleep(0.7)
            print("\nQuestion 1: Which country won the FIFA World Cup in 2018?")
            time.sleep(0.5)
            print("a) Brazil")
            time.sleep(0.2)
            print("b) Germany")
            time.sleep(0.2)
            print("c) Argentina")
            time.sleep(0.2)
            print("d) France")
            time.sleep(0.2)
            print("e) Spain")
            time.sleep(0.2)
            simple_answer1 = input("Answer [a/b/c/d/e]: ")
            simple_correct1 = "d"

            if simple_answer1.lower() == simple_correct1:
                simple_total += 1

            time.sleep(0.7)
            print("\nQuestion 2: What sport is known as 'The Beautiful Game'?")
            time.sleep(0.5)
            print("a) Basketball")
            time.sleep(0.2)
            print("b) Tennis")
            time.sleep(0.2)
            print("c) Football (Soccer)")
            time.sleep(0.2)
            print("d) Rugby")
            time.sleep(0.2)
            print("e) Cricket")
            time.sleep(0.2)
            simple_answer2 = input("Answer [a/b/c/d/e]: ")
            simple_correct2 = "c"

            if simple_answer2.lower() == simple_correct2:
                simple_total += 1

            time.sleep(0.7)
            print("\nQuestion 3: How many players are on a baseball team?")
            time.sleep(0.5)
            print("a) 7")
            time.sleep(0.2)
            print("b) 8")
            time.sleep(0.2)
            print("c) 9")
            time.sleep(0.2)
            print("d) 10")
            time.sleep(0.2)
            print("e) 11")
            time.sleep(0.2)
            simple_answer3 = input("Answer [a/b/c/d/e]: ")
            simple_correct3 = "c"

            if simple_answer3.lower() == simple_correct3:
                simple_total += 1

            time.sleep(0.7)
            print("\nQuestion 4: Which country is famous for originating the sport of cricket?")
            time.sleep(0.5)
            print("a) Australia")
            time.sleep(0.2)
            print("b) India")
            time.sleep(0.2)
            print("c) South Africa")
            time.sleep(0.2)
            print("d) England")
            time.sleep(0.2)
            print("e) New Zealand")
            time.sleep(0.2)
            simple_answer4 = input("Answer [a/b/c/d/e]: ")
            simple_correct4 = "d"

            if simple_answer4.lower() == simple_correct4:
                simple_total += 1

            time.sleep(0.7)
            print("\nQuestion 5: In what sport do players compete for the Stanley Cup?")
            time.sleep(0.5)
            print("a) Basketball")
            time.sleep(0.2)
            print("b) Ice Hockey")
            time.sleep(0.2)
            print("c) Football (American)")
            time.sleep(0.2)
            print("d) Baseball")
            time.sleep(0.2)
            print("e) Rugby")
            time.sleep(0.2)
            simple_answer5 = input("Answer [a/b/c/d/e]: ")
            simple_correct5 = "b"

            if simple_answer5.lower() == simple_correct5:
                simple_total += 1

            time.sleep(0.7)
            print("\nQuestion 6: How long is a marathon?")
            time.sleep(0.5)
            print("a) 21.1 km")
            time.sleep(0.2)
            print("b) 26.2 miles")
            time.sleep(0.2)
            print("c) 42.2 miles")
            time.sleep(0.2)
            print("d) 10 km")
            time.sleep(0.2)
            print("e) 5 km")
            time.sleep(0.2)
            simple_answer6 = input("Answer [a/b/c/d/e]: ")
            simple_correct6 = "b"

            if simple_answer6.lower() == simple_correct6:
                simple_total += 1
            
            time.sleep(0.7)
            print("\nQuestion 7: Which sport uses a term called 'love' for a score of zero?")
            time.sleep(0.5)
            print("a) Badminton")
            time.sleep(0.2)
            print("b) Tennis")
            time.sleep(0.2)
            print("c) Squash")
            time.sleep(0.2)
            print("d) Volleyball")
            time.sleep(0.2)
            print("e) Table Tennis")
            time.sleep(0.2)
            simple_answer7 = input("Answer [a/b/c/d/e]: ")
            simple_correct7 = "b"

            if simple_answer7.lower() == simple_correct7:
                simple_total += 1

            time.sleep(0.7)
            print("\nQuestion 8: Which country has won the most Olympic gold medals in history?")
            time.sleep(0.5)
            print("a) Russia")
            time.sleep(0.2)
            print("b) China")
            time.sleep(0.2)
            print("c) Germany")
            time.sleep(0.2)
            print("d) United States")
            time.sleep(0.2)
            print("e) Great Britain")
            time.sleep(0.2)
            simple_answer8 = input("Answer [a/b/c/d/e]: ")
            simple_correct8 = "d"

            if simple_answer8.lower() == simple_correct8:
                simple_total += 1

            time.sleep(0.7)
            print("\nQuestion 9: What is the national sport of Japan?")
            time.sleep(0.5)
            print("a) Judo")
            time.sleep(0.2)
            print("b) Sumo Wrestling")
            time.sleep(0.2)
            print("c) Baseball")
            time.sleep(0.2)
            print("d) Karate")
            time.sleep(0.2)
            print("e) Kendo")
            time.sleep(0.2)
            simple_answer9 = input("Answer [a/b/c/d/e]: ")
            simple_correct9 = "b"

            if simple_answer9.lower() == simple_correct9:
                simple_total += 1

            time.sleep(0.7)
            print("\nQuestion 10: Who holds the record for the most goals in a single World Cup tournament?")
            time.sleep(0.5)
            print("a) Pelé")
            time.sleep(0.2)
            print("b) Miroslav Klose")
            time.sleep(0.2)
            print("c) Just Fontaine")
            time.sleep(0.2)
            print("d) Ronaldo Nazário")
            time.sleep(0.2)
            print("e) Lionel Messi")
            time.sleep(0.2)
            simple_answer10 = input("Answer [a/b/c/d/e]: ")
            simple_correct10 = "c"

            if simple_answer10.lower() == simple_correct10:
                simple_total += 1

            totals("sports", simple_total, intermediate_total, advanced_total)

        elif difficulty == 2:

            time.sleep(0.7)
            print("Question 1: Who won the most recent Super Bowl as of 2023?")
            time.sleep(0.5)
            print("a) Kansas City Chiefs")
            time.sleep(0.2)
            print("b) Tampa Bay Buccaneers")
            time.sleep(0.2)
            print("c) San Francisco 49ers")
            time.sleep(0.2)
            print("d) Los Angeles Rams")
            time.sleep(0.2)
            print("e) Green Bay Packers")
            time.sleep(0.2)
            intermediate_answer1 = input("Answer [a/b/c/d/e]: ")
            intermediate_correct1 = "a"

            if intermediate_answer1.lower() == intermediate_correct1:
                intermediate_total += 1

            time.sleep(0.7)
            print("\nQuestion 2: In tennis, what is the term for a score of 40-40?")
            time.sleep(0.5)
            print("a) Love")
            time.sleep(0.2)
            print("b) Advantage")
            time.sleep(0.2)
            print("c) Deuce")
            time.sleep(0.2)
            print("d) Break Point")
            time.sleep(0.2)
            print("e) Game Point")
            time.sleep(0.2)
            intermediate_answer2 = input("Answer [a/b/c/d/e]: ")
            intermediate_correct2 = "c"

            if intermediate_answer2.lower() == intermediate_correct2:
                intermediate_total += 1

            time.sleep(0.7)
            print("\nQuestion 3: Which country won the first ever FIFA World Cup in 1930?")
            time.sleep(0.5)
            print("a) Brazil")
            time.sleep(0.2)
            print("b) Uruguay")
            time.sleep(0.2)
            print("c) Argentina")
            time.sleep(0.2)
            print("d) Italy")
            time.sleep(0.2)
            print("e) Germany")
            time.sleep(0.2)
            intermediate_answer3 = input("Answer [a/b/c/d/e]: ")
            intermediate_correct3 = "b"

            if intermediate_answer3.lower() == intermediate_correct3:
                intermediate_total += 1

            time.sleep(0.7)
            print("\nQuestion 4: Who is considered the fastest man in the world, holding the 100m world record?")
            time.sleep(0.5)
            print("a) Carl Lewis")
            time.sleep(0.2)
            print("b) Usain Bolt")
            time.sleep(0.2)
            print("c) Michael Johnson")
            time.sleep(0.2)
            print("d) Yohan Blake")
            time.sleep(0.2)
            print("e) Tyson Gay")
            time.sleep(0.2)
            intermediate_answer4 = input("Answer [a/b/c/d/e]: ")
            intermediate_correct4 = "b"

            if intermediate_answer4.lower() == intermediate_correct4:
                intermediate_total += 1

            time.sleep(0.7)
            print("\nQuestion 5: In which sport would you perform a slam dunk?")
            time.sleep(0.5)
            print("a) Volleyball")
            time.sleep(0.2)
            print("b) Basketball")
            time.sleep(0.2)
            print("c) Tennis")
            time.sleep(0.2)
            print("d) Rugby")
            time.sleep(0.2)
            print("e) Handball")
            time.sleep(0.2)
            intermediate_answer5 = input("Answer [a/b/c/d/e]: ")
            intermediate_correct5 = "b"

            if intermediate_answer5.lower() == intermediate_correct5:
                intermediate_total += 1

            time.sleep(0.7)
            print("\nQuestion 6: Which golfer has won the most major championships?")
            time.sleep(0.5)
            print("a) Tiger Woods")
            time.sleep(0.2)
            print("b) Arnold Palmer")
            time.sleep(0.2)
            print("c) Jack Nicklaus")
            time.sleep(0.2)
            print("d) Ben Hogan")
            time.sleep(0.2)
            print("e) Gary Player")
            time.sleep(0.2)
            intermediate_answer6 = input("Answer [a/b/c/d/e]: ")
            intermediate_correct6 = "c"

            if intermediate_answer6.lower() == intermediate_correct6:
                intermediate_total += 1
            
            time.sleep(0.7)
            print("\nQuestion 7: What is the only team in the NFL to have a perfect season, including the Super Bowl?")
            time.sleep(0.5)
            print("a) New England Patriots")
            time.sleep(0.2)
            print("b) Dallas Cowboys")
            time.sleep(0.2)
            print("c) Miami Dolphins")
            time.sleep(0.2)
            print("d) Pittsburgh Steelers")
            time.sleep(0.2)
            print("e) Green Bay Packers")
            time.sleep(0.2)
            intermediate_answer7 = input("Answer [a/b/c/d/e]: ")
            intermediate_correct7 = "c"

            if intermediate_answer7.lower() == intermediate_correct7:
                intermediate_total += 1

            time.sleep(0.7)
            print("\nQuestion 8: In what year did Roger Bannister break the 4-minute mile?")
            time.sleep(0.5)
            print("a) 1945")
            time.sleep(0.2)
            print("b) 1954")
            time.sleep(0.2)
            print("c) 1960")
            time.sleep(0.2)
            print("d) 1964")
            time.sleep(0.2)
            print("e) 1971")
            time.sleep(0.2)
            intermediate_answer8 = input("Answer [a/b/c/d/e]: ")
            intermediate_correct8 = "b"

            if intermediate_answer8.lower() == intermediate_correct8:
                intermediate_total += 1

            time.sleep(0.7)
            print("\nQuestion 9: Who was the first woman to win three Wimbledon titles in a row?")
            time.sleep(0.5)
            print("a) Steffi Graf")
            time.sleep(0.2)
            print("b) Serena Williams")
            time.sleep(0.2)
            print("c) Martina Navratilova")
            time.sleep(0.2)
            print("d) Margaret Court")
            time.sleep(0.2)
            print("e) Billie Jean King")
            time.sleep(0.2)
            intermediate_answer9 = input("Answer [a/b/c/d/e]: ")
            intermediate_correct9 = "c"

            if intermediate_answer9.lower() == intermediate_correct9:
                intermediate_total += 1

            time.sleep(0.7)
            print("\nQuestion 10: How many players are on a basketball team on the court at one time?")
            time.sleep(0.5)
            print("a) 4")
            time.sleep(0.2)
            print("b) 5")
            time.sleep(0.2)
            print("c) 6")
            time.sleep(0.2)
            print("d) 7")
            time.sleep(0.2)
            print("e) 8")
            time.sleep(0.2)
            intermediate_answer10 = input("Answer [a/b/c/d/e]: ")
            intermediate_correct10 = "b"

            if intermediate_answer10.lower() == intermediate_correct10:
                intermediate_total += 1

            totals("sports", simple_total, intermediate_total, advanced_total)

        elif difficulty == 3:
            
            time.sleep(0.7)
            print("Question 1: Which country hosted the first modern Olympic Games in 1896?")
            time.sleep(0.5)
            print("a) France")
            time.sleep(0.2)
            print("b) United States")
            time.sleep(0.2)
            print("c) Greece")
            time.sleep(0.2)
            print("d) United Kingdom")
            time.sleep(0.2)
            print("e) Germany")
            time.sleep(0.2)
            advanced_answer1 = input("Answer [a/b/c/d/e]: ")
            advanced_correct1 = "c"

            if advanced_answer1.lower() == advanced_correct1:
                advanced_total += 1

            time.sleep(0.7)
            print("\nQuestion 2: Who was the first athlete to win the Olympic decathlon twice?")
            time.sleep(0.5)
            print("a) Daley Thompson")
            time.sleep(0.2)
            print("b) Bruce Jenner")
            time.sleep(0.2)
            print("c) Rafer Johnson")
            time.sleep(0.2)
            print("d) Bob Mathias")
            time.sleep(0.2)
            print("e) Ashton Eaton")
            time.sleep(0.2)
            advanced_answer2 = input("Answer [a/b/c/d/e]: ")
            advanced_correct2 = "d"

            if advanced_answer2.lower() == advanced_correct2:
                advanced_total += 1

            time.sleep(0.7)
            print("\nQuestion 3: In what year was the first Rugby World Cup held?")
            time.sleep(0.5)
            print("a) 1983")
            time.sleep(0.2)
            print("b) 1985")
            time.sleep(0.2)
            print("c) 1987")
            time.sleep(0.2)
            print("d) 1989")
            time.sleep(0.2)
            print("e) 1991")
            time.sleep(0.2)
            advanced_answer3 = input("Answer [a/b/c/d/e]: ")
            advanced_correct3 = "c"

            if advanced_answer3.lower() == advanced_correct3:
                advanced_total += 1

            time.sleep(0.7)
            print("\nQuestion 4: Who has won the most NBA championships as a player?")
            time.sleep(0.5)
            print("a) Michael Jordan")
            time.sleep(0.2)
            print("b) Kobe Bryant")
            time.sleep(0.2)
            print("c) Bill Russell")
            time.sleep(0.2)
            print("d) Magic Johnson")
            time.sleep(0.2)
            print("e) Kareem Abdul-Jabbar")
            time.sleep(0.2)
            advanced_answer4 = input("Answer [a/b/c/d/e]: ")
            advanced_correct4 = "c"

            if advanced_answer4.lower() == advanced_correct4:
                advanced_total += 1

            time.sleep(0.7)
            print("\nQuestion 5: Which country has won the most Rugby World Cups?")
            time.sleep(0.5)
            print("a) New Zealand")
            time.sleep(0.2)
            print("b) South Africa")
            time.sleep(0.2)
            print("c) Australia")
            time.sleep(0.2)
            print("d) England")
            time.sleep(0.2)
            print("e) France")
            time.sleep(0.2)
            advanced_answer5 = input("Answer [a/b/c/d/e]: ")
            advanced_correct5 = "a"

            if advanced_answer5.lower() == advanced_correct5:
                advanced_total += 1

            time.sleep(0.7)
            print("\nQuestion 6: Who was the first African American to win a Grand Slam title in tennis?")
            time.sleep(0.5)
            print("a) Arthur Ashe")
            time.sleep(0.2)
            print("b) Althea Gibson")
            time.sleep(0.2)
            print("c) Serena Williams")
            time.sleep(0.2)
            print("d) Venus Williams")
            time.sleep(0.2)
            print("e) Yannick Noah")
            time.sleep(0.2)
            advanced_answer6 = input("Answer [a/b/c/d/e]: ")
            advanced_correct6 = "b"

            if advanced_answer6.lower() == advanced_correct6:
                advanced_total += 1
            
            time.sleep(0.7)
            print("\nQuestion 7: What is the maximum possible break in snooker?")
            time.sleep(0.5)
            print("a) 137")
            time.sleep(0.2)
            print("b) 140")
            time.sleep(0.2)
            print("c) 144")
            time.sleep(0.2)
            print("d) 147")
            time.sleep(0.2)
            print("e) 150")
            time.sleep(0.2)
            advanced_answer7 = input("Answer [a/b/c/d/e]: ")
            advanced_correct7 = "d"

            if advanced_answer7.lower() == advanced_correct7:
                advanced_total += 1

            time.sleep(0.7)
            print("\nQuestion 8: Who holds the record for the most goals scored in the Premier League in a single season?")
            time.sleep(0.5)
            print("a) Alan Shearer")
            time.sleep(0.2)
            print("b) Thierry Henry")
            time.sleep(0.2)
            print("c) Mohamed Salah")
            time.sleep(0.2)
            print("d) Harry Kane")
            time.sleep(0.2)
            print("e) Cristiano Ronaldo")
            time.sleep(0.2)
            advanced_answer8 = input("Answer [a/b/c/d/e]: ")
            advanced_correct8 = "c"

            if advanced_answer8.lower() == advanced_correct8:
                advanced_total += 1

            time.sleep(0.7)
            print("\nQuestion 9: What is the only Grand Slam tennis tournament played on clay?")
            time.sleep(0.5)
            print("a) Wimbledon")
            time.sleep(0.2)
            print("b) Australian Open")
            time.sleep(0.2)
            print("c) French Open")
            time.sleep(0.2)
            print("d) US Open")
            time.sleep(0.2)
            print("e) None")
            time.sleep(0.2)
            advanced_answer9 = input("Answer [a/b/c/d/e]: ")
            advanced_correct9 = "c"

            if advanced_answer9.lower() == advanced_correct9:
                advanced_total += 1

            time.sleep(0.7)
            print("\nQuestion 10: In which year did the Chicago Cubs break their 108-year World Series drought?")
            time.sleep(0.5)
            print("a) 2015")
            time.sleep(0.2)
            print("b) 2016")
            time.sleep(0.2)
            print("c) 2017")
            time.sleep(0.2)
            print("d) 2018")
            time.sleep(0.2)
            print("e) 2019")
            time.sleep(0.2)
            advanced_answer10 = input("Answer [a/b/c/d/e]: ")
            advanced_correct10 = "b"

            if advanced_answer10.lower() == advanced_correct10:
                advanced_total += 1

            totals("sports", simple_total, intermediate_total, advanced_total)

    except ValueError as v:
        print(f"\nAn Error Occurred: {v}")
        time.sleep(1)
        print("You will be brought back to the start of the quiz. Please input either a,b,c,d,e as your answer to continue.")
        time.sleep(2)
        general_quiz(difficulty)
    except Exception as e:
        print(f"\nAn Error Occurred: {e}")
        time.sleep(1)
        print("The program will now restart, please ensure you follow the instructions properly.")
        time.sleep(2)
        start()

def movies_quiz(difficulty):
    
    simple_total = 0
    intermediate_total = 0
    advanced_total = 0

    try:
        if difficulty == 1:

            time.sleep(0.7)
            print("Question 1: Which movie features the song 'My Heart Will Go On'?")
            time.sleep(0.5)
            print("a) The Bodyguard")
            time.sleep(0.2)
            print("b) Titanic")
            time.sleep(0.2)
            print("c) Ghost")
            time.sleep(0.2)
            print("d) Armageddon")
            time.sleep(0.2)
            print("e) The Lion King")
            time.sleep(0.2)
            simple_answer1 = input("Answer [a/b/c/d/e]: ")
            simple_correct1 = "b"

            if simple_answer1.lower() == simple_correct1:
                simple_total += 1

            time.sleep(0.7)
            print("\nQuestion 2: Who played the role of Harry Potter in the film series?")
            time.sleep(0.5)
            print("a) Elijah Wood")
            time.sleep(0.2)
            print("b) Daniel Radcliffe")
            time.sleep(0.2)
            print("c) Rupert Grint")
            time.sleep(0.2)
            print("d) Tom Felton")
            time.sleep(0.2)
            print("e) Robert Pattinson")
            time.sleep(0.2)
            simple_answer2 = input("Answer [a/b/c/d/e]: ")
            simple_correct2 = "b"

            if simple_answer2.lower() == simple_correct2:
                simple_total += 1

            time.sleep(0.7)
            print("\nQuestion 3: In which movie does Tom Hanks say, 'Life is like a box of chocolates'?")
            time.sleep(0.5)
            print("a) Forrest Gump")
            time.sleep(0.2)
            print("b) Cast Away")
            time.sleep(0.2)
            print("c) Saving Private Ryan")
            time.sleep(0.2)
            print("d) The Green Mile")
            time.sleep(0.2)
            print("e) Big")
            time.sleep(0.2)
            simple_answer3 = input("Answer [a/b/c/d/e]: ")
            simple_correct3 = "a"

            if simple_answer3.lower() == simple_correct3:
                simple_total += 1

            time.sleep(0.7)
            print("\nQuestion 4: What is the name of the kingdom where the 2013 animated movie 'Frozen' is set?")
            time.sleep(0.5)
            print("a) Arendelle")
            time.sleep(0.2)
            print("b) DunBroch")
            time.sleep(0.2)
            print("c) Corona")
            time.sleep(0.2)
            print("d) Atlantica")
            time.sleep(0.2)
            print("e) Eldorado")
            time.sleep(0.2)
            simple_answer4 = input("Answer [a/b/c/d/e]: ")
            simple_correct4 = "a"

            if simple_answer4.lower() == simple_correct4:
                simple_total += 1

            time.sleep(0.7)
            print("\nQuestion 5: Which actor played the Joker in the 2008 movie 'The Dark Knight'?")
            time.sleep(0.5)
            print("a) Jack Nicholson")
            time.sleep(0.2)
            print("b) Jared Leto")
            time.sleep(0.2)
            print("c) Joaquin Phoenix")
            time.sleep(0.2)
            print("d) Heath Ledger")
            time.sleep(0.2)
            print("e) Mark Hamill")
            time.sleep(0.2)
            simple_answer5 = input("Answer [a/b/c/d/e]: ")
            simple_correct5 = "d"

            if simple_answer5.lower() == simple_correct5:
                simple_total += 1

            time.sleep(0.7)
            print("\nQuestion 6: What is the highest-grossing film of all time (as of 2023)?")
            time.sleep(0.5)
            print("a) Avatar")
            time.sleep(0.2)
            print("b) Avengers: Endgame")
            time.sleep(0.2)
            print("c) Titanic")
            time.sleep(0.2)
            print("d) Star Wars: The Force Awakens")
            time.sleep(0.2)
            print("e) Jurassic World")
            time.sleep(0.2)
            simple_answer6 = input("Answer [a/b/c/d/e]: ")
            simple_correct6 = "a"

            if simple_answer6.lower() == simple_correct6:
                simple_total += 1
            
            time.sleep(0.7)
            print("\nQuestion 7: Who directed the movie 'Jurassic Park' released in 1993?")
            time.sleep(0.5)
            print("a) James Cameron")
            time.sleep(0.2)
            print("b) Steven Spielberg")
            time.sleep(0.2)
            print("c) George Lucas")
            time.sleep(0.2)
            print("d) Ridley Scott")
            time.sleep(0.2)
            print("e) Peter Jackson")
            time.sleep(0.2)
            simple_answer7 = input("Answer [a/b/c/d/e]: ")
            simple_correct7 = "b"

            if simple_answer7.lower() == simple_correct7:
                simple_total += 1

            time.sleep(0.7)
            print("\nQuestion 8: Which film won the Academy Award for Best Picture in 1994?")
            time.sleep(0.5)
            print("a) Pulp Fiction")
            time.sleep(0.2)
            print("b) The Shawshank Redemption")
            time.sleep(0.2)
            print("c) Forrest Gump")
            time.sleep(0.2)
            print("d) Four Weddings and a Funeral")
            time.sleep(0.2)
            print("e) Quiz Show")
            time.sleep(0.2)
            simple_answer8 = input("Answer [a/b/c/d/e]: ")
            simple_correct8 = "c"

            if simple_answer8.lower() == simple_correct8:
                simple_total += 1

            time.sleep(0.7)
            print("\nQuestion 9: In which movie did Keanu Reeves play the character Neo?")
            time.sleep(0.5)
            print("a) Speed")
            time.sleep(0.2)
            print("b) Point Break")
            time.sleep(0.2)
            print("c) John Wick")
            time.sleep(0.2)
            print("d) The Matrix")
            time.sleep(0.2)
            print("e) Constantine")
            time.sleep(0.2)
            simple_answer9 = input("Answer [a/b/c/d/e]: ")
            simple_correct9 = "d"

            if simple_answer9.lower() == simple_correct9:
                simple_total += 1

            time.sleep(0.7)
            print("\nQuestion 10: What is the name of the hobbit played by Elijah Wood in the 'Lord of the Rings' movies?")
            time.sleep(0.5)
            print("a) Samwise Gamgee")
            time.sleep(0.2)
            print("b) Frodo Baggins")
            time.sleep(0.2)
            print("c) Bilbo Baggins")
            time.sleep(0.2)
            print("d) Peregrin Took")
            time.sleep(0.2)
            print("e) Meriadoc Brandybuck")
            time.sleep(0.2)
            simple_answer10 = input("Answer [a/b/c/d/e]: ")
            simple_correct10 = "b"

            if simple_answer10.lower() == simple_correct10:
                simple_total += 1

            totals("movies", simple_total, intermediate_total, advanced_total)

        elif difficulty == 2:

            time.sleep(0.7)
            print("Question 1: Which movie features the character Tyler Durden?")
            time.sleep(0.5)
            print("a) The Usual Suspects")
            time.sleep(0.2)
            print("b) Fight Club")
            time.sleep(0.2)
            print("c) The Big Lebowski")
            time.sleep(0.2)
            print("d) American Psycho")
            time.sleep(0.2)
            print("e) Memento")
            time.sleep(0.2)
            intermediate_answer1 = input("Answer [a/b/c/d/e]: ")
            intermediate_correct1 = "b"

            if intermediate_answer1.lower() == intermediate_correct1:
                intermediate_total += 1

            time.sleep(0.7)
            print("\nQuestion 2: Who directed the movie 'Inception'?")
            time.sleep(0.5)
            print("a) Christopher Nolan")
            time.sleep(0.2)
            print("b) Quentin Tarantino")
            time.sleep(0.2)
            print("c) David Fincher")
            time.sleep(0.2)
            print("d) Martin Scorsese")
            time.sleep(0.2)
            print("e) James Cameron")
            time.sleep(0.2)
            intermediate_answer2 = input("Answer [a/b/c/d/e]: ")
            intermediate_correct2 = "a"

            if intermediate_answer2.lower() == intermediate_correct2:
                intermediate_total += 1

            time.sleep(0.7)
            print("\nQuestion 3: Which actress starred as Katniss Everdeen in 'The Hunger Games' series?")
            time.sleep(0.5)
            print("a) Emma Stone")
            time.sleep(0.2)
            print("b) Shailene Woodley")
            time.sleep(0.2)
            print("c) Jennifer Lawrence")
            time.sleep(0.2)
            print("d) Kristen Stewart")
            time.sleep(0.2)
            print("e) Margot Robbie")
            time.sleep(0.2)
            intermediate_answer3 = input("Answer [a/b/c/d/e]: ")
            intermediate_correct3 = "c"

            if intermediate_answer3.lower() == intermediate_correct3:
                intermediate_total += 1

            time.sleep(0.7)
            print("\nQuestion 4: In which movie did Tom Cruise famously say, 'Show me the money!'?")
            time.sleep(0.5)
            print("a) Top Gun")
            time.sleep(0.2)
            print("b) Jerry Maguire")
            time.sleep(0.2)
            print("c) A Few Good Men")
            time.sleep(0.2)
            print("d) Rain Man")
            time.sleep(0.2)
            print("e) Risky Business")
            time.sleep(0.2)
            intermediate_answer4 = input("Answer [a/b/c/d/e]: ")
            intermediate_correct4 = "b"

            if intermediate_answer4.lower() == intermediate_correct4:
                intermediate_total += 1

            time.sleep(0.7)
            print("\nQuestion 5: Who won the Academy Award for Best Actor in 2020?")
            time.sleep(0.5)
            print("a) Leonardo DiCaprio")
            time.sleep(0.2)
            print("b) Joaquin Phoenix")
            time.sleep(0.2)
            print("c) Brad Pitt")
            time.sleep(0.2)
            print("d) Adam Driver")
            time.sleep(0.2)
            print("e) Antonio Banderas")
            time.sleep(0.2)
            intermediate_answer5 = input("Answer [a/b/c/d/e]: ")
            intermediate_correct5 = "b"

            if intermediate_answer5.lower() == intermediate_correct5:
                intermediate_total += 1

            time.sleep(0.7)
            print("\nQuestion 6: Which movie is based on the life of mathematician John Nash?")
            time.sleep(0.5)
            print("a) The Imitation Game")
            time.sleep(0.2)
            print("b) The Theory of Everything")
            time.sleep(0.2)
            print("c) A Beautiful Mind")
            time.sleep(0.2)
            print("d) Good Will Hunting")
            time.sleep(0.2)
            print("e) Pi")
            time.sleep(0.2)
            intermediate_answer6 = input("Answer [a/b/c/d/e]: ")
            intermediate_correct6 = "c"

            if intermediate_answer6.lower() == intermediate_correct6:
                intermediate_total += 1
            
            time.sleep(0.7)
            print("\nQuestion 7: Who directed the 1972 movie 'The Godfather'?")
            time.sleep(0.5)
            print("a) Martin Scorsese")
            time.sleep(0.2)
            print("b) Francis Ford Coppola")
            time.sleep(0.2)
            print("c) Stanley Kubrick")
            time.sleep(0.2)
            print("d) Brian De Palma")
            time.sleep(0.2)
            print("e) Sergio Leone")
            time.sleep(0.2)
            intermediate_answer7 = input("Answer [a/b/c/d/e]: ")
            intermediate_correct7 = "b"

            if intermediate_answer7.lower() == intermediate_correct7:
                intermediate_total += 1

            time.sleep(0.7)
            print("\nQuestion 8: Which film features the quote, 'Here's looking at you, kid'?")
            time.sleep(0.5)
            print("a) Casablanca")
            time.sleep(0.2)
            print("b) Gone with the Wind")
            time.sleep(0.2)
            print("c) Citizen Kane")
            time.sleep(0.2)
            print("d) The Maltese Falcon")
            time.sleep(0.2)
            print("e) Sunset Boulevard")
            time.sleep(0.2)
            intermediate_answer8 = input("Answer [a/b/c/d/e]: ")
            intermediate_correct8 = "a"

            if intermediate_answer8.lower() == intermediate_correct8:
                intermediate_total += 1

            time.sleep(0.7)
            print("\nQuestion 9: Which actor played the role of Wolverine in the X-Men movies?")
            time.sleep(0.5)
            print("a) Hugh Jackman")
            time.sleep(0.2)
            print("b) Robert Downey Jr.")
            time.sleep(0.2)
            print("c) Chris Hemsworth")
            time.sleep(0.2)
            print("d) Ryan Reynolds")
            time.sleep(0.2)
            print("e) Tom Hardy")
            time.sleep(0.2)
            intermediate_answer9 = input("Answer [a/b/c/d/e]: ")
            intermediate_correct9 = "a"

            if intermediate_answer9.lower() == intermediate_correct9:
                intermediate_total += 1

            time.sleep(0.7)
            print("\nQuestion 10: What is the name of the AI character in the 1968 film '2001: A Space Odyssey'?")
            time.sleep(0.5)
            print("a) Skynet")
            time.sleep(0.2)
            print("b) HAL 9000")
            time.sleep(0.2)
            print("c) GLaDOS")
            time.sleep(0.2)
            print("d) JARVIS")
            time.sleep(0.2)
            print("e) Ultron")
            time.sleep(0.2)
            intermediate_answer10 = input("Answer [a/b/c/d/e]: ")
            intermediate_correct10 = "b"

            if intermediate_answer10.lower() == intermediate_correct10:
                intermediate_total += 1

            totals("movies", simple_total, intermediate_total, advanced_total)

        elif difficulty == 3:
            
            time.sleep(0.7)
            print("Question 1: Which director is known for the 'Three Colors' trilogy?")
            time.sleep(0.5)
            print("a) Ingmar Bergman")
            time.sleep(0.2)
            print("b) Jean-Luc Godard")
            time.sleep(0.2)
            print("c) Krzysztof Kieślowski")
            time.sleep(0.2)
            print("d) François Truffaut")
            time.sleep(0.2)
            print("e) Federico Fellini")
            time.sleep(0.2)
            advanced_answer1 = input("Answer [a/b/c/d/e]: ")
            advanced_correct1 = "c"

            if advanced_answer1.lower() == advanced_correct1:
                advanced_total += 1

            time.sleep(0.7)
            print("\nQuestion 2: Which silent film star was known as 'The Little Tramp'?")
            time.sleep(0.5)
            print("a) Buster Keaton")
            time.sleep(0.2)
            print("b) Charlie Chaplin")
            time.sleep(0.2)
            print("c) Harold Lloyd")
            time.sleep(0.2)
            print("d) Douglas Fairbanks")
            time.sleep(0.2)
            print("e) Lon Chaney")
            time.sleep(0.2)
            advanced_answer2 = input("Answer [a/b/c/d/e]: ")
            advanced_correct2 = "b"

            if advanced_answer2.lower() == advanced_correct2:
                advanced_total += 1

            time.sleep(0.7)
            print("\nQuestion 3: Which movie is the first to win the Academy Award for Best Animated Feature?")
            time.sleep(0.5)
            print("a) Toy Story")
            time.sleep(0.2)
            print("b) Beauty and the Beast")
            time.sleep(0.2)
            print("c) Spirited Away")
            time.sleep(0.2)
            print("d) Shrek")
            time.sleep(0.2)
            print("e) Finding Nemo")
            time.sleep(0.2)
            advanced_answer3 = input("Answer [a/b/c/d/e]: ")
            advanced_correct3 = "d"

            if advanced_answer3.lower() == advanced_correct3:
                advanced_total += 1

            time.sleep(0.7)
            print("\nQuestion 4: In which movie does the character Norman Bates appear?")
            time.sleep(0.5)
            print("a) Rear Window")
            time.sleep(0.2)
            print("b) Vertigo")
            time.sleep(0.2)
            print("c) Psycho")
            time.sleep(0.2)
            print("d) The Birds")
            time.sleep(0.2)
            print("e) North by Northwest")
            time.sleep(0.2)
            advanced_answer4 = input("Answer [a/b/c/d/e]: ")
            advanced_correct4 = "c"

            if advanced_answer4.lower() == advanced_correct4:
                advanced_total += 1

            time.sleep(0.7)
            print("\nQuestion 5: Who played the role of Hannibal Lecter in 'The Silence of the Lambs'?")
            time.sleep(0.5)
            print("a) Robert De Niro")
            time.sleep(0.2)
            print("b) Anthony Hopkins")
            time.sleep(0.2)
            print("c) Al Pacino")
            time.sleep(0.2)
            print("d) Jack Nicholson")
            time.sleep(0.2)
            print("e) Daniel Day-Lewis")
            time.sleep(0.2)
            advanced_answer5 = input("Answer [a/b/c/d/e]: ")
            advanced_correct5 = "b"

            if advanced_answer5.lower() == advanced_correct5:
                advanced_total += 1

            time.sleep(0.7)
            print("\nQuestion 6: What is the name of the spaceship in the movie 'Alien'?")
            time.sleep(0.5)
            print("a) Enterprise")
            time.sleep(0.2)
            print("b) Nostromo")
            time.sleep(0.2)
            print("c) Millennium Falcon")
            time.sleep(0.2)
            print("d) Discovery One")
            time.sleep(0.2)
            print("e) Serenity")
            time.sleep(0.2)
            advanced_answer6 = input("Answer [a/b/c/d/e]: ")
            advanced_correct6 = "b"

            if advanced_answer6.lower() == advanced_correct6:
                advanced_total += 1
            
            time.sleep(0.7)
            print("\nQuestion 7: Which film features the character 'The Dude'?")
            time.sleep(0.5)
            print("a) The Big Lebowski")
            time.sleep(0.2)
            print("b) Fargo")
            time.sleep(0.2)
            print("c) No Country for Old Men")
            time.sleep(0.2)
            print("d) Burn After Reading")
            time.sleep(0.2)
            print("e) Raising Arizona")
            time.sleep(0.2)
            advanced_answer7 = input("Answer [a/b/c/d/e]: ")
            advanced_correct7 = "a"

            if advanced_answer7.lower() == advanced_correct7:
                advanced_total += 1

            time.sleep(0.7)
            print("\nQuestion 8: What is the name of the assassin played by Uma Thurman in 'Kill Bill'?")
            time.sleep(0.5)
            print("a) Black Mamba")
            time.sleep(0.2)
            print("b) The Bride")
            time.sleep(0.2)
            print("c) O-Ren Ishii")
            time.sleep(0.2)
            print("d) Elle Driver")
            time.sleep(0.2)
            print("e) Gogo Yubari")
            time.sleep(0.2)
            advanced_answer8 = input("Answer [a/b/c/d/e]: ")
            advanced_correct8 = "b"

            if advanced_answer8.lower() == advanced_correct8:
                advanced_total += 1

            time.sleep(0.7)
            print("\nQuestion 9: Who won the Academy Award for Best Director in 2019 for 'Parasite'?")
            time.sleep(0.5)
            print("a) Bong Joon-ho")
            time.sleep(0.2)
            print("b) Martin Scorsese")
            time.sleep(0.2)
            print("c) Quentin Tarantino")
            time.sleep(0.2)
            print("d) Sam Mendes")
            time.sleep(0.2)
            print("e) Todd Phillips")
            time.sleep(0.2)
            advanced_answer9 = input("Answer [a/b/c/d/e]: ")
            advanced_correct9 = "a"

            if advanced_answer9.lower() == advanced_correct9:
                advanced_total += 1

            time.sleep(0.7)
            print("\nQuestion 10: Which actress won an Academy Award for her role in 'La La Land'?")
            time.sleep(0.5)
            print("a) Natalie Portman")
            time.sleep(0.2)
            print("b) Emma Stone")
            time.sleep(0.2)
            print("c) Jennifer Lawrence")
            time.sleep(0.2)
            print("d) Reese Witherspoon")
            time.sleep(0.2)
            print("e) Brie Larson")
            time.sleep(0.2)
            advanced_answer10 = input("Answer [a/b/c/d/e]: ")
            advanced_correct10 = "b"

            if advanced_answer10.lower() == advanced_correct10:
                advanced_total += 1

            totals("movies", simple_total, intermediate_total, advanced_total)

    except ValueError as v:
        print(f"\nAn Error Occurred: {v}")
        time.sleep(1)
        print("You will be brought back to the start of the quiz. Please input either a,b,c,d,e as your answer to continue.")
        time.sleep(2)
        general_quiz(difficulty)
    except Exception as e:
        print(f"\nAn Error Occurred: {e}")
        time.sleep(1)
        print("The program will now restart, please ensure you follow the instructions properly.")
        time.sleep(2)
        start()

def music_quiz(difficulty):
    
    simple_total = 0
    intermediate_total = 0
    advanced_total = 0

    try:
        if difficulty == 1:

            time.sleep(0.7)
            print("Question 1: Which artist is known as the 'King of Pop'?")
            time.sleep(0.5)
            print("a) Elvis Presley")
            time.sleep(0.2)
            print("b) Michael Jackson")
            time.sleep(0.2)
            print("c) Prince")
            time.sleep(0.2)
            print("d) Justin Timberlake")
            time.sleep(0.2)
            print("e) Stevie Wonder")
            time.sleep(0.2)
            simple_answer1 = input("Answer [a/b/c/d/e]: ")
            simple_correct1 = "b"

            if simple_answer1.lower() == simple_correct1:
                simple_total += 1

            time.sleep(0.7)
            print("\nQuestion 2: Which band released the album 'Abbey Road' in 1969?")
            time.sleep(0.5)
            print("a) The Rolling Stones")
            time.sleep(0.2)
            print("b) The Beatles")
            time.sleep(0.2)
            print("c) The Who")
            time.sleep(0.2)
            print("d) Pink Floyd")
            time.sleep(0.2)
            print("e) The Beach Boys")
            time.sleep(0.2)
            simple_answer2 = input("Answer [a/b/c/d/e]: ")
            simple_correct2 = "b"

            if simple_answer2.lower() == simple_correct2:
                simple_total += 1

            time.sleep(0.7)
            print("\nQuestion 3: Who is the lead singer of the band U2?")
            time.sleep(0.5)
            print("a) Bono")
            time.sleep(0.2)
            print("b) Sting")
            time.sleep(0.2)
            print("c) Mick Jagger")
            time.sleep(0.2)
            print("d) Bruce Springsteen")
            time.sleep(0.2)
            print("e) Dave Grohl")
            time.sleep(0.2)
            simple_answer3 = input("Answer [a/b/c/d/e]: ")
            simple_correct3 = "a"

            if simple_answer3.lower() == simple_correct3:
                simple_total += 1

            time.sleep(0.7)
            print("\nQuestion 4: Which pop star is known for the hits 'Like a Virgin' and 'Vogue'?")
            time.sleep(0.5)
            print("a) Madonna")
            time.sleep(0.2)
            print("b) Britney Spears")
            time.sleep(0.2)
            print("c) Lady Gaga")
            time.sleep(0.2)
            print("d) Cyndi Lauper")
            time.sleep(0.2)
            print("e) Janet Jackson")
            time.sleep(0.2)
            simple_answer4 = input("Answer [a/b/c/d/e]: ")
            simple_correct4 = "a"

            if simple_answer4.lower() == simple_correct4:
                simple_total += 1

            time.sleep(0.7)
            print("\nQuestion 5: Who was the first woman ever inducted into the Rock and Roll Hall of Fame?")
            time.sleep(0.5)
            print("a) Aretha Franklin")
            time.sleep(0.2)
            print("b) Janis Joplin")
            time.sleep(0.2)
            print("c) Tina Turner")
            time.sleep(0.2)
            print("d) Carole King")
            time.sleep(0.2)
            print("e) Joni Mitchell")
            time.sleep(0.2)
            simple_answer5 = input("Answer [a/b/c/d/e]: ")
            simple_correct5 = "a"

            if simple_answer5.lower() == simple_correct5:
                simple_total += 1

            time.sleep(0.7)
            print("\nQuestion 6: Which song is often referred to as 'the anthem of the 1960s' and was performed by Bob Dylan?")
            time.sleep(0.5)
            print("a) 'Blowin' in the Wind'")
            time.sleep(0.2)
            print("b) 'Hey Jude'")
            time.sleep(0.2)
            print("c) 'Imagine'")
            time.sleep(0.2)
            print("d) 'A Change Is Gonna Come'")
            time.sleep(0.2)
            print("e) 'All Along the Watchtower'")
            time.sleep(0.2)
            simple_answer6 = input("Answer [a/b/c/d/e]: ")
            simple_correct6 = "a"

            if simple_answer6.lower() == simple_correct6:
                simple_total += 1
            
            time.sleep(0.7)
            print("\nQuestion 7: What is the real name of the rapper known as 'Eminem'?")
            time.sleep(0.5)
            print("a) Marshall Mathers")
            time.sleep(0.2)
            print("b) Calvin Broadus")
            time.sleep(0.2)
            print("c) Sean Combs")
            time.sleep(0.2)
            print("d) Curtis Jackson")
            time.sleep(0.2)
            print("e) Andre Young")
            time.sleep(0.2)
            simple_answer7 = input("Answer [a/b/c/d/e]: ")
            simple_correct7 = "a"

            if simple_answer7.lower() == simple_correct7:
                simple_total += 1

            time.sleep(0.7)
            print("\nQuestion 8: Which iconic music festival took place in 1969?")
            time.sleep(0.5)
            print("a) Monterey Pop Festival")
            time.sleep(0.2)
            print("b) Woodstock")
            time.sleep(0.2)
            print("c) Glastonbury")
            time.sleep(0.2)
            print("d) Isle of Wight Festival")
            time.sleep(0.2)
            print("e) Coachella")
            time.sleep(0.2)
            simple_answer8 = input("Answer [a/b/c/d/e]: ")
            simple_correct8 = "b"

            if simple_answer8.lower() == simple_correct8:
                simple_total += 1

            time.sleep(0.7)
            print("\nQuestion 9: Which legendary guitarist is known for songs like 'Purple Haze' and 'Foxy Lady'?")
            time.sleep(0.5)
            print("a) Eric Clapton")
            time.sleep(0.2)
            print("b) Jimi Hendrix")
            time.sleep(0.2)
            print("c) Jimmy Page")
            time.sleep(0.2)
            print("d) Slash")
            time.sleep(0.2)
            print("e) Jeff Beck")
            time.sleep(0.2)
            simple_answer9 = input("Answer [a/b/c/d/e]: ")
            simple_correct9 = "b"

            if simple_answer9.lower() == simple_correct9:
                simple_total += 1

            time.sleep(0.7)
            print("\nQuestion 10: Which band is known for the hit song 'Hotel California'?")
            time.sleep(0.5)
            print("a) The Eagles")
            time.sleep(0.2)
            print("b) Fleetwood Mac")
            time.sleep(0.2)
            print("c) The Doors")
            time.sleep(0.2)
            print("d) Led Zeppelin")
            time.sleep(0.2)
            print("e) The Beach Boys")
            time.sleep(0.2)
            simple_answer10 = input("Answer [a/b/c/d/e]: ")
            simple_correct10 = "a"

            if simple_answer10.lower() == simple_correct10:
                simple_total += 1

            totals("music", simple_total, intermediate_total, advanced_total)

        elif difficulty == 2:

            time.sleep(0.7)
            print("Question 1: Who is known as the 'Queen of Soul'?")
            time.sleep(0.5)
            print("a) Whitney Houston")
            time.sleep(0.2)
            print("b) Aretha Franklin")
            time.sleep(0.2)
            print("c) Diana Ross")
            time.sleep(0.2)
            print("d) Etta James")
            time.sleep(0.2)
            print("e) Patti LaBelle")
            time.sleep(0.2)
            intermediate_answer1 = input("Answer [a/b/c/d/e]: ")
            intermediate_correct1 = "b"

            if intermediate_answer1.lower() == intermediate_correct1:
                intermediate_total += 1

            time.sleep(0.7)
            print("\nQuestion 2: Which album is the best-selling album of all time?")
            time.sleep(0.5)
            print("a) Back in Black - AC/DC")
            time.sleep(0.2)
            print("b) The Dark Side of the Moon - Pink Floyd")
            time.sleep(0.2)
            print("c) Thriller - Michael Jackson")
            time.sleep(0.2)
            print("d) The Wall - Pink Floyd")
            time.sleep(0.2)
            print("e) Rumours - Fleetwood Mac")
            time.sleep(0.2)
            intermediate_answer2 = input("Answer [a/b/c/d/e]: ")
            intermediate_correct2 = "c"

            if intermediate_answer2.lower() == intermediate_correct2:
                intermediate_total += 1

            time.sleep(0.7)
            print("\nQuestion 3: Who composed the music for the film 'The Good, the Bad and the Ugly'?")
            time.sleep(0.5)
            print("a) John Williams")
            time.sleep(0.2)
            print("b) Ennio Morricone")
            time.sleep(0.2)
            print("c) Hans Zimmer")
            time.sleep(0.2)
            print("d) Danny Elfman")
            time.sleep(0.2)
            print("e) Howard Shore")
            time.sleep(0.2)
            intermediate_answer3 = input("Answer [a/b/c/d/e]: ")
            intermediate_correct3 = "b"

            if intermediate_answer3.lower() == intermediate_correct3:
                intermediate_total += 1

            time.sleep(0.7)
            print("\nQuestion 4: Which song by The Beatles was their first number-one hit in the United States?")
            time.sleep(0.5)
            print("a) 'She Loves You'")
            time.sleep(0.2)
            print("b) 'I Want to Hold Your Hand'")
            time.sleep(0.2)
            print("c) 'Can't Buy Me Love'")
            time.sleep(0.2)
            print("d) 'A Hard Day's Night'")
            time.sleep(0.2)
            print("e) 'Please Please Me'")
            time.sleep(0.2)
            intermediate_answer4 = input("Answer [a/b/c/d/e]: ")
            intermediate_correct4 = "b"

            if intermediate_answer4.lower() == intermediate_correct4:
                intermediate_total += 1

            time.sleep(0.7)
            print("\nQuestion 5: Which composer is known for his nine symphonies, including the famous 'Ode to Joy'?")
            time.sleep(0.5)
            print("a) Wolfgang Amadeus Mozart")
            time.sleep(0.2)
            print("b) Johann Sebastian Bach")
            time.sleep(0.2)
            print("c) Ludwig van Beethoven")
            time.sleep(0.2)
            print("d) Johannes Brahms")
            time.sleep(0.2)
            print("e) Richard Wagner")
            time.sleep(0.2)
            intermediate_answer5 = input("Answer [a/b/c/d/e]: ")
            intermediate_correct5 = "c"

            if intermediate_answer5.lower() == intermediate_correct5:
                intermediate_total += 1

            time.sleep(0.7)
            print("\nQuestion 6: Which singer is known for the song 'Jolene'?")
            time.sleep(0.5)
            print("a) Dolly Parton")
            time.sleep(0.2)
            print("b) Patsy Cline")
            time.sleep(0.2)
            print("c) Loretta Lynn")
            time.sleep(0.2)
            print("d) Tammy Wynette")
            time.sleep(0.2)
            print("e) Reba McEntire")
            time.sleep(0.2)
            intermediate_answer6 = input("Answer [a/b/c/d/e]: ")
            intermediate_correct6 = "a"

            if intermediate_answer6.lower() == intermediate_correct6:
                intermediate_total += 1
            
            time.sleep(0.7)
            print("\nQuestion 7: Who was the original drummer for The Beatles?")
            time.sleep(0.5)
            print("a) Ringo Starr")
            time.sleep(0.2)
            print("b) Pete Best")
            time.sleep(0.2)
            print("c) George Martin")
            time.sleep(0.2)
            print("d) Stu Sutcliffe")
            time.sleep(0.2)
            print("e) Brian Epstein")
            time.sleep(0.2)
            intermediate_answer7 = input("Answer [a/b/c/d/e]: ")
            intermediate_correct7 = "b"

            if intermediate_answer7.lower() == intermediate_correct7:
                intermediate_total += 1

            time.sleep(0.7)
            print("\nQuestion 8: Which band is known for the album 'The Joshua Tree'?")
            time.sleep(0.5)
            print("a) U2")
            time.sleep(0.2)
            print("b) The Police")
            time.sleep(0.2)
            print("c) R.E.M.")
            time.sleep(0.2)
            print("d) The Smiths")
            time.sleep(0.2)
            print("e) Depeche Mode")
            time.sleep(0.2)
            intermediate_answer8 = input("Answer [a/b/c/d/e]: ")
            intermediate_correct8 = "a"

            if intermediate_answer8.lower() == intermediate_correct8:
                intermediate_total += 1

            time.sleep(0.7)
            print("\nQuestion 9: Which artist was known as 'The King of Rock and Roll'?")
            time.sleep(0.5)
            print("a) Buddy Holly")
            time.sleep(0.2)
            print("b) Chuck Berry")
            time.sleep(0.2)
            print("c) Little Richard")
            time.sleep(0.2)
            print("d) Elvis Presley")
            time.sleep(0.2)
            print("e) Jerry Lee Lewis")
            time.sleep(0.2)
            intermediate_answer9 = input("Answer [a/b/c/d/e]: ")
            intermediate_correct9 = "d"

            if intermediate_answer9.lower() == intermediate_correct9:
                intermediate_total += 1

            time.sleep(0.7)
            print("\nQuestion 10: Who wrote the song 'Bohemian Rhapsody'?")
            time.sleep(0.5)
            print("a) John Lennon")
            time.sleep(0.2)
            print("b) Freddie Mercury")
            time.sleep(0.2)
            print("c) Paul McCartney")
            time.sleep(0.2)
            print("d) David Bowie")
            time.sleep(0.2)
            print("e) Mick Jagger")
            time.sleep(0.2)
            intermediate_answer10 = input("Answer [a/b/c/d/e]: ")
            intermediate_correct10 = "b"

            if intermediate_answer10.lower() == intermediate_correct10:
                intermediate_total += 1

            totals("music", simple_total, intermediate_total, advanced_total)

        elif difficulty == 3:
            
            time.sleep(0.7)
            print("Question 1: Which jazz musician is known for playing the trumpet and for songs like 'What a Wonderful World'?")
            time.sleep(0.5)
            print("a) Miles Davis")
            time.sleep(0.2)
            print("b) Louis Armstrong")
            time.sleep(0.2)
            print("c) Dizzy Gillespie")
            time.sleep(0.2)
            print("d) Chet Baker")
            time.sleep(0.2)
            print("e) Duke Ellington")
            time.sleep(0.2)
            advanced_answer1 = input("Answer [a/b/c/d/e]: ")
            advanced_correct1 = "b"

            if advanced_answer1.lower() == advanced_correct1:
                advanced_total += 1

            time.sleep(0.7)
            print("\nQuestion 2: Who was the original lead singer of the band Genesis?")
            time.sleep(0.5)
            print("a) Phil Collins")
            time.sleep(0.2)
            print("b) Peter Gabriel")
            time.sleep(0.2)
            print("c) Tony Banks")
            time.sleep(0.2)
            print("d) Mike Rutherford")
            time.sleep(0.2)
            print("e) Steve Hackett")
            time.sleep(0.2)
            advanced_answer2 = input("Answer [a/b/c/d/e]: ")
            advanced_correct2 = "b"

            if advanced_answer2.lower() == advanced_correct2:
                advanced_total += 1

            time.sleep(0.7)
            print("\nQuestion 3: Which composer is known for his operas like 'The Magic Flute' and 'Don Giovanni'?")
            time.sleep(0.5)
            print("a) Wolfgang Amadeus Mozart")
            time.sleep(0.2)
            print("b) Giuseppe Verdi")
            time.sleep(0.2)
            print("c) Richard Wagner")
            time.sleep(0.2)
            print("d) Georges Bizet")
            time.sleep(0.2)
            print("e) Johann Strauss II")
            time.sleep(0.2)
            advanced_answer3 = input("Answer [a/b/c/d/e]: ")
            advanced_correct3 = "a"

            if advanced_answer3.lower() == advanced_correct3:
                advanced_total += 1

            time.sleep(0.7)
            print("\nQuestion 4: Which band was fronted by Freddie Mercury?")
            time.sleep(0.5)
            print("a) Led Zeppelin")
            time.sleep(0.2)
            print("b) The Who")
            time.sleep(0.2)
            print("c) Queen")
            time.sleep(0.2)
            print("d) The Rolling Stones")
            time.sleep(0.2)
            print("e) Pink Floyd")
            time.sleep(0.2)
            advanced_answer4 = input("Answer [a/b/c/d/e]: ")
            advanced_correct4 = "c"

            if advanced_answer4.lower() == advanced_correct4:
                advanced_total += 1

            time.sleep(0.7)
            print("\nQuestion 5: Which composer wrote the famous ballet 'Swan Lake'?")
            time.sleep(0.5)
            print("a) Pyotr Ilyich Tchaikovsky")
            time.sleep(0.2)
            print("b) Igor Stravinsky")
            time.sleep(0.2)
            print("c) Sergei Prokofiev")
            time.sleep(0.2)
            print("d) Claude Debussy")
            time.sleep(0.2)
            print("e) Maurice Ravel")
            time.sleep(0.2)
            advanced_answer5 = input("Answer [a/b/c/d/e]: ")
            advanced_correct5 = "a"

            if advanced_answer5.lower() == advanced_correct5:
                advanced_total += 1

            time.sleep(0.7)
            print("\nQuestion 6: Which artist is known for his alter ego Ziggy Stardust?")
            time.sleep(0.5)
            print("a) Mick Jagger")
            time.sleep(0.2)
            print("b) David Bowie")
            time.sleep(0.2)
            print("c) Lou Reed")
            time.sleep(0.2)
            print("d) Iggy Pop")
            time.sleep(0.2)
            print("e) Freddie Mercury")
            time.sleep(0.2)
            advanced_answer6 = input("Answer [a/b/c/d/e]: ")
            advanced_correct6 = "b"

            if advanced_answer6.lower() == advanced_correct6:
                advanced_total += 1
            
            time.sleep(0.7)
            print("\nQuestion 7: Who composed the 'Four Seasons'?")
            time.sleep(0.5)
            print("a) Antonio Vivaldi")
            time.sleep(0.2)
            print("b) Johann Sebastian Bach")
            time.sleep(0.2)
            print("c) Ludwig van Beethoven")
            time.sleep(0.2)
            print("d) Franz Schubert")
            time.sleep(0.2)
            print("e) Georg Friedrich Handel")
            time.sleep(0.2)
            advanced_answer7 = input("Answer [a/b/c/d/e]: ")
            advanced_correct7 = "a"

            if advanced_answer7.lower() == advanced_correct7:
                advanced_total += 1

            time.sleep(0.7)
            print("\nQuestion 8: Which band was Kurt Cobain a part of?")
            time.sleep(0.5)
            print("a) Pearl Jam")
            time.sleep(0.2)
            print("b) Nirvana")
            time.sleep(0.2)
            print("c) Soundgarden")
            time.sleep(0.2)
            print("d) Alice in Chains")
            time.sleep(0.2)
            print("e) Stone Temple Pilots")
            time.sleep(0.2)
            advanced_answer8 = input("Answer [a/b/c/d/e]: ")
            advanced_correct8 = "b"

            if advanced_answer8.lower() == advanced_correct8:
                advanced_total += 1

            time.sleep(0.7)
            print("\nQuestion 9: Which singer is known for the album 'Back to Black'?")
            time.sleep(0.5)
            print("a) Adele")
            time.sleep(0.2)
            print("b) Amy Winehouse")
            time.sleep(0.2)
            print("c) Duffy")
            time.sleep(0.2)
            print("d) Norah Jones")
            time.sleep(0.2)
            print("e) Florence Welch")
            time.sleep(0.2)
            advanced_answer9 = input("Answer [a/b/c/d/e]: ")
            advanced_correct9 = "b"

            if advanced_answer9.lower() == advanced_correct9:
                advanced_total += 1

            time.sleep(0.7)
            print("\nQuestion 10: Which musician is nicknamed 'Slowhand'?")
            time.sleep(0.5)
            print("a) Eric Clapton")
            time.sleep(0.2)
            print("b) B.B. King")
            time.sleep(0.2)
            print("c) Carlos Santana")
            time.sleep(0.2)
            print("d) Jimmy Page")
            time.sleep(0.2)
            print("e) Jeff Beck")
            time.sleep(0.2)
            advanced_answer10 = input("Answer [a/b/c/d/e]: ")
            advanced_correct10 = "a"

            if advanced_answer10.lower() == advanced_correct10:
                advanced_total += 1

            totals("music", simple_total, intermediate_total, advanced_total)

    except ValueError as v:
        print(f"\nAn Error Occurred: {v}")
        time.sleep(1)
        print("You will be brought back to the start of the quiz. Please input either a,b,c,d,e as your answer to continue.")
        time.sleep(2)
        general_quiz(difficulty)
    except Exception as e:
        print(f"\nAn Error Occurred: {e}")
        time.sleep(1)
        print("The program will now restart, please ensure you follow the instructions properly.")
        time.sleep(2)
        start()

def totals(quiz, simple_score, int_score, advanced_score):
    
    try:

        if quiz == "general":
            
            if simple_score > scores["General Knowledge Quiz"]["Best Simple Score"]:
                scores["General Knowledge Quiz"]["Best Simple Score"] = simple_score

            if simple_score != 0:
                scores["General Knowledge Quiz"]["Most Recent Simple Score"] = f"[{simple_score}/10]"
            
            if int_score > scores["General Knowledge Quiz"]["Best Intermediate Score"]:
                scores["General Knowledge Quiz"]["Best Intermediate Score"] = int_score

            if int_score != 0:
                scores["General Knowledge Quiz"]["Most Recent Intermediate Score"] = f"[{int_score}/10]"
            
            if advanced_score > scores["General Knowledge Quiz"]["Best Advanced Score"]:
                scores["General Knowledge Quiz"]["Best Advanced Score"] = advanced_score

            if advanced_score != 0:
                scores["General Knowledge Quiz"]["Most Recent Advanced Score"] = f"[{advanced_score}/10]"
            
            time.sleep(1.5)
            print("\nCurrent Scores")
            
            for quiz_type, info in scores.items():
                if quiz_type == "General Knowledge Quiz":
                    print("")
                    time.sleep(0.5)
                    print("\n\033[1m",quiz_type,"\033[0m")
                    print("")
                
                    time.sleep(0.5)

                    for key in info:
                        if isinstance(info[key], int):
                            print(key + ":", f"[{info[key]}/10]")
                            print("")
                        else:
                            print(key + ":", info[key])
                        time.sleep(0.2)

            another = input("\nWould you like to do another quiz? [Y/N]: ")

            if another.lower() == "y":
                time.sleep(0.5)
                start()

            elif another.lower() == "n":
                print("\nThanks for playing, Now closing.")
                return
            
            else:
                print("\nPlease enter either Y or N to continue.")
                totals(quiz, simple_score, int_score, advanced_score)

        elif quiz == "game":

            if simple_score > scores["Video Games Quiz"]["Best Simple Score"]:
                scores["Video Games Quiz"]["Best Simple Score"] = simple_score
                
            if simple_score != 0:
                scores["Video Games Quiz"]["Most Recent Simple Score"] = f"[{simple_score}/10]"
            
            if int_score > scores["Video Games Quiz"]["Best Intermediate Score"]:
                scores["Video Games Quiz"]["Best Intermediate Score"] = int_score

            if int_score != 0:
                scores["Video Games Quiz"]["Most Recent Intermediate Score"] = f"[{int_score}/10]"
            
            if advanced_score > scores["Video Games Quiz"]["Best Advanced Score"]:
                scores["Video Games Quiz"]["Best Advanced Score"] = advanced_score

            if advanced_score != 0:
                scores["Video Games Quiz"]["Most Recent Advanced Score"] = f"[{advanced_score}/10]"
            
            time.sleep(1.5)
            print("\nCurrent Scores")
            
            for quiz_type, info in scores.items():
                if quiz_type == "Video Games Quiz":
                    print("")
                    time.sleep(0.5)
                    print("\n\033[1m",quiz_type,"\033[0m")
                    print("")
                    
                    time.sleep(0.5)

                    for key in info:
                        if isinstance(info[key], int):
                            print(key + ":", f"[{info[key]}/10]")
                            print("")
                        else:
                            print(key + ":", info[key])
                        time.sleep(0.2)

            time.sleep(0.5)
            another = input("\nWould you like to do another quiz? [Y/N]: ")

            if another.lower() == "y":
                time.sleep(0.5)
                start()

            elif another.lower() == "n":
                time.sleep(0.5)
                print("\nThanks for playing, Now closing.")
                return
            
            else:
                print("\nPlease enter either Y or N to continue.")
                totals(quiz, simple_score, int_score, advanced_score)

        elif quiz == "history":
            
            if simple_score > scores["History Quiz"]["Best Simple Score"]:
                scores["History Quiz"]["Best Simple Score"] = simple_score
                
            if simple_score != 0:
                scores["History Quiz"]["Most Recent Simple Score"] = f"[{simple_score}/10]"
            
            if int_score > scores["History Quiz"]["Best Intermediate Score"]:
                scores["History Quiz"]["Best Intermediate Score"] = int_score

            if int_score != 0:
                scores["History Quiz"]["Most Recent Intermediate Score"] = f"[{int_score}/10]"
            
            if advanced_score > scores["History Quiz"]["Best Advanced Score"]:
                scores["History Quiz"]["Best Advanced Score"] = advanced_score

            if advanced_score != 0:
                scores["History Quiz"]["Most Recent Advanced Score"] = f"[{advanced_score}/10]"
            
            time.sleep(1.5)
            print("\nCurrent Scores")
            
            for quiz_type, info in scores.items():
                if quiz_type == "History Quiz":
                    print("")
                    time.sleep(0.5)
                    print("\n\033[1m",quiz_type,"\033[0m")
                    print("")
                    
                    time.sleep(0.5)

                    for key in info:
                        if isinstance(info[key], int):
                            print(key + ":", f"[{info[key]}/10]")
                            print("")
                        else:
                            print(key + ":", info[key])
                        time.sleep(0.2)

            time.sleep(0.5)
            another = input("\nWould you like to do another quiz? [Y/N]: ")

            if another.lower() == "y":
                time.sleep(0.5)
                start()

            elif another.lower() == "n":
                time.sleep(0.5)
                print("\nThanks for playing, Now closing.")
                return
            
            else:
                print("\nPlease enter either Y or N to continue.")
                totals(quiz, simple_score, int_score, advanced_score)

        elif quiz == "sports":
                        
            if simple_score > scores["Sports Quiz"]["Best Simple Score"]:
                scores["Sports Quiz"]["Best Simple Score"] = simple_score

            if simple_score != 0:
                scores["Sports Quiz"]["Most Recent Simple Score"] = f"[{simple_score}/10]"
            
            if int_score > scores["Sports Quiz"]["Best Intermediate Score"]:
                scores["Sports Quiz"]["Best Intermediate Score"] = int_score

            if int_score != 0:
                scores["Sports Quiz"]["Most Recent Intermediate Score"] = f"[{int_score}/10]"
            
            if advanced_score > scores["Sports Quiz"]["Best Advanced Score"]:
                scores["Sports Quiz"]["Best Advanced Score"] = advanced_score

            if advanced_score != 0:
                scores["Sports Quiz"]["Most Recent Advanced Score"] = f"[{advanced_score}/10]"
            
            time.sleep(1.5)
            print("\nCurrent Scores")
            
            for quiz_type, info in scores.items():
                if quiz_type == "Sports Quiz":
                    print("")
                    time.sleep(0.5)
                    print("\n\033[1m",quiz_type,"\033[0m")
                    print("")
                    
                    time.sleep(0.5)

                    for key in info:
                        if isinstance(info[key], int):
                            print(key + ":", f"[{info[key]}/10]")
                            print("")
                        else:
                            print(key + ":", info[key])
                        time.sleep(0.2)

            time.sleep(0.5)
            another = input("\nWould you like to do another quiz? [Y/N]: ")

            if another.lower() == "y":
                time.sleep(0.5)
                start()

            elif another.lower() == "n":
                print("\nThanks for playing, Now closing.")
                return
            
            else:
                print("\nPlease enter either Y or N to continue.")
                totals(quiz, simple_score, int_score, advanced_score)

        elif quiz == "movies":

            if simple_score > scores["Movies Quiz"]["Best Simple Score"]:
                scores["Movies Quiz"]["Best Simple Score"] = simple_score
                
            if simple_score != 0:
                scores["Movies Quiz"]["Most Recent Simple Score"] = f"[{simple_score}/10]"
            
            if int_score > scores["Movies Quiz"]["Best Intermediate Score"]:
                scores["Movies Quiz"]["Best Intermediate Score"] = int_score

            if int_score != 0:
                scores["Movies Quiz"]["Most Recent Intermediate Score"] = f"[{int_score}/10]"
            
            if advanced_score > scores["Movies Quiz"]["Best Advanced Score"]:
                scores["Movies Quiz"]["Best Advanced Score"] = advanced_score

            if advanced_score != 0:
                scores["Movies Quiz"]["Most Recent Advanced Score"] = f"[{advanced_score}/10]"
            
            time.sleep(1.5)
            print("\nCurrent Scores")
            
            for quiz_type, info in scores.items():
                if quiz_type == "Movies Quiz":
                    print("")
                    time.sleep(0.5)
                    print("\n\033[1m",quiz_type,"\033[0m")
                    print("")
                    
                    time.sleep(0.5)

                    for key in info:
                        if isinstance(info[key], int):
                            print(key + ":", f"[{info[key]}/10]")
                            print("")
                        else:
                            print(key + ":", info[key])
                        time.sleep(0.2)

            time.sleep(0.5)
            another = input("\nWould you like to do another quiz? [Y/N]: ")

            if another.lower() == "y":
                time.sleep(0.5)
                start()

            elif another.lower() == "n":
                time.sleep(0.5)
                print("\nThanks for playing, Now closing.")
                return
            
            else:
                print("\nPlease enter either Y or N to continue.")
                totals(quiz, simple_score, int_score, advanced_score)

        elif quiz == "music":
            
            if simple_score > scores["Music Quiz"]["Best Simple Score"]:
                scores["Music Quiz"]["Best Simple Score"] = simple_score

            if simple_score != 0:
                scores["Music Quiz"]["Most Recent Simple Score"] = f"[{simple_score}/10]"
            
            if int_score > scores["Music Quiz"]["Best Intermediate Score"]:
                scores["Music Quiz"]["Best Intermediate Score"] = int_score

            if int_score != 0:
                scores["Music Quiz"]["Most Recent Intermediate Score"] = f"[{int_score}/10]"
            
            if advanced_score > scores["Music Quiz"]["Best Advanced Score"]:
                scores["Music Quiz"]["Best Advanced Score"] = advanced_score

            if advanced_score != 0:
                scores["Music Quiz"]["Most Recent Advanced Score"] = f"[{advanced_score}/10]"
            
            time.sleep(1.5)
            print("\nCurrent Scores")
            
            for quiz_type, info in scores.items():
                if quiz_type == "Music Quiz":
                    print("")
                    time.sleep(0.5)
                    print("\n\033[1m",quiz_type,"\033[0m")
                    print("")
                    
                    time.sleep(0.5)
                    
                    for key in info:
                        if isinstance(info[key], int):
                            print(key + ":", f"[{info[key]}/10]")
                            print("")
                        else:
                            print(key + ":", info[key])
                        time.sleep(0.2)

            another = input("\nWould you like to do another quiz? [Y/N]: ")

            if another.lower() == "y":
                time.sleep(0.5)
                start()

            elif another.lower() == "n":
                print("\nThanks for playing, Now closing.")
                return
            
            else:
                print("\nPlease enter either Y or N to continue.")
                totals(quiz, simple_score, int_score, advanced_score)

        else:
            time.sleep(1.5)
            print("\nCurrent Scores")
            
            for quiz_type, info in scores.items():
                print("")
                time.sleep(0.5)
                print("\033[1m",quiz_type,"\033[0m")
                print("")
                
                time.sleep(0.7)

                for key in info:
                    if isinstance(info[key], int):
                        print(key + ":", f"[{info[key]}/10]")
                        print("")
                    else:
                        print(key + ":", info[key])
                    time.sleep(0.2)
            
            time.sleep(0.5)
            another = input("\nWould you like to do another quiz? [Y/N]: ")

            if another.lower() == "y":
                time.sleep(0.5)
                start()

            elif another.lower() == "n":
                time.sleep(0.5)
                print("\nThanks for playing, Now closing.")
                return
            
            else:
                print("\nPlease enter either Y or N to continue.")
                totals(quiz, simple_score, int_score, advanced_score)
    
    except Exception as e:
            print(f"\nAn Error Occurred: {e}")


start()