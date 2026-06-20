# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_strptime.py
# case: StrptimeTests_test_ValueError

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertRaises(ValueError, _strptime._strptime_time, data_string='%d', format='%A')
    for bad_format in ('%', '% ', '%e'):
        try:
            _strptime._strptime_time('2005', bad_format)
        except ValueError:
            continue
        except Exception as err:
            self.fail("'%s' raised %s, not ValueError" % (bad_format, err.__class__.__name__))
        else:
            self.fail("'%s' did not raise ValueError" % bad_format)
    with self.assertRaises(ValueError):
        _strptime._strptime('1999 50', '%Y %V')
    with self.assertRaises(ValueError):
        _strptime._strptime('1999 51', '%G %V')
    for w in ('A', 'a', 'w', 'u'):
        with self.assertRaises(ValueError):
            _strptime._strptime('1999 51', '%G %{}'.format(w))
    with self.assertRaises(ValueError):
        _strptime._strptime('2015', '%G')
    with self.assertRaises(ValueError):
        _strptime._strptime('1999 256', '%G %j')
