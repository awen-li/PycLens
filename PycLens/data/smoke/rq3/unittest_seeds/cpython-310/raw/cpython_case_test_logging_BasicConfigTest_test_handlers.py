# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_logging.py
# case: BasicConfigTest_test_handlers

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    handlers = [logging.StreamHandler(), logging.StreamHandler(sys.stdout), logging.StreamHandler()]
    f = logging.Formatter()
    handlers[2].setFormatter(f)
    logging.basicConfig(handlers=handlers)
    self.assertIs(handlers[0], logging.root.handlers[0])
    self.assertIs(handlers[1], logging.root.handlers[1])
    self.assertIs(handlers[2], logging.root.handlers[2])
    self.assertIsNotNone(handlers[0].formatter)
    self.assertIsNotNone(handlers[1].formatter)
    self.assertIs(handlers[2].formatter, f)
    self.assertIs(handlers[0].formatter, handlers[1].formatter)
