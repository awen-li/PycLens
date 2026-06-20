# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_types.py
# case: ClassCreationTests_test_bad___prepare__

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class BadMeta(type):

        @classmethod
        def __prepare__(*args):
            return None
    with self.assertRaisesRegex(TypeError, '^BadMeta\\.__prepare__\\(\\) must return a mapping, not NoneType$'):

        class Foo(metaclass=BadMeta):
            pass

    class BadMeta:

        @classmethod
        def __prepare__(*args):
            return None
    with self.assertRaisesRegex(TypeError, '^<metaclass>\\.__prepare__\\(\\) must return a mapping, not NoneType$'):

        class Bar(metaclass=BadMeta()):
            pass
