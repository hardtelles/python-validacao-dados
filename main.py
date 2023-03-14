from cpf_cnpj import Documento
from validate_docbr import CPF
from validate_docbr import CNPJ
cnpj = "26611374000137"
cpf = "72749323495"
objeto_cnpj = Documento.cria_codumento(cnpj)

print("CNPJ: ", objeto_cnpj)

objeto_cpf = Documento.cria_codumento(cpf)
print("CPF: ", objeto_cpf)





