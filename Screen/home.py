import flet as ft

from Components.cards import service_card
from Components.navigation import bottom_navigation


def home_screen(page):

    return ft.View(
        route="/home",
        bgcolor=ft.Colors.WHITE,
        controls=[
            ft.Column(
                controls=[

                    # Main scrollable content
                    ft.Column(
                        controls=[

                            # Top bar
                            ft.Row(
                                controls=[
                                    ft.Text(
                                        "OPay",
                                        size=28,
                                        weight=ft.FontWeight.BOLD,
                                        color=ft.Colors.GREEN
                                    ),

                                    ft.Icon(
                                        ft.Icons.NOTIFICATIONS_OUTLINED,
                                        color=ft.Colors.BLACK,
                                        size=25
                                    )
                                ],
                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                            ),

                            # Wallet balance card
                            ft.Container(
                                padding=20,
                                bgcolor=ft.Colors.GREEN,
                                border_radius=15,
                                content=ft.Column(
                                    controls=[
                                        ft.Text(
                                            "Available Balance",
                                            color=ft.Colors.WHITE,
                                            size=15
                                        ),

                                        ft.Text(
                                            "₦25,000.00",
                                            size=28,
                                            weight=ft.FontWeight.BOLD,
                                            color=ft.Colors.WHITE
                                        ),

                                        ft.Row(
                                            controls=[
                                                ft.Text(
                                                    "Wallet Balance",
                                                    color=ft.Colors.WHITE,
                                                    size=12
                                                ),

                                                ft.Button(
                                                    "Add Money",
                                                    bgcolor=ft.Colors.WHITE,
                                                    color=ft.Colors.GREEN
                                                )
                                            ],
                                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                                        )
                                    ],
                                    spacing=12
                                )
                            ),

                            # Services heading
                            ft.Text(
                                "Quick Services",
                                size=20,
                                weight=ft.FontWeight.BOLD
                            ),

                            # First row of services
                            ft.Row(
                                controls=[
                                    service_card(
                                        "Transfer",
                                        ft.Icons.SEND
                                    ),

                                    service_card(
                                        "Airtime",
                                        ft.Icons.PHONE_ANDROID
                                    ),

                                    service_card(
                                        "Data",
                                        ft.Icons.WIFI
                                    )
                                ],
                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                            ),

                            # Second row of services
                            ft.Row(
                                controls=[
                                    service_card(
                                        "Bills",
                                        ft.Icons.RECEIPT
                                    ),

                                    service_card(
                                        "Shopping",
                                        ft.Icons.SHOPPING_BAG
                                    ),

                                    service_card(
                                        "More",
                                        ft.Icons.GRID_VIEW
                                    )
                                ],
                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                            ),

                            # Recent transactions
                            ft.Text(
                                "Recent Transactions",
                                size=20,
                                weight=ft.FontWeight.BOLD
                            ),

                            ft.Container(
                                padding=20,
                                bgcolor=ft.Colors.GREY_100,
                                border_radius=12,
                                content=ft.Column(
                                    controls=[
                                        ft.Icon(
                                            ft.Icons.RECEIPT_LONG,
                                            size=35,
                                            color=ft.Colors.GREY
                                        ),

                                        ft.Text(
                                            "No transactions yet.",
                                            color=ft.Colors.GREY_700
                                        )
                                    ],
                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                    spacing=10
                                )
                            )

                        ],
                        spacing=20,
                        scroll=ft.ScrollMode.AUTO,
                        expand=True
                    ),

                    # Bottom navigation
                    bottom_navigation(page)

                ],
                spacing=10,
                expand=True
            )
        ]
    )