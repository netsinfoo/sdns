from extras.plugins import PluginMenuButton, PluginMenuItem
from utilities.choices import ButtonColorChoices

menu_items = (
    PluginMenuItem(
        link='plugins:sdns:register_list',
        link_text='Registers',
        permissions=[],
        buttons=(
            PluginMenuButton(
                link='plugins:sdns:register_add',
                title='Add a new register',
                icon_class='fa fa-plus',
            ),
            PluginMenuButton(
                link='admin:sdns',
                title='Add a new animal',
                icon_class='fa fa-plus',
                color=ButtonColorChoices.GREEN,
                permissions=['sdns.add_register']
            ),
        )
    ),
)