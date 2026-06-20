# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_logging.py
# case: CustomLevelsAndFiltersTest_test_specific_filters

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    handler = self.root_logger.handlers[0]
    specific_filter = None
    garr = GarrulousFilter()
    handler.addFilter(garr)
    try:
        self.log_at_all_levels(self.root_logger)
        first_lines = [('Boring', '1'), ('Chatterbox', '2'), ('Talkative', '4'), ('Verbose', '5'), ('Sociable', '6'), ('Effusive', '7'), ('Terse', '8'), ('Taciturn', '9'), ('Silent', '10')]
        self.assert_log_lines(first_lines)
        specific_filter = VerySpecificFilter()
        self.root_logger.addFilter(specific_filter)
        self.log_at_all_levels(self.root_logger)
        self.assert_log_lines(first_lines + [('Boring', '11'), ('Chatterbox', '12'), ('Talkative', '14'), ('Verbose', '15'), ('Effusive', '17'), ('Terse', '18'), ('Silent', '20')])
    finally:
        if specific_filter:
            self.root_logger.removeFilter(specific_filter)
        handler.removeFilter(garr)
