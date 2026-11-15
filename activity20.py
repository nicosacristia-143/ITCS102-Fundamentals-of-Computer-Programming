isMovie = True
Movie = input("Do you watch movies? (yes/no): ").lower()
Movielist = []
while isMovie == True:

    if Movie == "yes":
        Movie_name = input("Input your favorite movie:")
        Movielist.append(Movie_name)
        print(Movielist)
        Movie1 = input("Do you want to add another movie? (yes/no): ").lower()

        if Movie1 == "yes":
            continue

        else:
            print("Thank you for using the program!")
            isMovie = False
            break

    else:
        print("Thank you for using the program!")
        isMovie = False
        break