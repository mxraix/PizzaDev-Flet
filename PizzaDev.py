import flet as ft

def main(page: ft.Page):
    page.title = "PizzaDev"

    nome = ft.Text("PizzaDev Pizzaria", size=32, weight=ft.FontWeight.BOLD)
    slogan = ft.Text("Sempre quentinha na sua mesa!", size=20, italic=True, weight=ft.FontWeight.NORMAL)
    instrucao = ft.Text("Monte seu pedido abaixo e clique em 'Enviar pedido' para finalizar.", size=16, weight=ft.FontWeight.NORMAL)

    posicionador = ft.Container(
        content=ft.Text("Durval C. M. Filho", size=16, weight=ft.FontWeight.NORMAL),
        alignment=ft.Alignment.BOTTOM_LEFT,
        expand=True,
        padding=10

    )
    
    

    page.add(nome, slogan, instrucao, posicionador)

ft.run(main)