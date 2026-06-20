# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_logging.py
# case: CustomLevelsAndFiltersTest_test_handler_filter

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.root_logger.handlers[0].setLevel(SOCIABLE)
    try:
        self.log_at_all_levels(self.root_logger)
        self.assert_log_lines([('Sociable', '6'), ('Effusive', '7'), ('Terse', '8'), ('Taciturn', '9'), ('Silent', '10')])
    finally:
        self.root_logger.handlers[0].setLevel(logging.NOTSET)
