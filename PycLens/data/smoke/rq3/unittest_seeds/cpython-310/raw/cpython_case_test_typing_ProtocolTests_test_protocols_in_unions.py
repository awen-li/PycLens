# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: ProtocolTests_test_protocols_in_unions

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class P(Protocol):
        x = None
    Alias = typing.Union[typing.Iterable, P]
    Alias2 = typing.Union[P, typing.Iterable]
    self.assertEqual(Alias, Alias2)
