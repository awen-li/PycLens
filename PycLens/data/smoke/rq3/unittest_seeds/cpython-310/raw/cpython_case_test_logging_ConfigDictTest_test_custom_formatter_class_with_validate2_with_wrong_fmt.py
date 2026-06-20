# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_logging.py
# case: ConfigDictTest_test_custom_formatter_class_with_validate2_with_wrong_fmt

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    config = self.custom_formatter_class_validate.copy()
    config['formatters']['form1']['style'] = '$'
    self.apply_config(config)
    handler = logging.getLogger('my_test_logger_custom_formatter').handlers[0]
    self.assertIsInstance(handler.formatter, ExceptionFormatter)
