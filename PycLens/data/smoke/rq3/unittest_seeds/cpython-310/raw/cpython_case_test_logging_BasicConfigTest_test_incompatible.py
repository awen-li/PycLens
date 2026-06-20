# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_logging.py
# case: BasicConfigTest_test_incompatible

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    assertRaises = self.assertRaises
    handlers = [logging.StreamHandler()]
    stream = sys.stderr
    assertRaises(ValueError, logging.basicConfig, filename='test.log', stream=stream)
    assertRaises(ValueError, logging.basicConfig, filename='test.log', handlers=handlers)
    assertRaises(ValueError, logging.basicConfig, stream=stream, handlers=handlers)
    assertRaises(ValueError, logging.basicConfig, loglevel=logging.INFO)
    logging.basicConfig(filename=None, filemode='a')
