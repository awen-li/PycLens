# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_weakref.py
# case: ReferencesTestCase_test_callbacks_on_callback

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    import gc
    alist = []

    def safe_callback(ignore):
        alist.append('safe_callback called')

    class C(object):

        def cb(self, ignore):
            alist.append('cb called')
    (c, d) = (C(), C())
    c.other = d
    d.other = c
    callback = c.cb
    c.wr = weakref.ref(d, callback)
    d.wr = weakref.ref(callback, d.cb)
    external_wr = weakref.ref(callback, safe_callback)
    self.assertIs(external_wr(), callback)
    del callback, c, d, C
    self.assertEqual(alist, [])
    gc.collect()
    self.assertEqual(alist, ['safe_callback called'])
    self.assertEqual(external_wr(), None)
    del alist[:]
    gc.collect()
    self.assertEqual(alist, [])
