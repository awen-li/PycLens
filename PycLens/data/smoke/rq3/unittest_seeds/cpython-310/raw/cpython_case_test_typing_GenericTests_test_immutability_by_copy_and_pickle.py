# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: GenericTests_test_immutability_by_copy_and_pickle

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    global TP, TPB, TPV
    TP = TypeVar('TP')
    TPB = TypeVar('TPB', bound=int)
    TPV = TypeVar('TPV', bytes, str)
    for X in [TP, TPB, TPV, List, typing.Mapping, ClassVar, typing.Iterable, Union, Any, Tuple, Callable]:
        self.assertIs(copy(X), X)
        self.assertIs(deepcopy(X), X)
        self.assertIs(pickle.loads(pickle.dumps(X)), X)
    TL = TypeVar('TL')
    TLB = TypeVar('TLB', bound=int)
    TLV = TypeVar('TLV', bytes, str)
    for X in [TL, TLB, TLV]:
        self.assertIs(copy(X), X)
        self.assertIs(deepcopy(X), X)
