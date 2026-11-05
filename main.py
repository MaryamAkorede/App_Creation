import flet as ft

from Screen.welcome import welcome_screen
from Screen.register import register_screen
from Screen.login import login_screen
from Screen.home import home_screen
from Screen.account import account_screen


def main(page: ft.Page):

    page.title = "OPay"
    page.theme_mode = ft.ThemeMode.LIGHT

    def route_change(e=None):

        page.views.clear()

        if page.route == "/":
            page.views.append(welcome_screen(page))

        elif page.route == "/register":
            page.views.append(register_screen(page))

        elif page.route == "/login":
            page.views.append(login_screen(page))

        elif page.route == "/home":
            page.views.append(home_screen(page))

        elif page.route == "/account":
            page.views.append(account_screen(page))

        page.update()

    page.on_route_change = route_change

    page.route = "/"
    route_change()


ft.run(main)