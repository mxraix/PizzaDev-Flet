import flet as ft

def main(page: ft.Page):
    page.title = "PizzaDev"

    nome = ft.Text("PizzaDev Pizzaria", size=32, weight=ft.FontWeight.BOLD)
    slogan = ft.Text("Sempre quentinha na sua mesa!", size=20, italic=True, weight=ft.FontWeight.NORMAL)
    instrucao = ft.Text("Monte seu pedido abaixo e clique em 'Enviar pedido' para finalizar.", size=16, weight=ft.FontWeight.NORMAL)
    mensagem = ft.Text("", size=18, weight=ft.FontWeight.BOLD)

    pizzas = [
        {
            "nome": "Calabresa",
            "ingredientes": "Molho de tomate, muçarela, calabresa e cebola",
            "preco_m": 32.00,
            "preco_g": 42.00,
        },
        {
            "nome": "Margherita",
            "ingredientes": "Molho de tomate, muçarela, tomate e manjericão",
            "preco_m": 34.00,
            "preco_g": 48.00,
        },
        {
            "nome": "Portuguesa",
            "ingredientes": "Molho de tomate, muçarela, presunto, ovo, cebola e azeitona",
            "preco_m": 38.00,
            "preco_g": 53.00,
        },
        {
            "nome": "Frango com Catupiry",
            "ingredientes": "Molho de tomate, frango desfiado e requeijão cremoso",
            "preco_m": 39.00,
            "preco_g": 55.00,
        },
        {
            "nome": "Pizza Temporária",
            "ingredientes": "Molho de tomate, muçarela e manjericão",
            "preco_m": 30.00,
            "preco_g": 44.00,
        },
    ]

    def selecionar_pizza(e):
        mensagem.value = f"Selecionada: {e.control.data}"
        page.update()

    def criar_cartao(pizza):
        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text(pizza["nome"], size=22, weight=ft.FontWeight.BOLD),
                    ft.Text(pizza["ingredientes"], size=16),
                    ft.Row(
                        controls=[
                            ft.Text(f"M: R$ {pizza['preco_m']:.2f}"),
                            ft.Text(f"G: R$ {pizza['preco_g']:.2f}"),
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    ),
                    ft.Button(
                        "Selecionar",
                        data=pizza["nome"],
                        on_click=selecionar_pizza,
                    ),
                ],
                spacing=10,
            ),
            padding=16,
            border=ft.border.Border.all(1, ft.Colors.GREY_400),
            border_radius=8,
        )

    cartoes = [criar_cartao(pizza) for pizza in pizzas]


    pizzas = [
        ("Calabresa", "Molho de tomate, muçarela, calabresa e cebola", "R$ 35,00", "R$ 49,00"),
        ("Margherita", "Molho de tomate, muçarela, tomate e manjericão", "R$ 34,00", "R$ 48,00"),
        ("Portuguesa", "Molho de tomate, muçarela, presunto, ovo, cebola e azeitona", "R$ 38,00", "R$ 53,00"),
        ("Frango com Catupiry", "Molho de tomate, frango desfiado e requeijão cremoso", "R$ 39,00", "R$ 55,00"),
    ]

    cartoes = [
        ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text(sabor, size=22, weight=ft.FontWeight.BOLD),
                    ft.Text(ingredientes, size=16),
                    ft.Row(
                        controls=[
                            ft.Text(f"M: {preco_m}", size=16, weight=ft.FontWeight.BOLD),
                            ft.Text(f"G: {preco_g}", size=16, weight=ft.FontWeight.BOLD),
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    ),
                ],
                spacing=10,
            ),
            padding=16,
            border=ft.border.Border.all(1, ft.Colors.GREY_400),
            border_radius=8,
        )
        for sabor, ingredientes, preco_m, preco_g in pizzas
    ]

    conteudo = ft.Column(
        controls=[nome, slogan, instrucao, *cartoes],
        spacing=16,
        scroll=ft.ScrollMode.AUTO,
        expand=True,
    )

    posicionador = ft.Container(
            content=ft.Text("Durval C. M. Filho.", size=16, weight=ft.FontWeight.NORMAL),
            alignment=ft.Alignment.BOTTOM_LEFT,
            expand=False,
            padding=16,
                        border=ft.border.Border.all(1, ft.Colors.GREY_400),
                        border_radius=8,
    
        )

    page.add(conteudo, posicionador)

ft.run(main)