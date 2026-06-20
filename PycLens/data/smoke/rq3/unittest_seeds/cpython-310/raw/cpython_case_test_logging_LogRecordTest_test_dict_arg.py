# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_logging.py
# case: LogRecordTest_test_dict_arg

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    h = RecordingHandler()
    r = logging.getLogger()
    r.addHandler(h)
    d = {'less': 'more'}
    logging.warning('less is %(less)s', d)
    self.assertIs(h.records[0].args, d)
    self.assertEqual(h.records[0].message, 'less is more')
    r.removeHandler(h)
    h.close()
