import flet as ft

def main(page: ft.Page):
    page.title = "PizzaDev"

    nome = ft.Text("PizzaDev Pizzaria", size=32, weight=ft.FontWeight.BOLD)
    slogan = ft.Text("Sempre quentinha na sua mesa!", size=20, italic=True, weight=ft.FontWeight.NORMAL)
    instrucao = ft.Text("Monte seu pedido abaixo e clique em 'Enviar pedido' para finalizar.", size=16, weight=ft.FontWeight.NORMAL)
    mensagem = ft.Text("", size=18, weight=ft.FontWeight.BOLD)

    quantidade = ft.TextField(
        label="Quantidade",
        keyboard_type=ft.KeyboardType.NUMBER,
        width=200,
    )
    tamanho = ft.RadioGroup(
        content=ft.Row(
            controls=[
                ft.Radio(label="M", value="M"),
                ft.Radio(label="G", value="G"),
            ]
        ),
        value="M",
    )

    def calcular(e):
        valor = quantidade.value.strip()
        if not valor.isdigit() or not 1 <= int(valor) <= 10:
            mensagem.value = "Informe uma quantidade entre 1 e 10."
        else:
            preco = 32 if tamanho.value == "M" else 42
            parcial = int(valor) * preco
            mensagem.value = f"Parcial: R$ {parcial},00"
        page.update()

    posicionador = ft.Container(
                content=ft.Text("Durval C. M. Filho", size=16, weight=ft.FontWeight.NORMAL),
                alignment=ft.Alignment.BOTTOM_LEFT,
                expand=False,
                padding=10,
                border=ft.border.Border.all(1, ft.Colors.GREY_400),
                                border_radius=8,
        
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
            controls=[
                nome,
                slogan,
                instrucao,
                ft.Text("Pizza Calabresa", size=22, weight=ft.FontWeight.BOLD),
                ft.Text("M: R$ 32,00   |   G: R$ 42,00"),
                quantidade,
                tamanho,
                ft.Button("Calcular", on_click=calcular),
                mensagem,
                posicionador,
            ],
            spacing=16,
            scroll=ft.ScrollMode.AUTO,
            expand=True,
        )
    )

ft.run(main)