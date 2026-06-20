# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_unicode.py
# case: UnicodeTest_test_formatting_with_enum

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    import enum

    class Float(float, enum.Enum):
        PI = 3.1415926

    class Int(enum.IntEnum):
        IDES = 15

    class Str(str, enum.Enum):
        ABC = 'abc'
    self.assertEqual('%s, %s' % (Str.ABC, Str.ABC), 'Str.ABC, Str.ABC')
    self.assertEqual('%s, %s, %d, %i, %u, %f, %5.2f' % (Str.ABC, Str.ABC, Int.IDES, Int.IDES, Int.IDES, Float.PI, Float.PI), 'Str.ABC, Str.ABC, 15, 15, 15, 3.141593,  3.14')
    self.assertEqual('...%(foo)s...' % {'foo': Str.ABC}, '...Str.ABC...')
    self.assertEqual('...%(foo)s...' % {'foo': Int.IDES}, '...Int.IDES...')
    self.assertEqual('...%(foo)i...' % {'foo': Int.IDES}, '...15...')
    self.assertEqual('...%(foo)d...' % {'foo': Int.IDES}, '...15...')
    self.assertEqual('...%(foo)u...' % {'foo': Int.IDES, 'def': Float.PI}, '...15...')
    self.assertEqual('...%(foo)f...' % {'foo': Float.PI, 'def': 123}, '...3.141593...')
