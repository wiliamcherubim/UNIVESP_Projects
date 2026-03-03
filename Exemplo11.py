# Inicialização dos contadores
votos_cand1 = 0
votos_cand2 = 0
votos_cand3 = 0
votos_branco = 0
votos_nulos = 0

print("--- Sistema de Votação ---")
print("Opções: 1, 2, 3 para candidatos | 4 para Branco | 0 para Encerrar")

while True:
    voto = int(input("\nDigite seu voto: "))

    if voto == 0:
        break
    elif voto == 1:
        votos_cand1 += 1
    elif voto == 2:
        votos_cand2 += 1
    elif voto == 3:
        votos_cand3 += 1
    elif voto == 4:
        votos_branco += 1
    elif voto not in [1, 2, 3, 4]:
        votos_nulos += 1
    #print("Voto inválido! Tente novamente.")

# Regra especial: Votos em branco vão para o Candidato 2
# total_cand2_final = votos_cand2 + votos_branco

# Exibição dos resultados
print("\n" + "=" * 20)
print("RESULTADO FINAL")
print(f"Candidato 1: {votos_cand1} votos")
print(f"Candidato 2: {votos_cand2} votos")
print(f"Candidato 3: {votos_cand3} votos")
print(f"Votos em branco: {votos_branco} votos")
print(f"Votos nulos: {votos_nulos} votos")