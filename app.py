from flet import *


def main(page: Page):
    page.padding = 0
    page.add(
        Container(
            alignment=alignment.center,
            expand=True,
            bgcolor="blue",
            content=Text(
                'Welcome to the ControlKAF website',
                size=35
            )
        )
    )


app(target=main)
