# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_exceptions.py
# case: ExceptionTests_test_WindowsError

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        WindowsError
    except NameError:
        pass
    else:
        self.assertIs(WindowsError, OSError)
        self.assertEqual(str(OSError(1001)), '1001')
        self.assertEqual(str(OSError(1001, 'message')), '[Errno 1001] message')
        w = OSError(9, 'foo', 'bar')
        self.assertEqual(w.errno, 9)
        self.assertEqual(w.winerror, None)
        self.assertEqual(str(w), "[Errno 9] foo: 'bar'")
        w = OSError(0, 'foo', 'bar', 3)
        self.assertEqual(w.errno, 2)
        self.assertEqual(w.winerror, 3)
        self.assertEqual(w.strerror, 'foo')
        self.assertEqual(w.filename, 'bar')
        self.assertEqual(w.filename2, None)
        self.assertEqual(str(w), "[WinError 3] foo: 'bar'")
        w = OSError(0, 'foo', None, 1001)
        self.assertEqual(w.errno, 22)
        self.assertEqual(w.winerror, 1001)
        self.assertEqual(w.strerror, 'foo')
        self.assertEqual(w.filename, None)
        self.assertEqual(w.filename2, None)
        self.assertEqual(str(w), '[WinError 1001] foo')
        w = OSError('bar', 'foo')
        self.assertEqual(w.errno, 'bar')
        self.assertEqual(w.winerror, None)
        self.assertEqual(w.strerror, 'foo')
        self.assertEqual(w.filename, None)
        self.assertEqual(w.filename2, None)
