# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestSignatureObject_test_signature_on_class

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class C:

        def __init__(self, a):
            pass
    self.assertEqual(self.signature(C), ((('a', ..., ..., 'positional_or_keyword'),), ...))

    class CM(type):

        def __call__(cls, a):
            pass

    class C(metaclass=CM):

        def __init__(self, b):
            pass
    self.assertEqual(self.signature(C), ((('a', ..., ..., 'positional_or_keyword'),), ...))

    class CM(type):

        def __new__(mcls, name, bases, dct, *, foo=1):
            return super().__new__(mcls, name, bases, dct)

    class C(metaclass=CM):

        def __init__(self, b):
            pass
    self.assertEqual(self.signature(C), ((('b', ..., ..., 'positional_or_keyword'),), ...))
    self.assertEqual(self.signature(CM), ((('name', ..., ..., 'positional_or_keyword'), ('bases', ..., ..., 'positional_or_keyword'), ('dct', ..., ..., 'positional_or_keyword'), ('foo', 1, ..., 'keyword_only')), ...))

    class CMM(type):

        def __new__(mcls, name, bases, dct, *, foo=1):
            return super().__new__(mcls, name, bases, dct)

        def __call__(cls, nm, bs, dt):
            return type(nm, bs, dt)

    class CM(type, metaclass=CMM):

        def __new__(mcls, name, bases, dct, *, bar=2):
            return super().__new__(mcls, name, bases, dct)

    class C(metaclass=CM):

        def __init__(self, b):
            pass
    self.assertEqual(self.signature(CMM), ((('name', ..., ..., 'positional_or_keyword'), ('bases', ..., ..., 'positional_or_keyword'), ('dct', ..., ..., 'positional_or_keyword'), ('foo', 1, ..., 'keyword_only')), ...))
    self.assertEqual(self.signature(CM), ((('nm', ..., ..., 'positional_or_keyword'), ('bs', ..., ..., 'positional_or_keyword'), ('dt', ..., ..., 'positional_or_keyword')), ...))
    self.assertEqual(self.signature(C), ((('b', ..., ..., 'positional_or_keyword'),), ...))

    class CM(type):

        def __init__(cls, name, bases, dct, *, bar=2):
            return super().__init__(name, bases, dct)

    class C(metaclass=CM):

        def __init__(self, b):
            pass
    self.assertEqual(self.signature(CM), ((('name', ..., ..., 'positional_or_keyword'), ('bases', ..., ..., 'positional_or_keyword'), ('dct', ..., ..., 'positional_or_keyword'), ('bar', 2, ..., 'keyword_only')), ...))
