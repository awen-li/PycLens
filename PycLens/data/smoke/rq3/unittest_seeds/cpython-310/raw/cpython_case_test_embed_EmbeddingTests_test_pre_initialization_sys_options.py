# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_embed.py
# case: EmbeddingTests_test_pre_initialization_sys_options

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    env = remove_python_envvars()
    env['PYTHONPATH'] = os.pathsep.join(sys.path)
    (out, err) = self.run_embedded_interpreter('test_pre_initialization_sys_options', env=env)
    expected_output = "sys.warnoptions: ['once', 'module', 'default']\nsys._xoptions: {'not_an_option': '1', 'also_not_an_option': '2'}\nwarnings.filters[:3]: ['default', 'module', 'once']\n"
    self.assertIn(expected_output, out)
    self.assertEqual(err, '')
