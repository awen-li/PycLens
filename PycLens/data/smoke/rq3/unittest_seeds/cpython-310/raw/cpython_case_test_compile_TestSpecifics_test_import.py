# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_compile.py
# case: TestSpecifics_test_import

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    succeed = ['import sys', 'import os, sys', 'import os as bar', 'import os.path as bar', 'from __future__ import nested_scopes, generators', 'from __future__ import (nested_scopes,\ngenerators)', 'from __future__ import (nested_scopes,\ngenerators,)', 'from sys import stdin, stderr, stdout', 'from sys import (stdin, stderr,\nstdout)', 'from sys import (stdin, stderr,\nstdout,)', 'from sys import (stdin\n, stderr, stdout)', 'from sys import (stdin\n, stderr, stdout,)', 'from sys import stdin as si, stdout as so, stderr as se', 'from sys import (stdin as si, stdout as so, stderr as se)', 'from sys import (stdin as si, stdout as so, stderr as se,)']
    fail = ['import (os, sys)', 'import (os), (sys)', 'import ((os), (sys))', 'import (sys', 'import sys)', 'import (os,)', 'import os As bar', 'import os.path a bar', 'from sys import stdin As stdout', 'from sys import stdin a stdout', 'from (sys) import stdin', 'from __future__ import (nested_scopes', 'from __future__ import nested_scopes)', 'from __future__ import nested_scopes,\ngenerators', 'from sys import (stdin', 'from sys import stdin)', 'from sys import stdin, stdout,\nstderr', 'from sys import stdin si', 'from sys import stdin,', 'from sys import (*)', 'from sys import (stdin,, stdout, stderr)', 'from sys import (stdin, stdout),']
    for stmt in succeed:
        compile(stmt, 'tmp', 'exec')
    for stmt in fail:
        self.assertRaises(SyntaxError, compile, stmt, 'tmp', 'exec')
