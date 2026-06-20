# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_asyncore.py
# case: HelperFunctionTests_test_compact_traceback

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        raise Exception("I don't like spam!")
    except:
        (real_t, real_v, real_tb) = sys.exc_info()
        r = asyncore.compact_traceback()
    else:
        self.fail('Expected exception')
    ((f, function, line), t, v, info) = r
    self.assertEqual(os.path.split(f)[-1], 'test_asyncore.py')
    self.assertEqual(function, 'test_compact_traceback')
    self.assertEqual(t, real_t)
    self.assertEqual(v, real_v)
    self.assertEqual(info, '[%s|%s|%s]' % (f, function, line))
