# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_functools.py
# case: TestSingleDispatch_test_type_ann_register

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class A:

        @functools.singledispatchmethod
        def t(self, arg):
            return 'base'

        @t.register
        def _(self, arg: int):
            return 'int'

        @t.register
        def _(self, arg: str):
            return 'str'
    a = A()
    self.assertEqual(a.t(0), 'int')
    self.assertEqual(a.t(''), 'str')
    self.assertEqual(a.t(0.0), 'base')
