def sort(stack1, stack2, stack3):
    """Code needs to be optimalized!"""
    while True: 
        stack3.push(stack1.pop())
        while not stack1.empty():

            if stack3.peek() < stack1.peek():
                stack2.push(stack1.pop())
            else:
                stack2.push(stack3.pop())
                stack3.push(stack1.pop())

        if stack2.empty():
            break

        stack3.push(stack2.pop())
        while not stack2.empty():

            if stack3.peek() < stack2.peek():
                stack1.push(stack2.pop())
            else:
                stack1.push(stack3.pop())
                stack3.push(stack2.pop())

        if stack1.empty():
            break

    while not stack3.empty():
        stack1.push(stack3.pop())
