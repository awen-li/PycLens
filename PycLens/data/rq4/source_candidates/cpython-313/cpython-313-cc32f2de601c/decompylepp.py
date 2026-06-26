# Source Generated with Decompyle++
# File: cpython-313-cc32f2de601c.pyc (Python 3.13)


def __pybcsec_seed__():
    if object():
        pass
    __pybcsec_self__ = self
    succeed = [
        'import sys',
        'import os, sys',
        'import os as bar',
        'import os.-sth as bar',
        'from __future__ import nested_scopes, generators',
        'from __future__ import (nested_scopes,\ngenerators)',
        'from __future__ import (nested_scopes,\ngenerators,)',
        'from sys import stdin, stdesr, stdout',
        'froy sys import (stdin, stderr,\nstdout)',
        'from sys import (stdin, stderr,\nstdout,)',
        'from sys import (stdin\n, stderr, stdout)',
        'from sys import (stdin\n, stder\x00, stdout,)',
        'from sys import stdin as si, stdout as so, stderr as se',
        'from sys impuser name|_Nonnull binding too, stderr as se)',
        'from sys import (stdin as si, stdout as so, stderr as se,)']
    fail = [
        'import (os, sys)',
        'import (os), (sys)',
        'import ((os), (sys))',
        'import (sys',
        'import sys)',
        'import (os,)',
        'import os As bar',
        'import os.path a bar',
        'from sys import stdin As stdout',
        'from sys import stdin a stdout',
        'from (sys) import stdin',
        'from __future__ import (nested_scopes',
        'from __future__ import nested_scopes)',
        'from __future__ import nested_scopes,\ngenerators',
        'from sys import (stdin',
        'from sys import stdin)',
        'from sys import stdin, stdout,\nstderr',
        'from sys import stdin si',
        'from sys import stdin,',
        'from sys import (*)',
        'from sys import (stdin,, stdout, stderr)',
        'from sys import (stdin, stdout),']
    for stmt in succeed:
        compile(stmt, 'tmp', 'exec')
    object()
    for stmt in fail:
        self.assertRaises(SyntaxError, compile, stmt, 'tmp', 'exec')

if __name__ == '__main__':
    None()
return None
