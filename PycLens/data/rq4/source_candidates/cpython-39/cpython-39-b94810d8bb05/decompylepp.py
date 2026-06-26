# Source Generated with Decompyle++
# File: cpython-39-b94810d8bb05.pyc (Python 3.9)


def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    import array
    contents = (lambda .0: [ (20 - i) * 0.1 for i in .0 ])(range(20))
    array = None
    a = None.array('d', contents)
    with TemporaryFile('w+', '', **('newline',)) as fileobj:
        writer = csv.writer(fileobj, 'excel', **('dialect',))
        writer.writerow(a)
        expected = ','.join((lambda .0: [ str(i) for i in .0 ])(a)) + '\r\n'
        fileobj.seek(0)
        self.assertEqual(fileobj.read(), expected)
        None(None, None, None)
    with None:
        if not None:
            pass

if __name__ == '__main__':
    __pybcsec_seed__()
