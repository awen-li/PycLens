# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bytes.py
# case: BytearrayPEP3137Test_test_returns_new_copy

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    val = self.marshal(b'1234')
    for methname in ('zfill', 'rjust', 'ljust', 'center'):
        method = getattr(val, methname)
        newval = method(3)
        self.assertEqual(val, newval)
        self.assertIsNot(val, newval, methname + ' returned self on a mutable object')
    for expr in ('val.split()[0]', 'val.rsplit()[0]', 'val.partition(b".")[0]', 'val.rpartition(b".")[2]', 'val.splitlines()[0]', 'val.replace(b"", b"")'):
        newval = eval(expr)
        self.assertEqual(val, newval)
        self.assertIsNot(val, newval, expr + ' returned val on a mutable object')
    sep = self.marshal(b'')
    newval = sep.join([val])
    self.assertEqual(val, newval)
    self.assertIsNot(val, newval)
