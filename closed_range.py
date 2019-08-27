class ClosedRange(object):
    def __init__(self, a, b):
        try:
            a, b = int(a), int(b)
        except ValueError:
            raise
        if not isinstance(a, int) or not isinstance(b, int):
            raise ValueError
        if a > b:
            raise ValueError
        self.closed_range = [a, b]

    def return_string(self):
        return str(self.closed_range)

    def is_contained(self, num):
        if self.closed_range[0] <= num <= self.closed_range[1]:
            return True
        else:
            return False

    def arg_is_equal_to_closed_range(self, arg):
        del arg[1:-1]
        if arg == self.closed_range:
            return True
        else:
            return False

    def arg_is_fully_contained(self, arg):
        if arg[0] >= self.closed_range[0] and arg[-1] <= self.closed_range[1]:
            return True
        else:
            return False
