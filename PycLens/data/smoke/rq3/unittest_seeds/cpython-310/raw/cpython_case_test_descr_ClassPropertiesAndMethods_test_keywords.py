# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_descr.py
# case: ClassPropertiesAndMethods_test_keywords

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.assertRaisesRegex(TypeError, 'keyword argument'):
        int(x=1)
    with self.assertRaisesRegex(TypeError, 'keyword argument'):
        float(x=2)
    with self.assertRaisesRegex(TypeError, 'keyword argument'):
        bool(x=2)
    self.assertEqual(complex(imag=42, real=666), complex(666, 42))
    self.assertEqual(str(object=500), '500')
    self.assertEqual(str(object=b'abc', errors='strict'), 'abc')
    with self.assertRaisesRegex(TypeError, 'keyword argument'):
        tuple(sequence=range(3))
    with self.assertRaisesRegex(TypeError, 'keyword argument'):
        list(sequence=(0, 1, 2))
    for constructor in (int, float, int, complex, str, str, tuple, list):
        try:
            constructor(bogus_keyword_arg=1)
        except TypeError:
            pass
        else:
            self.fail('expected TypeError from bogus keyword argument to %r' % constructor)
