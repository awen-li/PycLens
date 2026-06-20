# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_functools.py
# case: TestSingleDispatch_test_annotations

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @functools.singledispatch
    def i(arg):
        return 'base'

    @i.register
    def _(arg: collections.abc.Mapping):
        return 'mapping'

    @i.register
    def _(arg: 'collections.abc.Sequence'):
        return 'sequence'
    self.assertEqual(i(None), 'base')
    self.assertEqual(i({'a': 1}), 'mapping')
    self.assertEqual(i([1, 2, 3]), 'sequence')
    self.assertEqual(i((1, 2, 3)), 'sequence')
    self.assertEqual(i('str'), 'sequence')

    @i.register(str)
    class _:

        def __init__(self, arg):
            self.arg = arg

        def __eq__(self, other):
            return self.arg == other
    self.assertEqual(i('str'), 'str')
