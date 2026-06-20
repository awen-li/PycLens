# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_csv.py
# case: Test_Csv_test_write_escape

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self._write_test(['a', 1, 'p,q'], 'a,1,"p,q"', escapechar='\\')
    self._write_error_test(csv.Error, ['a', 1, 'p,"q"'], escapechar=None, doublequote=False)
    self._write_test(['a', 1, 'p,"q"'], 'a,1,"p,\\"q\\""', escapechar='\\', doublequote=False)
    self._write_test(['"'], '""""', escapechar='\\', quoting=csv.QUOTE_MINIMAL)
    self._write_test(['"'], '\\"', escapechar='\\', quoting=csv.QUOTE_MINIMAL, doublequote=False)
    self._write_test(['"'], '\\"', escapechar='\\', quoting=csv.QUOTE_NONE)
    self._write_test(['a', 1, 'p,q'], 'a,1,p\\,q', escapechar='\\', quoting=csv.QUOTE_NONE)
    self._write_test(['\\', 'a'], '\\\\,a', escapechar='\\', quoting=csv.QUOTE_NONE)
    self._write_test(['\\', 'a'], '\\\\,a', escapechar='\\', quoting=csv.QUOTE_MINIMAL)
    self._write_test(['\\', 'a'], '"\\\\","a"', escapechar='\\', quoting=csv.QUOTE_ALL)
    self._write_test(['\\ ', 'a'], '\\\\ ,a', escapechar='\\', quoting=csv.QUOTE_MINIMAL)
    self._write_test(['\\,', 'a'], '\\\\\\,,a', escapechar='\\', quoting=csv.QUOTE_NONE)
    self._write_test([',\\', 'a'], '",\\\\",a', escapechar='\\', quoting=csv.QUOTE_MINIMAL)
    self._write_test(['C\\', '6', '7', 'X"'], 'C\\\\,6,7,"X"""', escapechar='\\', quoting=csv.QUOTE_MINIMAL)
