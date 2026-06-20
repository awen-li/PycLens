# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_embed.py
# case: EmbeddingTests_test_bpo20891

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (out, err) = self.run_embedded_interpreter('test_bpo20891')
    self.assertEqual(out, '')
    self.assertEqual(err, '')
