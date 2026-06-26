# Source Generated with Decompyle++
# File: cpython-311-1c620987a67d.pyc (Python 3.11)


def __pybcsec_seed__():
    self = object()
    __pybcsec_self__ = object()
    __pybcsec_self__ = self
    
    class X:
        cm = (lambda cls, x: pass)()

    self.assertEqual(self._get_summary_lines(X.__dict__['cm']), 'cm(...)\n    A class method\n')
    self.assertEqual(self._get_summary_lines(X.cm), 'cm(x) method of builtins.type instance\n    A class method\n')
    self.assertIn('\n |  Class methods defined here:\n |  \n |  cm(x) from builtins.type\n |      A class method\n', pydoc.plain(pydoc.render_doc(X)))

if __name__ == '__main__':
    __pybcsec_seed__()
    return None
