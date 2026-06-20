# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_logging.py
# case: BasicFilterTest_test_filter

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    filter_ = logging.Filter('spam.eggs')
    handler = self.root_logger.handlers[0]
    try:
        handler.addFilter(filter_)
        spam = logging.getLogger('spam')
        spam_eggs = logging.getLogger('spam.eggs')
        spam_eggs_fish = logging.getLogger('spam.eggs.fish')
        spam_bakedbeans = logging.getLogger('spam.bakedbeans')
        spam.info(self.next_message())
        spam_eggs.info(self.next_message())
        spam_eggs_fish.info(self.next_message())
        spam_bakedbeans.info(self.next_message())
        self.assert_log_lines([('spam.eggs', 'INFO', '2'), ('spam.eggs.fish', 'INFO', '3')])
    finally:
        handler.removeFilter(filter_)
