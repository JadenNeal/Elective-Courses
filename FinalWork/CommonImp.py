class CommonImp:
    """
    Several common implementation for python
    """
    def __init__(self):
        """
        initialize the variables
        """
        pass

    def sortport(self, lis):
        """
        Sort a list,or we can use lis.sort()
        :param lis: A list to sort
        :return:a sorted list
        """
        for i in range(len(lis) - 1):
            for j in range(len(lis) - 1 - i):
                if lis[j] > lis[j+1]:
                    lis[j], lis[j+1] = lis[j+1], lis[j]
        return lis

    def sumofsquare(self, *numbers):
        """
        calculate the summary of square for numbers
        :param numbers:Just a number
        :return:summary
        """
        summary = 0
        for n in numbers:
            summary += n ** 2
        return summary

    def fac(self, num):
        """
        calculate factorial
        :param num:the superior limit number
        :return: factorial
        """
        factorial = 1

        if num < 0:
            print("Sorry, negative number is illegal!")
        elif num == 0:
            print("Factorial of 0 is 1.")
        else:
            for i in range(1, num+1):
                factorial *= i
            print("Factorial of %d is %d" % (num, factorial))


