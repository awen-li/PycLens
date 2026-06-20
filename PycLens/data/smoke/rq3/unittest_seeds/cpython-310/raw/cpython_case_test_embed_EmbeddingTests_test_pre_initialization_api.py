# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_embed.py
# case: EmbeddingTests_test_pre_initialization_api

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    env = dict(os.environ, PYTHONPATH=os.pathsep.join(sys.path))
    (out, err) = self.run_embedded_interpreter('test_pre_initialization_api', env=env)
    if MS_WINDOWS:
        expected_path = self.test_exe
    else:
        expected_path = os.path.join(os.getcwd(), 'spam')
    expected_output = f'sys.executable: {expected_path}\n'
    self.assertIn(expected_output, out)
    self.assertEqual(err, '')
