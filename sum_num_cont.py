#!/usr/bin/env python3
# Created By: Titwech Wal
# Date: April.27. 2022

# program that generates a random correct guess. It then
# uses a loop to keep asking the user to guess
# the number until they guess correctly.
# Once they guess the correct number, it breaks out of the loop.


def main():

    # initialize the loop counter and sum
    loop_counter = 0
    sum = 0

    while True:
        # input
        user_number_string = input("How many numbers do you want to add?: ")
        print("")

        try:
            # convert to string
            user_number = int(user_number_string)

            if user_number >= 0:

                # add the sum of the numbers
                while (loop_counter < user_number):
                    user_add_string = input("Enter your numbers: ")

                    try:
                        # converts entered number from string to integer
                        user_add = int(user_add_string)

                        # sets a range, as well as, adds the number entered.
                        if user_add >= 0:
                            print("{} has been added to the sum."
                                  .format(user_add))
                            print("")
                            sum = sum + user_add
                            loop_counter = loop_counter + 1
                        else:
                            print("{} is negative, so it cannot be added." .
                                  format(user_add))
                            print("")
                            continue
                    # handles the error case.
                    except Exception:
                        print("{} is not a number.". format(user_add_string))
                        print("")
                        continue
                # tells user the sum
                if (loop_counter == user_number):
                    print("The sum is = {} ". format(sum))
                    break

            else:
                print('Enter an integer , try again')

        except Exception:
            print("{} is not a valid number.".format(user_number_string))


if __name__ == "__main__":
    main()
