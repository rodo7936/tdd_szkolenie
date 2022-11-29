class Calculator:
    def add(self, *args) -> int:
        return sum(args)

    def minus(self, a, b) -> int:
        return a - b

    def multiplication(self, *args) -> int:
        if not all(args):
            raise ValueError(f'Provided 0 in numbers list!: {args}')
        result = 1
        for x in args:
            result *= x
        return result

    def division(self, a, b) -> float:
        if not b:
            return float('inf')
        return a / b

    def avg(self, *args, **kwargs) -> float:
        if not args:
            return 0
        if not kwargs:
            return sum(args) / len(args)
        nums = args
        if 'lt' in kwargs:
            nums = [_ for _ in nums if _ <= kwargs.get('lt')]
        if 'gt' in kwargs:
            nums = [_ for _ in nums if _ >= kwargs.get('gt')]
        if not nums:
            return 0
        return sum(nums) / len(nums)
