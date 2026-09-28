import flet as ft

def main(page: ft.Page):
    page.title = "PizzaDev"

    nome = ft.Text("PizzaDev Pizzaria", size=32, weight=ft.FontWeight.BOLD)
    slogan = ft.Text("Sempre quentinha na sua mesa!", size=20, italic=True, weight=ft.FontWeight.NORMAL)
    instrucao = ft.Text("Monte seu pedido abaixo e clique em 'Enviar pedido' para finalizar.", size=16, weight=ft.FontWeight.NORMAL)
    mensagem = ft.Text("", size=18, weight=ft.FontWeight.BOLD)

    pizzas = [
        ("Calabresa", "Molho de tomate, muçarela, calabresa e cebola", "R$ 35,00", "R$ 49,00"),
        ("Margherita", "Molho de tomate, muçarela, tomate e manjericão", "R$ 34,00", "R$ 48,00"),
        ("Portuguesa", "Molho de tomate, muçarela, presunto, ovo, cebola e azeitona", "R$ 38,00", "R$ 53,00"),
        ("Frango com Catupiry", "Molho de tomate, frango desfiado e requeijão cremoso", "R$ 39,00", "R$ 55,00"),
    ]

    def selecionar_pizza(sabor):
        mensagem.value = f"Selecionada: {sabor}"
        page.update()

    cartoes = []
    for sabor, ingredientes, preco_m, preco_g in pizzas:
        cartoes.append(
            ft.Container(
                content=ft.Column(
                    controls=[
                        ft.Text(sabor, size=22, weight=ft.FontWeight.BOLD),
                        ft.Text(ingredientes, size=16),
                        ft.Row(
                            controls=[
                                ft.Text(f"M: {preco_m}"),
                                ft.Text(f"G: {preco_g}"),
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        ),
                        ft.Button(
                            "Selecionar",
                            on_click=lambda e, nome=sabor: selecionar_pizza(nome),
                        ),
                    ],
                    spacing=10,
                ),
                padding=16,
                border=ft.border.Border.all(1, ft.Colors.GREY_400),
                border_radius=8,
            )
        )

    posicionador = ft.Container(
                content=ft.Text("Durval C. M. Filho", size=16, weight=ft.FontWeight.NORMAL),
                alignment=ft.Alignment.BOTTOM_LEFT,
                expand=False,
                padding=10,
                border=ft.border.Border.all(1, ft.Colors.GREY_400),
                                border_radius=8,
        
            )

    page.add(
        ft.Column(
            controls=[nome, slogan, instrucao, mensagem, *cartoes, posicionador],
            spacing=16,
            scroll=ft.ScrollMode.AUTO,
            expand=True,
        )
    )

ft.run(main)