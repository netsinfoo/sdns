from extras.plugins import PluginMenuButton, PluginMenuItem
from utilities.choices import ButtonColorChoices


menu_items = (
    PluginMenuItem(
        link='plugins:sdns:register_list',
        link_text='Registers',
        permissions=['sdns.view_register'],
        buttons=(
            PluginMenuButton(
                link='plugins:sdns:register_add',
                title='Add a new register',
                icon_class='fa fa-plus',
                color=ButtonColorChoices.GREEN,
                permissions=['sdns.add_register']
            ),
        )
    ),
    PluginMenuItem(
        link='plugins:sdns:register_list',
        link_text='Add a new register 2',
        permissions=['sdns.view_register'],
        buttons=(
            PluginMenuButton(
                link='plugins:sdns:register_add',
                title='Assign a register 2',
                icon_class='fa fa-plus',
                color=ButtonColorChoices.GREEN,
                permissions=['sdns.add_register']
            ),
        )
    ),
)