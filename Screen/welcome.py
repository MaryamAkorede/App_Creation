import flet as ft

from Components.buttons import custom_button


def welcome_screen(page):

    def get_started(e):
        page.route = "/register"
        page.on_route_change(None)

    return ft.View(
        route="/",
        controls=[
            ft.Column(
                controls=[
                    ft.Text(
                        "Welcome to OPay",
                        size=25,
                        weight=ft.FontWeight.BOLD,
                        text_align=ft.TextAlign.CENTER
                    ),

                    custom_button(
                        "Get Started",
                        get_started
                    )
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.MainAxisAlignment.CENTER,
                expand=True,
                spacing=20
            )
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        vertical_alignment=ft.MainAxisAlignment.CENTER
    )