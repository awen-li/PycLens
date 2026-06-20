# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib2.py
# case: OpenerDirectorTests_test_add_non_handler

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class NonHandler(object):
        pass
    self.assertRaises(TypeError, OpenerDirector().add_handler, NonHandler())
