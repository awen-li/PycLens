# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_enum.py
# case: TestEnum_test_missing

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Color(Enum):
        red = 1
        green = 2
        blue = 3

        @classmethod
        def _missing_(cls, item):
            if item == 'three':
                return cls.blue
            elif item == 'bad return':
                return 5
            elif item == 'error out':
                raise ZeroDivisionError
            else:
                return None
    self.assertIs(Color('three'), Color.blue)
    try:
        Color(7)
    except ValueError as exc:
        self.assertTrue(exc.__context__ is None)
    else:
        raise Exception('Exception not raised.')
    try:
        Color('bad return')
    except TypeError as exc:
        self.assertTrue(isinstance(exc.__context__, ValueError))
    else:
        raise Exception('Exception not raised.')
    try:
        Color('error out')
    except ZeroDivisionError as exc:
        self.assertTrue(isinstance(exc.__context__, ValueError))
    else:
        raise Exception('Exception not raised.')
