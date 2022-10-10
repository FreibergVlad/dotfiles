"""
Group definitions are here
"""
from libqtile.config import Group

group_definitions = [
    {
        'name': 'web',
        'label': '',
    },
    {
        'name': 'terminal',
        'label': '',
    },
    {
        'name': 'messaging',
        'label': '',
    },
    {
        'name': 'music',
        'label': 'ﱘ',
    },
]

groups = [Group(**group) for group in group_definitions]
