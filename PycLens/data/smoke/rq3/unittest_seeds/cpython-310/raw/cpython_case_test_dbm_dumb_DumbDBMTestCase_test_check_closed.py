# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dbm_dumb.py
# case: DumbDBMTestCase_test_check_closed

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    f = dumbdbm.open(_fname, 'c')
    f.close()
    for meth in (partial(operator.delitem, f), partial(operator.setitem, f, 'b'), partial(operator.getitem, f), partial(operator.contains, f)):
        with self.assertRaises(dumbdbm.error) as cm:
            meth('test')
        self.assertEqual(str(cm.exception), 'DBM object has already been closed')
    for meth in (operator.methodcaller('keys'), operator.methodcaller('iterkeys'), operator.methodcaller('items'), len):
        with self.assertRaises(dumbdbm.error) as cm:
            meth(f)
        self.assertEqual(str(cm.exception), 'DBM object has already been closed')
