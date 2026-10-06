import flet as ft

def main(page: ft.Page):
    page.title = "PizzaDev"

    nome = ft.Text("PizzaDev Pizzaria", size=32, weight=ft.FontWeight.BOLD)
    slogan = ft.Text("Sempre quentinha na sua mesa!", size=20, italic=True, weight=ft.FontWeight.NORMAL)
    estado = {"pizza": None, "tamanho": None}
    area_central = ft.Container(expand=True, padding=20)

    def mostrar_tela(conteudo):
        area_central.content = conteudo
        page.update()

    def mostrar_inicio(_=None):
        mostrar_tela(
            ft.Column(
                [
                    ft.Text("Início", size=24, weight=ft.FontWeight.BOLD),
                    ft.Text("Monte sua pizza escolhendo o sabor e o tamanho."),
                    ft.Button("Avançar", on_click=mostrar_cardapio),
                ],
                spacing=16,
            )
        )

    def mostrar_cardapio(_=None):
        mostrar_tela(
            ft.Column(
                [
                    ft.Text("Cardápio", size=24, weight=ft.FontWeight.BOLD),
                    ft.Text("Calabresa • Marguerita • Quatro queijos"),
                    ft.Row(
                        [
                            ft.Button("Voltar", on_click=mostrar_inicio),
                            ft.Button("Avançar", on_click=mostrar_selecao),
                        ]
                    ),
                ],
                spacing=16,
            )
        )

    def selecionar_pizza(pizza):
        estado["pizza"] = pizza
        mostrar_selecao()

    def selecionar_tamanho(tamanho):
        estado["tamanho"] = tamanho
        mostrar_selecao()

    def mostrar_selecao(_=None):
        pizza_atual = estado["pizza"] or "Nenhuma pizza selecionada"
        tamanho_atual = estado["tamanho"] or "Nenhum tamanho selecionado"
        mostrar_tela(
            ft.Column(
                [
                    ft.Text("Seleção", size=24, weight=ft.FontWeight.BOLD),
                    ft.Text(f"Pizza guardada: {pizza_atual}"),
                    ft.Row(
                        [
                            ft.Button("Calabresa", on_click=lambda _: selecionar_pizza("Calabresa")),
                            ft.Button("Marguerita", on_click=lambda _: selecionar_pizza("Marguerita")),
                            ft.Button("Quatro queijos", on_click=lambda _: selecionar_pizza("Quatro queijos")),
                        ],
                        wrap=True,
                    ),
                    ft.Text(f"Tamanho: {tamanho_atual}"),
                    ft.Row(
                        [
                            ft.Button("Pequena", on_click=lambda _: selecionar_tamanho("Pequena")),
                            ft.Button("Média", on_click=lambda _: selecionar_tamanho("Média")),
                            ft.Button("Grande", on_click=lambda _: selecionar_tamanho("Grande")),
                        ],
                        wrap=True,
                    ),
                    ft.Row(
                        [
                            ft.Button("Voltar", on_click=mostrar_cardapio),
                            ft.Button("Avançar", on_click=mostrar_resumo),
                        ]
                    ),
                ],
                spacing=16,
            )
        )

    def mostrar_resumo(_=None):
        mostrar_tela(
            ft.Column(
                [
                    ft.Text("Resumo do pedido", size=24, weight=ft.FontWeight.BOLD),
                    ft.Text(f"Pizza: {estado['pizza'] or 'Não selecionada'}"),
                    ft.Text(f"Tamanho: {estado['tamanho'] or 'Não selecionado'}"),
                    ft.Row(
                        [
                            ft.Button("Voltar", on_click=mostrar_selecao),
                            ft.Button("Início", on_click=mostrar_inicio),
                        ]
                    ),
                ],
                spacing=16,
            )
        )

    page.add(nome, slogan, area_central)
    mostrar_inicio()

ft.run(main)