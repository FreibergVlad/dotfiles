"""
Group definitions are here
"""
from libqtile.config import Group, Match

group_definitions = [
    {
        'name': 'web',
        'label': '󰈹',
        'matches': [Match(wm_class='firefox')],
        'layout': 'max'
    },
    {
        'name': 'dev',
        'label': '',
        'layout': 'columns'
    },
    {
        'name': 'ms-teams',
        'label': '',
        'matches': [Match(wm_class='teams-for-linux')],
        'layout': 'max'
    },
    {
        'name': 'telegram',
        'label': '',
        'matches': [Match(wm_class='telegram-desktop')],
        'layout': 'max'
    },
    {
        'name': 'spotify',
        'label': '',
        'matches': [Match(wm_class='Spotify')],
        'layout': 'max'
    },
    {
        'name': 'miscellaneous',
        'label': '󱗼',
        'layout': 'floating'
    },
]

groups = [Group(**group) for group in group_definitions]
