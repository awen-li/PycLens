# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_logging.py
# case: ConfigDictTest_test_out_of_order_with_dollar_style

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    config = copy.deepcopy(self.out_of_order)
    config['formatters']['mySimpleFormatter']['format'] = '${asctime} (${name}) ${levelname}: ${message}'
    self.apply_config(config)
    handler = logging.getLogger('mymodule').handlers[0]
    self.assertIsInstance(handler.target, logging.Handler)
    self.assertIsInstance(handler.formatter._style, logging.StringTemplateStyle)
