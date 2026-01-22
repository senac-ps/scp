import flet as ft
import requests
from datetime import date

API_URL = "http://127.0.0.1:8000/transacoes/"

def main(page: ft.Page):
    page.title = "Controle Financeiro"
    page.theme_mode = "dark"
    page.padding = 20

    # --- Elementos da Interface ---

    # 1. Dashboard (Cards de Resumo)
    txt_saldo = ft.Text("R$ 0.00", size=30, weight="bold")
    txt_receita = ft.Text("R$ 0.00", color="green")
    txt_despesa = ft.Text("R$ 0.00", color="red")

    container_saldo = ft.Container(
        content=ft.Column([
            ft.Text("Saldo Atual"),
            txt_saldo,
            ft.Row([
                ft.Column([ft.Text("Receitas"), txt_receita]),
                ft.Column([ft.Text("Despesas"), txt_despesa]),
            ], alignment="spaceBetween")
        ]),
        padding=20,
        bgcolor="black26",
        border_radius=10,
        width=350
    )

    # 2. Formulário
    txt_titulo = ft.TextField(label="Descrição", width=200)
    txt_valor = ft.TextField(label="Valor", width=100, keyboard_type="number")
    
    # Seletor de Tipo (Receita ou Despesa)
    radio_tipo = ft.RadioGroup(
        content=ft.Row([
            ft.Radio(value="despesa", label="Despesa"),
            ft.Radio(value="receita", label="Receita"),
        ]),
        value="despesa" # Padrão
    )

    dd_categoria = ft.Dropdown(
        label="Categoria",
        width=300,
        options=[
            ft.dropdown.Option("Alimentação"),
            ft.dropdown.Option("Transporte"),
            ft.dropdown.Option("Lazer"),
            ft.dropdown.Option("Salário"),
            ft.dropdown.Option("Contas"),
        ],
    )

    # 3. Lista de Transações
    lista_transacoes = ft.Column(scroll="auto", height=300)

    # --- Lógica ---

    def calcular_resumo(transacoes):
        """Faz a matemática do dinheiro"""
        total_receita = 0.0
        total_despesa = 0.0

        for t in transacoes:
            valor = t['valor']
            if t['tipo'] == 'receita':
                total_receita += valor
            else:
                total_despesa += valor
        
        saldo = total_receita - total_despesa

        # Atualiza os textos na tela
        txt_saldo.value = f"R$ {saldo:.2f}"
        txt_receita.value = f"+ R$ {total_receita:.2f}"
        txt_despesa.value = f"- R$ {total_despesa:.2f}"
        
        # Muda a cor do saldo se estiver negativo
        txt_saldo.color = "red" if saldo < 0 else "white"

    def carregar_dados():
        try:
            response = requests.get(API_URL)
            if response.status_code == 200:
                transacoes = response.json()
                calcular_resumo(transacoes) # Chama a calculadora
                
                lista_transacoes.controls.clear()
                
                # Inverte a lista para o mais recente aparecer primeiro
                for t in reversed(transacoes):
                    icone = ft.Icon(ft.icons.ARROW_DOWNWARD, color="red") if t['tipo'] == 'despesa' else ft.Icon(ft.icons.ARROW_UPWARD, color="green")
                    
                    lista_transacoes.controls.append(
                        ft.Container(
                            content=ft.Row([
                                icone,
                                ft.Column([
                                    ft.Text(t["titulo"], weight="bold"),
                                    ft.Text(t["categoria"], size=12, italic=True)
                                ], expand=True),
                                ft.Text(f"R$ {t['valor']:.2f}", weight="bold")
                            ]),
                            padding=10,
                            border=ft.border.only(bottom=ft.border.BorderSide(1, "grey")),
                        )
                    )
                page.update()
        except Exception as e:
            print(f"Erro: {e}")

    def adicionar_gasto(e):
        if not txt_titulo.value or not txt_valor.value:
            return

        try:
            valor_formatado = float(txt_valor.value.replace(",", "."))
        except ValueError:
            return

        payload = {
            "titulo": txt_titulo.value,
            "valor": valor_formatado,
            "tipo": radio_tipo.value, # Pega o valor do seletor (receita/despesa)
            "categoria": dd_categoria.value or "Outros",
            "data": str(date.today())
        }

        try:
            requests.post(API_URL, json=payload)
            # Limpa campos
            txt_titulo.value = ""
            txt_valor.value = ""
            carregar_dados()
            page.update()
        except Exception as e:
            print(f"Erro ao salvar: {e}")

    btn_adicionar = ft.ElevatedButton("Salvar", on_click=adicionar_gasto, width=300)

    # --- Montagem Final ---
    page.add(
        ft.Text("Meu Financeiro", size=24, weight="bold"),
        container_saldo, # O novo painel de resumo
        ft.Divider(),
        ft.Text("Novo Lançamento", size=16),
        radio_tipo, # O seletor novo
        ft.Row([txt_titulo, txt_valor]),
        dd_categoria,
        btn_adicionar,
        ft.Divider(),
        ft.Text("Histórico", size=16),
        lista_transacoes
    )

    carregar_dados()
    def carregar_dados():
        try:
            response = requests.get(API_URL)
            if response.status_code == 200:
                transacoes = response.json()
                calcular_resumo(transacoes)
                
                lista_transacoes.controls.clear()
                
                for t in reversed(transacoes):
                    # Verifica se o tipo existe, se não, assume 'despesa' para evitar erro
                    tipo_transacao = t.get('tipo', 'despesa')
                    icone = ft.Icon(ft.icons.ARROW_DOWNWARD, color="red") if tipo_transacao == 'despesa' else ft.Icon(ft.icons.ARROW_UPWARD, color="green")
                    
                    lista_transacoes.controls.append(
                        ft.Container(
                            content=ft.Row([
                                icone,
                                ft.Column([
                                    ft.Text(t["titulo"], weight="bold"),
                                    ft.Text(t["categoria"], size=12, italic=True)
                                ], expand=True),
                                ft.Text(f"R$ {t['valor']:.2f}", weight="bold")
                            ]),
                            padding=10,
                            border=ft.border.only(bottom=ft.border.BorderSide(1, "grey")),
                        )
                    )
                page.update()
        except Exception as e:
            # ESTA É A PARTE IMPORTANTE QUE VAI TE MOSTRAR O ERRO
            page.snack_bar = ft.SnackBar(ft.Text(f"Erro ao carregar: {e}"), bgcolor="red")
            page.snack_bar.open = True
            page.update()
            print(f"ERRO DETALHADO: {e}")

ft.app(target=main)