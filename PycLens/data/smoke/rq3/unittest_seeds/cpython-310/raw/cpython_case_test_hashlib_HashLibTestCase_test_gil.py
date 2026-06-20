# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_hashlib.py
# case: HashLibTestCase_test_gil

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    gil_minsize = 2048
    for cons in self.hash_constructors:
        m = cons(usedforsecurity=False)
        m.update(b'1')
        m.update(b'#' * gil_minsize)
        m.update(b'1')
        m = cons(b'x' * gil_minsize, usedforsecurity=False)
        m.update(b'1')
    m = hashlib.sha256()
    m.update(b'1')
    m.update(b'#' * gil_minsize)
    m.update(b'1')
    self.assertEqual(m.hexdigest(), '1cfceca95989f51f658e3f3ffe7f1cd43726c9e088c13ee10b46f57cef135b94')
    m = hashlib.sha256(b'1' + b'#' * gil_minsize + b'1')
    self.assertEqual(m.hexdigest(), '1cfceca95989f51f658e3f3ffe7f1cd43726c9e088c13ee10b46f57cef135b94')
