# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_embed.py
# case: EmbeddingTests_test_repeated_init_and_inittab

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (out, err) = self.run_embedded_interpreter('test_repeated_init_and_inittab')
    self.assertEqual(err, '')
    lines = [f'--- Pass {i} ---' for i in range(1, INIT_LOOPS + 1)]
    lines = '\n'.join(lines) + '\n'
    self.assertEqual(out, lines)
