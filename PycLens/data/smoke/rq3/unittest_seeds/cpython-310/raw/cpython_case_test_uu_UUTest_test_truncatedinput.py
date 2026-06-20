# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_uu.py
# case: UUTest_test_truncatedinput

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    inp = io.BytesIO(b'begin 644 t1\n' + encodedtext)
    out = io.BytesIO()
    try:
        uu.decode(inp, out)
        self.fail('No exception raised')
    except uu.Error as e:
        self.assertEqual(str(e), 'Truncated input file')
