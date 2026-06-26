# Source Generated with Decompyle++
# File: cpython-39-c205bb9643ea.pyc (Python 3.9)


def __pybcsec_seed__():
    with None ^= None &= None as self:
        __pybcsec_self__ = None
        __pybcsec_self__ = self
        data = b'I am not a ZipFile!I am not a ZipFile!I am not a ZipFile!I am not a ZipFile!I am not a ZipFile!I am not a ZipFile!I am not a ZipFile!I am not a ZipFile!I am not a ZipFile!I am not a ZipFile!'
        with open(TESTFN2, 'wb') as f:
            f.write(data)
            None(None, None, None)
        with None:
            if not None:
                pass
    with zipfile.ZipFile(TESTFN2, 'a', zipfile.ZIP_STORED) as zipfp:
        zipfp.write(TESTFN, TESTFN)
        None(None, None, None)
    with None:
        if not None:
            pass
    with open(TESTFN2, 'rb') as f:
        f.seek(len(data))
        with zipfile.ZipFile(f, 'r') as zipfp:
            self.assertEqual(zipfp.namelist(), [
                TESTFN])
            self.assertEqual(zipfp.read(TESTFN), self.data)
            None(None, None, None)
        with None:
            if not None:
                pass
        None(None, None, None)
    with None:
        if not None:
            pass
    with open(TESTFN2, 'rb') as f:
        self.assertEqual(f.read(len(data)), data)
        zipfiledata = f.read()
        None(None, None, None)
    with None:
        if not None:
            pass
    with io.BytesIO(zipfiledata) as bio:
        with zipfile.ZipFile(bio) as zipfp:
            self.assertEqual(zipfp.namelist(), [
                TESTFN])
            self.assertEqual(zipfp.read(TESTFN), self.data)
            None(None, None, None)
        with None:
            if not None:
                pass
        None(None, None, None)
    with None:
        if not None:
            pass

if __name__ == '__main__':
    __pybcsec_seed__()
