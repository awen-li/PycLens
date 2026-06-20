# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_hashlib.py
# case: HashLibTestCase_test_case_blake2b_all_parameters

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.check('blake2b', b'foo', '920568b0c5873b2f0ab67bedb6cf1b2b', digest_size=16, key=b'bar', salt=b'baz', person=b'bing', fanout=2, depth=3, leaf_size=4, node_offset=5, node_depth=6, inner_size=7, last_node=True)
