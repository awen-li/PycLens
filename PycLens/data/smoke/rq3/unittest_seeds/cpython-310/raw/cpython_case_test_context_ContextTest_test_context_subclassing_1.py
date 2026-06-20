# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_context.py
# case: ContextTest_test_context_subclassing_1

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.assertRaisesRegex(TypeError, 'not an acceptable base type'):

        class MyContextVar(contextvars.ContextVar):
            pass
    with self.assertRaisesRegex(TypeError, 'not an acceptable base type'):

        class MyContext(contextvars.Context):
            pass
    with self.assertRaisesRegex(TypeError, 'not an acceptable base type'):

        class MyToken(contextvars.Token):
            pass
