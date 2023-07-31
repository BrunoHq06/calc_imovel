import streamlit as st

def calculadora_imovel_ou_aluguel(valor_aluguel, valor_imovel, valorizacao_imovel, taxa_juros_aluguel, taxa_juros_aplicacao, horizonte_anos):
    montante_investimento = valor_imovel
    montante_comprado = valor_imovel
    aluguel_acumulado = 0

    for ano in range(1, horizonte_anos + 1):
        # Atualização do valor do aluguel
        valor_aluguel *= (1 + taxa_juros_aluguel)
        aluguel_acumulado += valor_aluguel * 12

        # Atualiza o valor do montante investido com base na taxa de juros informada
        montante_investimento += (montante_investimento * taxa_juros_aplicacao)

        # Atualiza o valor do imóvel para o próximo ano com a valorização
        montante_comprado *= (1 + valorizacao_imovel)

    dicionario_retorno = {'valor_imóvel':round(montante_comprado,2),
                        'valor_rendimento':round(montante_investimento,2),
                        'valor_descontado':round(montante_investimento - aluguel_acumulado,2)}
    
    return dicionario_retorno
    
st.title("Decisão: Comprar ou Alugar um Imóvel?")

# Criação do formulário utilizando o Streamlit
with st.form("input_form"):
    col1, col2 = st.columns(2)  # Divisão em duas colunas
    
    with col1:
        # Number input para Valor do Aluguel
        valor_aluguel = st.number_input("Valor do Aluguel (ao mês)", value=1000.0, min_value=0.0)
        # Number input para Taxa de Juros do Aluguel
        taxa_juros_aluguel = st.number_input("Taxa de Juros do Aluguel (Anual)", value=0.03,step=0.001,format="%.3f")
        # Number input para Taxa de Juros da Aplicação
        taxa_juros_aplicacao = st.number_input("Taxa de Juros da Aplicação (Anual)", value=0.06,step=0.001,format="%.3f")  
    
    with col2:
        # Number input para Valor do Imóvel
        valor_imovel = st.number_input("Valor do Imóvel", value=300000.0,min_value=0.0)
        # Number input para Valorização do Imóvel
        valorizacao_imovel = st.number_input("Valorização do Imóvel (Anual)", value=0.05,step=0.001,format="%.3f")
        # Number input para Horizonte de Anos
        horizonte_anos = st.number_input("Horizonte de Anos", value=20,min_value=1)
    
    # Botão para enviar os dados e obter a resposta
    submit_button = st.form_submit_button(label='Calcular')

if submit_button:
    # Chama a função para tomar a decisão e mostra o resultado na tela
    resultado_dicionario = calculadora_imovel_ou_aluguel(valor_aluguel, valor_imovel, valorizacao_imovel, taxa_juros_aluguel, taxa_juros_aplicacao, horizonte_anos)
    
    if resultado_dicionario['valor_descontado'] > resultado_dicionario['valor_imóvel']:
        resultado = 'Sugestão: Alugar o imóvel'
    else:
        resultado = 'Seguestão: Comprar o imóvel'
    
    st.write(f'Valor Final do rendimento: {resultado_dicionario["valor_descontado"]:,}')
    st.write(f'Valor Final do imóvel: {resultado_dicionario["valor_imóvel"]:,}')
    st.write(resultado)