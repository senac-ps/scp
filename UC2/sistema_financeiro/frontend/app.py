import flet as ft
import requests
from datetime import date

API_URL = "http://127.0.0.1:8000/transacoes/"

def main(page: ft.Page):
    page.title = "Controle Financeiro"
    page.theme_mode = "dark"
    page.padding = 20
    page.scroll = "auto" # Permite rolar a tela se for muito pequena

    # --- 1. Dashboard (Resumo) ---
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

    # --- 2. Formulário de Cadastro ---
    txt_titulo = ft.TextField(label="Descrição", width=200)
    txt_valor = ft.TextField(label="Valor", width=100, keyboard_type="number")
    
    # Seletor simplificado
    radio_tipo = ft.RadioGroup(
        content=ft.Row([
            ft.Radio(value="despesa", label="Despesa"),
            ft.Radio(value="receita", label="Receita"),
        ]),
        value="despesa"
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

    # Lista de rolagem
    lista_transacoes = ft.Column()

    # --- Lógica do Sistema ---

    def calcular_resumo(transacoes):
        total_receita = 0.0
        total_despesa = 0.0

        for t in transacoes:
            valor = t['valor']
            tipo = t.get('tipo', 'despesa') # Proteção contra dados antigos
            
            if tipo == 'receita':
                total_receita += valor
            else:
                total_despesa += valor
        
        saldo = total_receita - total_despesa

        txt_saldo.value = f"R$ {saldo:.2f}"
        txt_receita.value = f"+ R$ {total_receita:.2f}"
        txt_despesa.value = f"- R$ {total_despesa:.2f}"
        txt_saldo.color = "red" if saldo < 0 else "white"

    def carregar_dados():
        try:
            response = requests.get(API_URL)
            if response.status_code == 200:
                transacoes = response.json()
                calcular_resumo(transacoes)
                
                lista_transacoes.controls.clear()
                
                for t in reversed(transacoes):
                    tipo = t.get('tipo', 'despesa')
                    
                    # AQUI MUDAMOS: Usamos Emojis em vez de ft.Icon para evitar erros
                    if tipo == 'despesa':
                        emoji = "⬇"
                        cor = "red"
                    else:
                        emoji = "⬆"
                        cor = "green"

                    lista_transacoes.controls.append(
                        ft.Container(
                            content=ft.Row([
                                ft.Text(emoji, color=cor, size=20, weight="bold"), # Emoji simples
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
            # Mostra erro na tela se houver
            page.add(ft.Text(f"Erro de Conexão: {e}", color="red"))
            page.update()

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
            "tipo": radio_tipo.value,
            "categoria": dd_categoria.value or "Outros",
            "data": str(date.today())
        }

        try:
            requests.post(API_URL, json=payload)
            txt_titulo.value = ""
            txt_valor.value = ""
            carregar_dados()
            page.update()
        except Exception as e:
            print(f"Erro ao salvar: {e}")

    # Botão simples (compatível com qualquer versão)
    btn_adicionar = ft.ElevatedButton("Salvar Lançamento", on_click=adicionar_gasto)

    # --- Montagem da Tela ---
    page.add(
        ft.Text("Meu Financeiro", size=24, weight="bold"),
        container_saldo,
        ft.Divider(),
        ft.Text("Novo Lançamento", size=16),
        radio_tipo,
        ft.Row([txt_titulo, txt_valor]),
        dd_categoria,
        btn_adicionar,
        ft.Divider(),
        ft.Text("Histórico", size=16),
        lista_transacoes
    )

    carregar_dados()

ft.app(target=main)