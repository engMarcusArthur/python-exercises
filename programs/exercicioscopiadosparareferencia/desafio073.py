cbf = 'Flamengo', 'Santos', 'Palmeiras', 'Grêmio', \
      'Athletico', 'São Paulo', 'Internacional', 'Corinthians', \
      'Fortaleza', 'Goiás', 'Bahia', 'Vasco da Gama', 'Atlético', \
      'Fluminense', 'Botafogo', 'Ceará', 'Cruzeiro', 'CSA', \
      'Chapecoense', 'Avaí'
print(f'Zona de Classificação para Libertadores: {cbf[:5]}\n')
print(f'Zona de Rebaixamento: {cbf[-4:]}\n')
print(f'Lista de Equipes: {sorted(cbf)}\n')
print(f'A Chapecoense está na {cbf.index("Chapecoense") + 1}ª posição')
