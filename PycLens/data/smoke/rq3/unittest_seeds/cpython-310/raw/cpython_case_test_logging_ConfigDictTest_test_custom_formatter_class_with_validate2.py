# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_logging.py
# case: ConfigDictTest_test_custom_formatter_class_with_validate2

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.apply_config(self.custom_formatter_class_validate2)
    handler = logging.getLogger('my_test_logger_custom_formatter').handlers[0]
    self.assertIsInstance(handler.formatter, ExceptionFormatter)
