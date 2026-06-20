# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: GetTypeHintTests_test_respect_no_type_check

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @no_type_check
    class NoTpCheck:

        class Inn:

            def __init__(self, x: 'not a type'):
                ...
    self.assertTrue(NoTpCheck.__no_type_check__)
    self.assertTrue(NoTpCheck.Inn.__init__.__no_type_check__)
    self.assertEqual(gth(ann_module2.NTC.meth), {})

    class ABase(Generic[T]):

        def meth(x: int):
            ...

    @no_type_check
    class Der(ABase):
        ...
    self.assertEqual(gth(ABase.meth), {'x': int})
