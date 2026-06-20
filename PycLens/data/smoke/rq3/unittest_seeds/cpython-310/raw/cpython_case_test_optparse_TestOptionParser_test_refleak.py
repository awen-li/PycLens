# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_optparse.py
# case: TestOptionParser_test_refleak

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    big_thing = [42]
    refcount = sys.getrefcount(big_thing)
    parser = OptionParser()
    parser.add_option('-a', '--aaarggh')
    parser.big_thing = big_thing
    parser.destroy()
    del parser
    self.assertEqual(refcount, sys.getrefcount(big_thing))
