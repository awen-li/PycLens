# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_builtin.py
# case: BuiltinTest_test_format

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(format(3, ''), '3')

    def classes_new():

        class A(object):

            def __init__(self, x):
                self.x = x

            def __format__(self, format_spec):
                return str(self.x) + format_spec

        class DerivedFromA(A):
            pass

        class Simple(object):
            pass

        class DerivedFromSimple(Simple):

            def __init__(self, x):
                self.x = x

            def __format__(self, format_spec):
                return str(self.x) + format_spec

        class DerivedFromSimple2(DerivedFromSimple):
            pass
        return (A, DerivedFromA, DerivedFromSimple, DerivedFromSimple2)

    def class_test(A, DerivedFromA, DerivedFromSimple, DerivedFromSimple2):
        self.assertEqual(format(A(3), 'spec'), '3spec')
        self.assertEqual(format(DerivedFromA(4), 'spec'), '4spec')
        self.assertEqual(format(DerivedFromSimple(5), 'abc'), '5abc')
        self.assertEqual(format(DerivedFromSimple2(10), 'abcdef'), '10abcdef')
    class_test(*classes_new())

    def empty_format_spec(value):
        self.assertEqual(format(value, ''), str(value))
        self.assertEqual(format(value), str(value))
    empty_format_spec(17 ** 13)
    empty_format_spec(1.0)
    empty_format_spec(3.1415e+104)
    empty_format_spec(-3.1415e+104)
    empty_format_spec(3.1415e-104)
    empty_format_spec(-3.1415e-104)
    empty_format_spec(object)
    empty_format_spec(None)

    class BadFormatResult:

        def __format__(self, format_spec):
            return 1.0
    self.assertRaises(TypeError, format, BadFormatResult(), '')
    self.assertRaises(TypeError, format, object(), 4)
    self.assertRaises(TypeError, format, object(), object())
    x = object().__format__('')
    self.assertTrue(x.startswith('<object object at'))
    self.assertRaises(TypeError, object().__format__, 3)
    self.assertRaises(TypeError, object().__format__, object())
    self.assertRaises(TypeError, object().__format__, None)

    class A:

        def __format__(self, fmt_str):
            return format('', fmt_str)
    self.assertEqual(format(A()), '')
    self.assertEqual(format(A(), ''), '')
    self.assertEqual(format(A(), 's'), '')

    class B:
        pass

    class C(object):
        pass
    for cls in [object, B, C]:
        obj = cls()
        self.assertEqual(format(obj), str(obj))
        self.assertEqual(format(obj, ''), str(obj))
        with self.assertRaisesRegex(TypeError, '\\b%s\\b' % re.escape(cls.__name__)):
            format(obj, 's')

    class DerivedFromStr(str):
        pass
    self.assertEqual(format(0, DerivedFromStr('10')), '         0')
