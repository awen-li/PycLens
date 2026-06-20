# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_functools.py
# case: TestTotalOrdering_test_type_error_when_not_implemented

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @functools.total_ordering
    class ImplementsLessThan:

        def __init__(self, value):
            self.value = value

        def __eq__(self, other):
            if isinstance(other, ImplementsLessThan):
                return self.value == other.value
            return False

        def __lt__(self, other):
            if isinstance(other, ImplementsLessThan):
                return self.value < other.value
            return NotImplemented

    @functools.total_ordering
    class ImplementsGreaterThan:

        def __init__(self, value):
            self.value = value

        def __eq__(self, other):
            if isinstance(other, ImplementsGreaterThan):
                return self.value == other.value
            return False

        def __gt__(self, other):
            if isinstance(other, ImplementsGreaterThan):
                return self.value > other.value
            return NotImplemented

    @functools.total_ordering
    class ImplementsLessThanEqualTo:

        def __init__(self, value):
            self.value = value

        def __eq__(self, other):
            if isinstance(other, ImplementsLessThanEqualTo):
                return self.value == other.value
            return False

        def __le__(self, other):
            if isinstance(other, ImplementsLessThanEqualTo):
                return self.value <= other.value
            return NotImplemented

    @functools.total_ordering
    class ImplementsGreaterThanEqualTo:

        def __init__(self, value):
            self.value = value

        def __eq__(self, other):
            if isinstance(other, ImplementsGreaterThanEqualTo):
                return self.value == other.value
            return False

        def __ge__(self, other):
            if isinstance(other, ImplementsGreaterThanEqualTo):
                return self.value >= other.value
            return NotImplemented

    @functools.total_ordering
    class ComparatorNotImplemented:

        def __init__(self, value):
            self.value = value

        def __eq__(self, other):
            if isinstance(other, ComparatorNotImplemented):
                return self.value == other.value
            return False

        def __lt__(self, other):
            return NotImplemented
    with self.subTest('LT < 1'), self.assertRaises(TypeError):
        ImplementsLessThan(-1) < 1
    with self.subTest('LT < LE'), self.assertRaises(TypeError):
        ImplementsLessThan(0) < ImplementsLessThanEqualTo(0)
    with self.subTest('LT < GT'), self.assertRaises(TypeError):
        ImplementsLessThan(1) < ImplementsGreaterThan(1)
    with self.subTest('LE <= LT'), self.assertRaises(TypeError):
        ImplementsLessThanEqualTo(2) <= ImplementsLessThan(2)
    with self.subTest('LE <= GE'), self.assertRaises(TypeError):
        ImplementsLessThanEqualTo(3) <= ImplementsGreaterThanEqualTo(3)
    with self.subTest('GT > GE'), self.assertRaises(TypeError):
        ImplementsGreaterThan(4) > ImplementsGreaterThanEqualTo(4)
    with self.subTest('GT > LT'), self.assertRaises(TypeError):
        ImplementsGreaterThan(5) > ImplementsLessThan(5)
    with self.subTest('GE >= GT'), self.assertRaises(TypeError):
        ImplementsGreaterThanEqualTo(6) >= ImplementsGreaterThan(6)
    with self.subTest('GE >= LE'), self.assertRaises(TypeError):
        ImplementsGreaterThanEqualTo(7) >= ImplementsLessThanEqualTo(7)
    with self.subTest('GE when equal'):
        a = ComparatorNotImplemented(8)
        b = ComparatorNotImplemented(8)
        self.assertEqual(a, b)
        with self.assertRaises(TypeError):
            a >= b
    with self.subTest('LE when equal'):
        a = ComparatorNotImplemented(9)
        b = ComparatorNotImplemented(9)
        self.assertEqual(a, b)
        with self.assertRaises(TypeError):
            a <= b
