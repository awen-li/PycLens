# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tokenize.py
# case: TestTokenize_test_oneline_defs

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    buf = []
    for i in range(500):
        buf.append('def i{i}(): return {i}'.format(i=i))
    buf.append('OK')
    buf = '\n'.join(buf)
    toks = list(tokenize(BytesIO(buf.encode('utf-8')).readline))
    self.assertEqual(toks[-3].string, 'OK')
