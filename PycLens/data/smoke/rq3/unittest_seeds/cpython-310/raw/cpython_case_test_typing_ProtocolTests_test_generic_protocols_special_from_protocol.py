# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: ProtocolTests_test_generic_protocols_special_from_protocol

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @runtime_checkable
    class PR(Protocol):
        x = 1

    class P(Protocol):

        def meth(self):
            pass
    T = TypeVar('T')

    class PG(Protocol[T]):
        x = 1

        def meth(self):
            pass
    self.assertTrue(P._is_protocol)
    self.assertTrue(PR._is_protocol)
    self.assertTrue(PG._is_protocol)
    self.assertFalse(P._is_runtime_protocol)
    self.assertTrue(PR._is_runtime_protocol)
    self.assertTrue(PG[int]._is_protocol)
    self.assertEqual(typing._get_protocol_attrs(P), {'meth'})
    self.assertEqual(typing._get_protocol_attrs(PR), {'x'})
    self.assertEqual(frozenset(typing._get_protocol_attrs(PG)), frozenset({'x', 'meth'}))
