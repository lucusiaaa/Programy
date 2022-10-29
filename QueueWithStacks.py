# This function print out menu options.
def options():
    print("1 - add to queue")
    print("2 - remove item from queue")
    print("3 - check the last element in queue")
    print("4 - print out the queue")
    print("5 - check if queue is empty")
    print("6 - quit")


# This function is menu with options:
#  - adding new element at the end of queue,
#  - removing element from the beginning of queue,
#  - checking the last element,
#  - printing out the queue,
#  - checking if queue is empty,
#  - exiting the program.
# Returns the queue created by the two stacks.
def main():
    # boolean running <- flag responsible for exiting the loop
    running = True
    # stack1, stack2 <- stacks used to form a queue
    stack1 = []
    stack2 = []

    while running:
        options()
        option = input()

        if option == '1':
            myInput = input("Insert: ")
            stack1.append(myInput)
        elif option == '2':
            while stack1:
                stack2.append(stack1.pop())
            stack2.pop()
            while stack2:
                stack1.append(stack2.pop())
        elif option == '3':
            print(stack1[-1])
        elif option == '4':
            print(stack1)
        elif option == '5':
            if stack1:
                print("Queue IS NOT empty")
            else:
                print("Queue IS empty")
        elif option == '6':
            running = False
        else:
            print("There isn't such option!")

    return stack1


main()
