# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_turtle.py
# case: TurtleConfigTest_test_config_dict

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    cfg_name = self.get_cfg_file(test_config)
    parsed_cfg = turtle.config_dict(cfg_name)
    expected = {'width': 0.75, 'height': 0.8, 'canvwidth': 500, 'canvheight': 200, 'leftright': 100, 'topbottom': 100, 'mode': 'world', 'colormode': 255, 'delay': 100, 'undobuffersize': 10000, 'shape': 'circle', 'pencolor': 'red', 'fillcolor': 'blue', 'resizemode': 'auto', 'visible': None, 'language': 'english', 'exampleturtle': 'turtle', 'examplescreen': 'screen', 'title': 'Python Turtle Graphics', 'using_IDLE': ''}
    self.assertEqual(parsed_cfg, expected)
