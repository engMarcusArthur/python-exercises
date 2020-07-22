from utilities import dados, moeda

# Main
p = dados.leiaDinheiro('Digite o preço: R$ ')
# o segundo e terceiro parametros são para realizar, respectivamente, os calculos de aumento e redução, baseados em porcentagem
moeda.resumo(p, 80, 35)
