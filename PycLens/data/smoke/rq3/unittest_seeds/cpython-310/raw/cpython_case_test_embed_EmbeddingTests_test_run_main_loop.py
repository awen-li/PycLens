# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_embed.py
# case: EmbeddingTests_test_run_main_loop

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    nloop = 5
    (out, err) = self.run_embedded_interpreter('test_run_main_loop')
    self.assertEqual(out, "Py_RunMain(): sys.argv=['-c', 'arg2']\n" * nloop)
    self.assertEqual(err, '')
