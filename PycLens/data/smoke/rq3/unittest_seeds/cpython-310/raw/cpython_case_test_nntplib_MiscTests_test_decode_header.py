# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_nntplib.py
# case: MiscTests_test_decode_header

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def gives(a, b):
        self.assertEqual(nntplib.decode_header(a), b)
    gives('', '')
    gives('a plain header', 'a plain header')
    gives(' with extra  spaces ', ' with extra  spaces ')
    gives('=?ISO-8859-15?Q?D=E9buter_en_Python?=', 'Débuter en Python')
    gives('=?utf-8?q?Re=3A_=5Bsqlite=5D_probl=C3=A8me_avec_ORDER_BY_sur_des_cha?= =?utf-8?q?=C3=AEnes_de_caract=C3=A8res_accentu=C3=A9es?=', 'Re: [sqlite] problème avec ORDER BY sur des chaînes de caractères accentuées')
    gives('Re: =?UTF-8?B?cHJvYmzDqG1lIGRlIG1hdHJpY2U=?=', 'Re: problème de matrice')
    gives("Re: Message d'erreur incompréhensible (par moi)", "Re: Message d'erreur incompréhensible (par moi)")
