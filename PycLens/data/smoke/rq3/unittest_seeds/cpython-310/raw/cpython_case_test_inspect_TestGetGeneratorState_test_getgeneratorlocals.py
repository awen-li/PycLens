# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestGetGeneratorState_test_getgeneratorlocals

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def each(lst, a=None):
        b = (1, 2, 3)
        for v in lst:
            if v == 3:
                c = 12
            yield v
    numbers = each([1, 2, 3])
    self.assertEqual(inspect.getgeneratorlocals(numbers), {'a': None, 'lst': [1, 2, 3]})
    next(numbers)
    self.assertEqual(inspect.getgeneratorlocals(numbers), {'a': None, 'lst': [1, 2, 3], 'v': 1, 'b': (1, 2, 3)})
    next(numbers)
    self.assertEqual(inspect.getgeneratorlocals(numbers), {'a': None, 'lst': [1, 2, 3], 'v': 2, 'b': (1, 2, 3)})
    next(numbers)
    self.assertEqual(inspect.getgeneratorlocals(numbers), {'a': None, 'lst': [1, 2, 3], 'v': 3, 'b': (1, 2, 3), 'c': 12})
    try:
        next(numbers)
    except StopIteration:
        pass
    self.assertEqual(inspect.getgeneratorlocals(numbers), {})
