AUTHOR = 'La Crida'
SITENAME = 'Crida Premià de Dalt'
SITEURL = ''

THEME = 'themes/pelican-hss'

PATH = 'content'

TIMEZONE = 'Europe/Rome'

DEFAULT_LANG = 'ca_ES'

ARTICLE_URL = ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}.html'

DEFAULT_CATEGORY = 'misc'

STATIC_PATHS = [
    'extra',  # this
]

# Header links
LINKS = (
    ('Inici', '/', ''),
    ('Tags', '/tags', ''),
    ('Categories', '/categories', ''),
    ('Contacte', '/contacte', ''),
    ('Programa', '/programa', ''),
    ('Arxiu', SITEURL + '/archives.html', ''),
       )

# Social links
SOCIAL = (('twitter', 'https://twitter.com/cridapremiadalt', '@cridapremiadalt'),
          ('facebook', 'https://www.facebook.com/cridapremiadedalt', 'Crida Premià de Dalt'),
          ('youtube', 'https://www.youtube.com/channel/UCMQkonVf7Swo3icVW0uuwSg', 'Crida Premià de Dalt'),
          ('instagram', 'https://www.instagram.com/crida.pdd', '@crida.pdd'),
          ('email', 'mailto:cridapremiadedalt@gmail.com?subject=Contacte%20Crida%20Premi%C3%A0%20de%20Dalt&body=-', 'cridapremiadedalt@gmail.com'))


DEFAULT_PAGINATION = 5

DISPLAY_CATEGORIES = False

DIRECT_TEMPLATES = ['index', 'categories', 'tags', 'authors', 'archives',
                    'author', 'category', 'tag',
                    'contacte', 'programa', 'codi-etic',
                    ]

EXTRA_PATH_METADATA = {'extra/favicon.ico': {'path': 'favicon.ico'}}