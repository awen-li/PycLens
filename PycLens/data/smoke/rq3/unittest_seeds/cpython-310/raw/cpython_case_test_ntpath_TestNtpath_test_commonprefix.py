# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ntpath.py
# case: TestNtpath_test_commonprefix

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tester('ntpath.commonprefix(["/home/swenson/spam", "/home/swen/spam"])', '/home/swen')
    tester('ntpath.commonprefix(["\\home\\swen\\spam", "\\home\\swen\\eggs"])', '\\home\\swen\\')
    tester('ntpath.commonprefix(["/home/swen/spam", "/home/swen/spam"])', '/home/swen/spam')
