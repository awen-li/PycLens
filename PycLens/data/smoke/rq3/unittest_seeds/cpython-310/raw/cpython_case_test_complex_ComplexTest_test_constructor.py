# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_complex.py
# case: ComplexTest_test_constructor

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class NS:

        def __init__(self, value):
            self.value = value

        def __complex__(self):
            return self.value
    self.assertEqual(complex(NS(1 + 10j)), 1 + 10j)
    self.assertRaises(TypeError, complex, NS(None))
    self.assertRaises(TypeError, complex, {})
    self.assertRaises(TypeError, complex, NS(1.5))
    self.assertRaises(TypeError, complex, NS(1))
    self.assertAlmostEqual(complex('1+10j'), 1 + 10j)
    self.assertAlmostEqual(complex(10), 10 + 0j)
    self.assertAlmostEqual(complex(10.0), 10 + 0j)
    self.assertAlmostEqual(complex(10), 10 + 0j)
    self.assertAlmostEqual(complex(10 + 0j), 10 + 0j)
    self.assertAlmostEqual(complex(1, 10), 1 + 10j)
    self.assertAlmostEqual(complex(1, 10), 1 + 10j)
    self.assertAlmostEqual(complex(1, 10.0), 1 + 10j)
    self.assertAlmostEqual(complex(1, 10), 1 + 10j)
    self.assertAlmostEqual(complex(1, 10), 1 + 10j)
    self.assertAlmostEqual(complex(1, 10.0), 1 + 10j)
    self.assertAlmostEqual(complex(1.0, 10), 1 + 10j)
    self.assertAlmostEqual(complex(1.0, 10), 1 + 10j)
    self.assertAlmostEqual(complex(1.0, 10.0), 1 + 10j)
    self.assertAlmostEqual(complex(3.14 + 0j), 3.14 + 0j)
    self.assertAlmostEqual(complex(3.14), 3.14 + 0j)
    self.assertAlmostEqual(complex(314), 314.0 + 0j)
    self.assertAlmostEqual(complex(314), 314.0 + 0j)
    self.assertAlmostEqual(complex(3.14 + 0j, 0j), 3.14 + 0j)
    self.assertAlmostEqual(complex(3.14, 0.0), 3.14 + 0j)
    self.assertAlmostEqual(complex(314, 0), 314.0 + 0j)
    self.assertAlmostEqual(complex(314, 0), 314.0 + 0j)
    self.assertAlmostEqual(complex(0j, 3.14j), -3.14 + 0j)
    self.assertAlmostEqual(complex(0.0, 3.14j), -3.14 + 0j)
    self.assertAlmostEqual(complex(0j, 3.14), 3.14j)
    self.assertAlmostEqual(complex(0.0, 3.14), 3.14j)
    self.assertAlmostEqual(complex('1'), 1 + 0j)
    self.assertAlmostEqual(complex('1j'), 1j)
    self.assertAlmostEqual(complex(), 0)
    self.assertAlmostEqual(complex('-1'), -1)
    self.assertAlmostEqual(complex('+1'), +1)
    self.assertAlmostEqual(complex('(1+2j)'), 1 + 2j)
    self.assertAlmostEqual(complex('(1.3+2.2j)'), 1.3 + 2.2j)
    self.assertAlmostEqual(complex('3.14+1J'), 3.14 + 1j)
    self.assertAlmostEqual(complex(' ( +3.14-6J )'), 3.14 - 6j)
    self.assertAlmostEqual(complex(' ( +3.14-J )'), 3.14 - 1j)
    self.assertAlmostEqual(complex(' ( +3.14+j )'), 3.14 + 1j)
    self.assertAlmostEqual(complex('J'), 1j)
    self.assertAlmostEqual(complex('( j )'), 1j)
    self.assertAlmostEqual(complex('+J'), 1j)
    self.assertAlmostEqual(complex('( -j)'), -1j)
    self.assertAlmostEqual(complex('1e-500'), 0.0 + 0j)
    self.assertAlmostEqual(complex('-1e-500j'), 0.0 - 0j)
    self.assertAlmostEqual(complex('-1e-500+1e-500j'), -0.0 + 0j)

    class complex2(complex):
        pass
    self.assertAlmostEqual(complex(complex2(1 + 1j)), 1 + 1j)
    self.assertAlmostEqual(complex(real=17, imag=23), 17 + 23j)
    self.assertAlmostEqual(complex(real=17 + 23j), 17 + 23j)
    self.assertAlmostEqual(complex(real=17 + 23j, imag=23), 17 + 46j)
    self.assertAlmostEqual(complex(real=1 + 2j, imag=3 + 4j), -3 + 5j)

    def split_zeros(x):
        """Function that produces different results for 0. and -0."""
        return atan2(x, -1.0)
    self.assertEqual(split_zeros(complex(1.0, 0.0).imag), split_zeros(0.0))
    self.assertEqual(split_zeros(complex(1.0, -0.0).imag), split_zeros(-0.0))
    self.assertEqual(split_zeros(complex(0.0, 1.0).real), split_zeros(0.0))
    self.assertEqual(split_zeros(complex(-0.0, 1.0).real), split_zeros(-0.0))
    c = 3.14 + 1j
    self.assertTrue(complex(c) is c)
    del c
    self.assertRaises(TypeError, complex, '1', '1')
    self.assertRaises(TypeError, complex, 1, '1')
    self.assertRaises(ValueError, complex, '1+1j\x00j')
    self.assertRaises(TypeError, int, 5 + 3j)
    self.assertRaises(TypeError, int, 5 + 3j)
    self.assertRaises(TypeError, float, 5 + 3j)
    self.assertRaises(ValueError, complex, '')
    self.assertRaises(TypeError, complex, None)
    self.assertRaisesRegex(TypeError, "not 'NoneType'", complex, None)
    self.assertRaises(ValueError, complex, '\x00')
    self.assertRaises(ValueError, complex, '3\x009')
    self.assertRaises(TypeError, complex, '1', '2')
    self.assertRaises(TypeError, complex, '1', 42)
    self.assertRaises(TypeError, complex, 1, '2')
    self.assertRaises(ValueError, complex, '1+')
    self.assertRaises(ValueError, complex, '1+1j+1j')
    self.assertRaises(ValueError, complex, '--')
    self.assertRaises(ValueError, complex, '(1+2j')
    self.assertRaises(ValueError, complex, '1+2j)')
    self.assertRaises(ValueError, complex, '1+(2j)')
    self.assertRaises(ValueError, complex, '(1+2j)123')
    self.assertRaises(ValueError, complex, 'x')
    self.assertRaises(ValueError, complex, '1j+2')
    self.assertRaises(ValueError, complex, '1e1ej')
    self.assertRaises(ValueError, complex, '1e++1ej')
    self.assertRaises(ValueError, complex, ')1+2j(')
    self.assertRaisesRegex(TypeError, "first argument must be a string or a number, not 'dict'", complex, {1: 2}, 1)
    self.assertRaisesRegex(TypeError, "second argument must be a number, not 'dict'", complex, 1, {1: 2})
    self.assertRaises(ValueError, complex, '1..1j')
    self.assertRaises(ValueError, complex, '1.11.1j')
    self.assertRaises(ValueError, complex, '1e1.1j')
    self.assertEqual(type(complex('1' * 500)), complex)
    self.assertEqual(complex('\u2003(\u20021+1j ) '), 1 + 1j)
    self.assertRaises(ValueError, complex, 'こんにちは')

    class EvilExc(Exception):
        pass

    class evilcomplex:

        def __complex__(self):
            raise EvilExc
    self.assertRaises(EvilExc, complex, evilcomplex())

    class float2:

        def __init__(self, value):
            self.value = value

        def __float__(self):
            return self.value
    self.assertAlmostEqual(complex(float2(42.0)), 42)
    self.assertAlmostEqual(complex(real=float2(17.0), imag=float2(23.0)), 17 + 23j)
    self.assertRaises(TypeError, complex, float2(None))

    class MyIndex:

        def __init__(self, value):
            self.value = value

        def __index__(self):
            return self.value
    self.assertAlmostEqual(complex(MyIndex(42)), 42.0 + 0j)
    self.assertAlmostEqual(complex(123, MyIndex(42)), 123.0 + 42j)
    self.assertRaises(OverflowError, complex, MyIndex(2 ** 2000))
    self.assertRaises(OverflowError, complex, 123, MyIndex(2 ** 2000))

    class MyInt:

        def __int__(self):
            return 42
    self.assertRaises(TypeError, complex, MyInt())
    self.assertRaises(TypeError, complex, 123, MyInt())

    class complex0(complex):
        """Test usage of __complex__() when inheriting from 'complex'"""

        def __complex__(self):
            return 42j

    class complex1(complex):
        """Test usage of __complex__() with a __new__() method"""

        def __new__(self, value=0j):
            return complex.__new__(self, 2 * value)

        def __complex__(self):
            return self

    class complex2(complex):
        """Make sure that __complex__() calls fail if anything other than a
            complex is returned"""

        def __complex__(self):
            return None
    self.assertEqual(complex(complex0(1j)), 42j)
    with self.assertWarns(DeprecationWarning):
        self.assertEqual(complex(complex1(1j)), 2j)
    self.assertRaises(TypeError, complex, complex2(1j))
