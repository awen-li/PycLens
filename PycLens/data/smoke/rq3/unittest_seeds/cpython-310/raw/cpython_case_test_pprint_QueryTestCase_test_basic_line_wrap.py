# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pprint.py
# case: QueryTestCase_test_basic_line_wrap

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    o = {'RPM_cal': 0, 'RPM_cal2': 48059, 'Speed_cal': 0, 'controldesk_runtime_us': 0, 'main_code_runtime_us': 0, 'read_io_runtime_us': 0, 'write_io_runtime_us': 43690}
    exp = "{'RPM_cal': 0,\n 'RPM_cal2': 48059,\n 'Speed_cal': 0,\n 'controldesk_runtime_us': 0,\n 'main_code_runtime_us': 0,\n 'read_io_runtime_us': 0,\n 'write_io_runtime_us': 43690}"
    for type in [dict, dict2]:
        self.assertEqual(pprint.pformat(type(o)), exp)
    o = range(100)
    exp = '[%s]' % ',\n '.join(map(str, o))
    for type in [list, list2]:
        self.assertEqual(pprint.pformat(type(o)), exp)
    o = tuple(range(100))
    exp = '(%s)' % ',\n '.join(map(str, o))
    for type in [tuple, tuple2]:
        self.assertEqual(pprint.pformat(type(o)), exp)
    o = range(100)
    exp = '[   %s]' % ',\n    '.join(map(str, o))
    for type in [list, list2]:
        self.assertEqual(pprint.pformat(type(o), indent=4), exp)
