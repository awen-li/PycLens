# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_logging.py
# case: ConfigFileTest_test_config_set_handler_names

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    test_config = '\n            [loggers]\n            keys=root\n\n            [handlers]\n            keys=hand1\n\n            [formatters]\n            keys=form1\n\n            [logger_root]\n            handlers=hand1\n\n            [handler_hand1]\n            class=StreamHandler\n            formatter=form1\n\n            [formatter_form1]\n            format=%(levelname)s ++ %(message)s\n            '
    self.apply_config(test_config)
    self.assertEqual(logging.getLogger().handlers[0].name, 'hand1')
