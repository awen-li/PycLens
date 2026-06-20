# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_turtle.py
# case: TurtleConfigTest_test_partial_config_dict_with_comments

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    cfg_name = self.get_cfg_file(test_config_two)
    parsed_cfg = turtle.config_dict(cfg_name)
    expected = {'pencolor': 'red', 'fillcolor': 'blue', 'visible': False, 'language': 'english', 'using_IDLE': False}
    self.assertEqual(parsed_cfg, expected)
