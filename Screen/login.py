import flet as ft

from Components.buttons import custom_button
from Components.textfields import custom_textfield


def login_screen(page):

    def navigate(route):
        page.route = route
        page.on_route_change(None)

    return ft.View(
        route="/login",
        controls=[
            ft.Column(
                controls=[
                    ft.Text(
                        "Sign In",
                        size=28,
                        weight=ft.FontWeight.BOLD
                    ),

                    ft.Text("Welcome back!"),

                    custom_textfield(
                        "Phone Number",
                        "Enter phone number"
                    ),

                    custom_textfield(
                        "Password",
                        "Enter password"
                    ),

                    ft.Checkbox(
                        label="Remember Password"
                    ),

                    custom_button(
                        "Sign In",
                        lambda e: navigate("/home")
                    ),

                    ft.TextButton(
                        "Create an account",
                        on_click=lambda e: navigate("/register")
                    ),

                    ft.TextButton(
                        "Back to Welcome",
                        on_click=lambda e: navigate("/")
                    )
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=18
            )
        ],
        scroll=ft.ScrollMode.AUTO
    )