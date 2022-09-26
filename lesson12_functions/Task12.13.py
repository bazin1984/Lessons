#  декоратор функции

def simple_decore(fn) :
    print("Start function")
    fn()
    print("Stop function")

@simple_decore
def first_test() :
    print("Test function 1")

@simple_decore
def second_test() :
    print("Test function 2")

