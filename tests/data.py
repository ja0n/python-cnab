
import os
import codecs
from decimal import Decimal
from cnab240.bancos import itau
from cnab240.tipos import Lote, Evento

TESTS_DIRPATH = os.path.abspath(os.path.dirname(__file__))
ARQS_DIRPATH = os.path.join(TESTS_DIRPATH, 'arquivos')


def get_itau_data_from_file():
    itau_data = dict()
    arquivo_remessa = codecs.open(os.path.join(ARQS_DIRPATH,
                                  'cobranca.itau.rem'), encoding='ascii')

    itau_data['remessa'] = arquivo_remessa.read()
    arquivo_remessa.seek(0)

    itau_data['header_arquivo'] = itau.registros.HeaderArquivo()
    itau_data['header_arquivo_str'] = arquivo_remessa.readline().strip('\r\n')
    itau_data['header_arquivo'].carregar(itau_data['header_arquivo_str'])

    itau_data['header_lote'] = itau.registros.HeaderLoteCobranca()
    itau_data['header_lote_str'] = arquivo_remessa.readline().strip('\r\n')
    itau_data['header_lote'].carregar(itau_data['header_lote_str'])

    itau_data['seg_p1'] = itau.registros.SegmentoP()
    itau_data['seg_p1_str'] = arquivo_remessa.readline().strip('\r\n')
    itau_data['seg_p1'].carregar(itau_data['seg_p1_str'])

    itau_data['seg_q1'] = itau.registros.SegmentoQ()
    itau_data['seg_q1_str'] = arquivo_remessa.readline().strip('\r\n')
    itau_data['seg_q1'].carregar(itau_data['seg_q1_str'])

    itau_data['seg_p2'] = itau.registros.SegmentoP()
    itau_data['seg_p2_str'] = arquivo_remessa.readline().strip('\r\n')
    itau_data['seg_p2'].carregar(itau_data['seg_p2_str'])

    itau_data['seg_q2'] = itau.registros.SegmentoQ()
    itau_data['seg_q2_str'] = arquivo_remessa.readline().strip('\r\n')
    itau_data['seg_q2'].carregar(itau_data['seg_q2_str'])

    itau_data['trailer_lote'] = itau.registros.TrailerLoteCobranca()
    itau_data['trailer_lote_str'] = arquivo_remessa.readline().strip('\r\n')
    itau_data['trailer_lote'].carregar(itau_data['trailer_lote_str'])

    itau_data['trailer_arquivo'] = itau.registros.TrailerArquivo()
    itau_data['trailer_arquivo_str'] = arquivo_remessa.readline().strip('\r\n')
    itau_data['trailer_arquivo'].carregar(itau_data['trailer_arquivo_str'])

    itau_data['lote_cob'] = Lote(itau, itau_data['header_lote'],
                                 itau_data['trailer_lote'])
    itau_data['evento_cob1'] = Evento(itau, 1)
    itau_data['evento_cob1'].adicionar_segmento(itau_data['seg_p1'])
    itau_data['evento_cob1'].adicionar_segmento(itau_data['seg_q1'])

    itau_data['evento_cob2'] = Evento(itau, 1)
    itau_data['evento_cob2'].adicionar_segmento(itau_data['seg_p2'])
    itau_data['evento_cob2'].adicionar_segmento(itau_data['seg_q2'])

    arquivo_remessa.close()
    return itau_data


def get_itau_data_from_dict():
    itau_data = dict()
    dict_arquivo = {
        'cedente_inscricao_tipo': 2,
        'cedente_inscricao_numero': 15594050000111,
        'cedente_agencia': 4459,
        'cedente_conta': 17600,
        'cedente_agencia_conta_dv': 6,
        'cedente_nome': "TRACY TECNOLOGIA LTDA ME",
        'arquivo_data_de_geracao': 27062012,
        'arquivo_hora_de_geracao': 112000,
        'arquivo_sequencia': 900002
    }

    dict_cobranca = {
        'cedente_agencia': 4459,
        'cedente_conta': 17600,
        'cedente_agencia_conta_dv': 6,
        'carteira_numero': 109,
        'nosso_numero': 99999999,
        'nosso_numero_dv': 9,
        'numero_documento': '9999999999',
        'vencimento_titulo': 30072012,
        'valor_titulo': Decimal('100.00'),
        'especie_titulo': 8,
        'aceite_titulo': 'A',
        'data_emissao_titulo': 27062012,
        'juros_mora_taxa_dia': Decimal('2.00'),
        'valor_abatimento': Decimal('0.00'),
        'identificacao_titulo': 'BOLETO DE TESTE',
        'codigo_protesto': 3,
        'prazo_protesto': 0,
        'codigo_baixa': 0,
        'prazo_baixa': 0,
        'sacado_inscricao_tipo': 1,
        'sacado_inscricao_numero': 83351622120,
        'sacado_nome': 'JESUS DO CEU',
        'sacado_endereco': 'RUA AVENIDA DO CEU, 666',
        'sacado_bairro': 'JD PARAISO',
        'sacado_cep': 60606,
        'sacado_cep_sufixo': 666,
        'sacado_cidade': 'PARAISO DE DEUS',
        'sacado_uf': 'SP',
    }

    itau_data['arquivo'] = dict_arquivo
    itau_data['cobranca'] = dict_cobranca

    return itau_data


def get_itau_file_remessa():
    arquivo_remessa = codecs.open(
        os.path.join(ARQS_DIRPATH, 'cobranca_dict.itau.rem'), encoding='ascii')
    arquivo_data = arquivo_remessa.read()
    arquivo_remessa.close()
    return arquivo_data


def get_bb_data_from_dict():
    # bb stands for banco_brasil
    bb_data = dict()
    dict_arquivo = {
        'cedente_inscricao_tipo': 2,
        'cedente_inscricao_numero': 15594050000111,
        'cedente_agencia': 4459,
        'cedente_conta': 17600,
        'cedente_agencia_conta_dv': 6,
        'cedente_nome': "TRACY TECNOLOGIA LTDA ME",
        'arquivo_data_de_geracao': 27062012,
        'arquivo_hora_de_geracao': 112000,
        'arquivo_sequencia': 900002
    }

    dict_pagamento = {
        'codigo_convenio_banco': '9999999990014CCVVVTS',
        'test_banco_brasil': True,
        'cedente_agencia': 4459,
        'cedente_conta': 17600,
        'cedente_agencia_conta_dv': 6,
        'cedente_endereco': 'RUA AVENIDA DO CEU',
        'cedente_endereco_numero': 665,
        'cedente_bairro': 'JD PARAISO',
        'cedente_cep': 60606,
        'cedente_cep_sufixo': '666',
        'cedente_cidade': 'PARAISO DE DEUS',
        'favorecido_uf': 'SP',
        'carteira_numero': 109,
        'nosso_numero': 99999999,
        'nosso_numero_dv': 9,
        'numero_documento': '9999999999',
        'vencimento_titulo': 30072012,
        'valor_titulo': Decimal('100.00'),
        'especie_titulo': 8,
        'aceite_titulo': 'A',
        'data_emissao_titulo': 27062012,
        'juros_mora_taxa_dia': Decimal('2.00'),
        'valor_abatimento': Decimal('0.00'),
        'identificacao_titulo': 'BOLETO DE TESTE',
        'codigo_protesto': 3,
        'prazo_protesto': 0,
        'codigo_baixa': 0,
        'prazo_baixa': 0,
        'favorecido_agencia_dv': 'X',
        'favorecido_conta_dv': 'X',
        'favorecido_agencia_conta_dv': 'X',
        'favorecido_inscricao_tipo': 1,
        'favorecido_inscricao_numero': 83351622120,
        'favorecido_nome': 'JESUS DO CEU',
        'favorecido_endereco': 'RUA AVENIDA DO CEU',
        'favorecido_endereco_numero': 666,
        'favorecido_bairro': 'JD PARAISO',
        'favorecido_cep': 60606,
        'favorecido_cep_sufixo': '666',
        'favorecido_cidade': 'PARAISO DE DEUS',
        'favorecido_uf': 'SP',
        'quantidade_moeda': Decimal('1000000000.00000'),
        'valor': Decimal('1200.00'),
        'valor_real': Decimal('1200.00'),
        'abatimento': Decimal('0.00'),
        'desconto': Decimal('0.00'),
        'juros_mora': Decimal('0.00'),
        'multa': Decimal('0.00'),
    }

    bb_data['arquivo'] = dict_arquivo
    bb_data['pagamento'] = dict_pagamento

    return bb_data
