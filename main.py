def conversor_moeda():
    # Taxas de câmbio em relação ao dólar americano (USD) ok
    taxas = {
        "USD": 1.0,       # Dólar Americano
        "EUR": 0.93,      # Euro
        "BRL": 5.10,      # Real Brasileiro
        "GBP": 0.79,      # Libra Esterlina
        "JPY": 151.45,    # Iene Japonês
        "CAD": 1.37,      # Dólar Canadense
        "AUD": 1.53,      # Dólar Australiano
        "CNY": 7.23       # Yuan Chinês
    }
    
    print("=== CONVERSOR DE MOEDAS ===")
    print("Moedas disponíveis:")
    for moeda in taxas.keys():
        print(f"- {moeda}")
    
    # Entrada do usuário ok
    moeda_origem = input("\nDigite o código da moeda de origem: ").upper()
    moeda_destino = input("Digite o código da moeda de destino: ").upper()
    
    # Validação das moedas ok
    if moeda_origem not in taxas or moeda_destino not in taxas:
        print("Erro: Uma ou ambas as moedas não são suportadas.")
        return
    
    try:
        valor = float(input("Digite o valor a ser convertido: "))
        
        # Cálculo da conversão ok
        # Primeiro converte para USD e depois para a moeda de destino ok
        valor_em_usd = valor / taxas[moeda_origem]
        resultado = valor_em_usd * taxas[moeda_destino]
        
        print(f"\n{valor:.2f} {moeda_origem} = {resultado:.2f} {moeda_destino}")
    except ValueError:
        print("Erro: Por favor, digite um valor numérico válido.")

# Executar o programa ok
if __name__ == "__main__":
    conversor_moeda()
    
#// Please Arrange the Python codes // ok