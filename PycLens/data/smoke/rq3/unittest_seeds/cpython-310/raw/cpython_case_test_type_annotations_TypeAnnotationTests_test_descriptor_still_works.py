# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_type_annotations.py
# case: TypeAnnotationTests_test_descriptor_still_works

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class C:

        def __init__(self, name=None, bases=None, d=None):
            self.my_annotations = None

        @property
        def __annotations__(self):
            if not hasattr(self, 'my_annotations'):
                self.my_annotations = {}
            if not isinstance(self.my_annotations, dict):
                self.my_annotations = {}
            return self.my_annotations

        @__annotations__.setter
        def __annotations__(self, value):
            if not isinstance(value, dict):
                raise ValueError('can only set __annotations__ to a dict')
            self.my_annotations = value

        @__annotations__.deleter
        def __annotations__(self):
            if getattr(self, 'my_annotations', False) is None:
                raise AttributeError('__annotations__')
            self.my_annotations = None
    c = C()
    self.assertEqual(c.__annotations__, {})
    d = {'a': 'int'}
    c.__annotations__ = d
    self.assertEqual(c.__annotations__, d)
    with self.assertRaises(ValueError):
        c.__annotations__ = 123
    del c.__annotations__
    with self.assertRaises(AttributeError):
        del c.__annotations__
    self.assertEqual(c.__annotations__, {})

    class D(metaclass=C):
        pass
    self.assertEqual(D.__annotations__, {})
    d = {'a': 'int'}
    D.__annotations__ = d
    self.assertEqual(D.__annotations__, d)
    with self.assertRaises(ValueError):
        D.__annotations__ = 123
    del D.__annotations__
    with self.assertRaises(AttributeError):
        del D.__annotations__
    self.assertEqual(D.__annotations__, {})
