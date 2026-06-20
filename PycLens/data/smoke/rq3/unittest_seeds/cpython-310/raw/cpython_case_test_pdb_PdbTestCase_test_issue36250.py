# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pdb.py
# case: PdbTestCase_test_issue36250

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with open(os_helper.TESTFN, 'wb') as f:
        f.write(textwrap.dedent('\n                import threading\n                import pdb\n\n                evt = threading.Event()\n\n                def start_pdb():\n                    evt.wait()\n                    pdb.Pdb(readrc=False).set_trace()\n\n                t = threading.Thread(target=start_pdb)\n                t.start()\n                pdb.Pdb(readrc=False).set_trace()\n                evt.set()\n                t.join()').encode('ascii'))
    cmd = [sys.executable, '-u', os_helper.TESTFN]
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.STDOUT, env={**os.environ, 'PYTHONIOENCODING': 'utf-8'})
    self.addCleanup(proc.stdout.close)
    (stdout, stderr) = proc.communicate(b'cont\ncont\n')
    self.assertNotIn(b'Error', stdout, 'Got an error running test script under PDB')
