
import unittest

import os
import codecs

from unittest import skip

from cnab240 import errors
from cnab240.bancos import itau, banco_brasil
from cnab240.tipos import Arquivo
from tests.data import get_itau_data_from_dict, get_itau_file_remessa, \
        ARQS_DIRPATH, get_bb_data_from_dict


class TestCnab240(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestCnab240, self).__init__(*args, **kwargs)
        self.maxDiff = None

    def setUp(self):
        self.itau_data = get_itau_data_from_dict()
        self.bb_data = get_bb_data_from_dict()
        self.arquivo = Arquivo(itau, **self.itau_data['arquivo'])

    @skip
    def test_unicode(self):
        import pdb; pdb.set_trace()
        self.arquivo.incluir_cobranca(**self.itau_data['cobranca'])
        self.assertEqual(str(self.arquivo), get_itau_file_remessa())

    def test_empty_data(self):
        arquivo = Arquivo(itau)
        self.assertRaises(errors.ArquivoVazioError, str, arquivo)

    def test_leitura(self):
        return_file_path = os.path.join(ARQS_DIRPATH, 'cobranca.itau.ret')
        ret_file = codecs.open(return_file_path, encoding='ascii')
        arquivo = Arquivo(itau, arquivo=ret_file)
        ret_file.seek(0)
        self.assertEqual(ret_file.read(), str(arquivo))

    @skip
    def test_pagamento(self):
        arquivo = Arquivo(banco_brasil, **self.bb_data['arquivo'])
        arquivo.incluir_pagamentos_diversos(**self.bb_data['pagamento'])
        arquivo.lotes[0].header.codigo_convenio_banco
        print(str(arquivo))

if __name__ == '__main__':
    unittest.main()
