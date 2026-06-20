# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_re.py
# case: ReTests_test_bigcharset

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(re.match('([∢∣])', '∢').group(1), '∢')
    r = '[%s]' % ''.join(map(chr, range(256, 2 ** 16, 255)))
    self.assertEqual(re.match(r, '！').group(), '！')
