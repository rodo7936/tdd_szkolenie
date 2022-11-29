class Calculator:
    def add(self, *args) -> int:
        return sum(args)

    def minus(self, a, b) -> int:
        return a - b

    def multiplication(self, *args) -> int:
        if not any(args):
            raise ValueError(f'Provided 0 in numbers list!: {args}')
        result = 1
        for x in args:
            result *= x
        return result

    def division(self, *args) -> float:
        if not any(args):
            return float('inf')
