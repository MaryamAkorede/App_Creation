import flet as ft

from Components.buttons import custom_button
from Components.textfields import custom_textfield


def register_screen(page):

    def navigate(route):
        page.route = route
        page.on_route_change(None)

    return ft.View(
        route="/register",
        controls=[
            ft.Column(
                controls=[
                    ft.Text(
                        "Welcome to OPay",
                        size=25,
                        weight=ft.FontWeight.BOLD
                    ),

                    ft.Text(
                        "Create your account",
                        size=20,
                        weight=ft.FontWeight.BOLD
                    ),

                    custom_textfield(
                        "Phone Number",
                        "Enter your phone number"
                    ),

                    custom_textfield(
                        "Password",
                        "Enter your password"
                    ),

                    custom_button(
                        "Continue",
                        lambda e: navigate("/home")
                    ),

                    ft.TextButton(
                        "Already have an account? Sign in",
                        on_click=lambda e: navigate("/login")
                    ),

                    ft.TextButton(
                        "Back",
                        on_click=lambda e: navigate("/")
                    )
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20,
            )
        ],
        scroll=ft.ScrollMode.AUTO
    )