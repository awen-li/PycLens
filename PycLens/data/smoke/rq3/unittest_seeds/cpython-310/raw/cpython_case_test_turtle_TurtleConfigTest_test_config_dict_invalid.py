# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_turtle.py
# case: TurtleConfigTest_test_config_dict_invalid

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    cfg_name = self.get_cfg_file(invalid_test_config)
    with support.captured_stdout() as stdout:
        parsed_cfg = turtle.config_dict(cfg_name)
    err_msg = stdout.getvalue()
    self.assertIn('Bad line in config-file ', err_msg)
    self.assertIn('fillcolor: blue', err_msg)
    self.assertEqual(parsed_cfg, {'pencolor': 'red', 'visible': False})
