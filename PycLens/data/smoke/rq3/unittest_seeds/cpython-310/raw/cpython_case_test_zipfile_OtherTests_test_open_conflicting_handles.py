# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zipfile.py
# case: OtherTests_test_open_conflicting_handles

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    msg1 = b"It's fun to charter an accountant!"
    msg2 = b'And sail the wide accountant sea'
    msg3 = b'To find, explore the funds offshore'
    with zipfile.ZipFile(TESTFN2, 'w', zipfile.ZIP_STORED) as zipf:
        with zipf.open('foo', mode='w') as w2:
            w2.write(msg1)
        with zipf.open('bar', mode='w') as w1:
            with self.assertRaises(ValueError):
                zipf.open('handle', mode='w')
            with self.assertRaises(ValueError):
                zipf.open('foo', mode='r')
            with self.assertRaises(ValueError):
                zipf.writestr('str', 'abcde')
            with self.assertRaises(ValueError):
                zipf.write(__file__, 'file')
            with self.assertRaises(ValueError):
                zipf.close()
            w1.write(msg2)
        with zipf.open('baz', mode='w') as w2:
            w2.write(msg3)
    with zipfile.ZipFile(TESTFN2, 'r') as zipf:
        self.assertEqual(zipf.read('foo'), msg1)
        self.assertEqual(zipf.read('bar'), msg2)
        self.assertEqual(zipf.read('baz'), msg3)
        self.assertEqual(zipf.namelist(), ['foo', 'bar', 'baz'])
