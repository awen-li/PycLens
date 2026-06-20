# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pydoc.py
# case: PydocImportTest_test_badimport

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    modname = 'testmod_xyzzy'
    testpairs = (('i_am_not_here', 'i_am_not_here'), ('test.i_am_not_here_either', 'test.i_am_not_here_either'), ('test.i_am_not_here.neither_am_i', 'test.i_am_not_here'), ('i_am_not_here.{}'.format(modname), 'i_am_not_here'), ('test.{}'.format(modname), 'test.{}'.format(modname)))
    sourcefn = os.path.join(TESTFN, modname) + os.extsep + 'py'
    for (importstring, expectedinmsg) in testpairs:
        with open(sourcefn, 'w') as f:
            f.write('import {}\n'.format(importstring))
        result = run_pydoc(modname, PYTHONPATH=TESTFN).decode('ascii')
        expected = badimport_pattern % (modname, expectedinmsg)
        self.assertEqual(expected, result)
