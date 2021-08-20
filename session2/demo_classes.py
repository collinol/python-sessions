

def get_square(x):
    return x**2


class Squarer:

    def __init__(self, value):
        self.x = value

    def create_square(self) -> None:
        """Takes number, returns square

        Args:
            x: number to square

        Returns:
            integer squared

        """
        # do stuff
        # more stuff
        self.x = self.x**2

    def additional_func(self):
        print(self.x)


class S3:
    def __init__(self, foo, bar):
        self.S3Value = 4
    pass


class SubSquarer(Squarer, S3):

    def __init__(self, value):
        super(Squarer, self).__init__(value)
        super(S3, self).__init__()
        self.x = value

    def create_square(self) -> None:
        """Takes number, returns square

        Args:
            x: number to square

        Returns:
            integer squared

        """
        # do stuff
        # more stuff
        self.x = self.x**3


subclass = SubSquarer(8)
subclass.create_square()
print(subclass.S3Value)