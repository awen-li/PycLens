# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_types.py
# case: UnionTests_test_or_type_operator_reference_cycle

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    if not hasattr(sys, 'gettotalrefcount'):
        self.skipTest('Cannot get total reference count.')
    gc.collect()
    before = sys.gettotalrefcount()
    for _ in range(30):
        T = typing.TypeVar('T')
        U = int | list[T]
        T.blah = U
        del T
        del U
    gc.collect()
    leeway = 15
    self.assertLessEqual(sys.gettotalrefcount() - before, leeway, msg='Check for union reference leak.')
