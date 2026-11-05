import flet as ft

from Components.buttons import custom_button
from Components.navigation import bottom_navigation


def account_screen(page):

    def logout(e):
        page.route = "/login"
        page.on_route_change(e)

    return ft.View(
        route="/account",
        controls=[
            ft.Column(
                controls=[
                    ft.Text(
                        "My Account",
                        size=25,
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.GREEN
                    ),

                    ft.CircleAvatar(
                        content=ft.Icon(
                            ft.Icons.PERSON,
                            size=40
                        ),
                        bgcolor=ft.Colors.GREEN,
                        radius=40
                    ),

                    ft.Text(
                        "Maryam",
                        size=20,
                        weight=ft.FontWeight.BOLD
                    ),

                    ft.Text("08000000000"),

                    ft.Divider(),

                    ft.ListTile(
                        leading=ft.Icon(ft.Icons.PERSON_OUTLINE),
                        title=ft.Text("Personal Information")
                    ),

                    ft.ListTile(
                        leading=ft.Icon(ft.Icons.SECURITY),
                        title=ft.Text("Security")
                    ),

                    ft.ListTile(
                        leading=ft.Icon(ft.Icons.SETTINGS),
                        title=ft.Text("Settings")
                    ),

                    ft.ListTile(
                        leading=ft.Icon(ft.Icons.HELP_OUTLINE),
                        title=ft.Text("Help and Support")
                    ),

                    custom_button(
                        "Logout",
                        logout
                    ),

                    bottom_navigation(page)
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=15
            )
        ]
    )