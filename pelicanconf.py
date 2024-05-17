AUTHOR = 'Thomas Stucky'
SITENAME = 'AstroStucky'
SITEURL = ""

PATH = "content"
STATIC_PATHS = ['images', 'documents']

TIMEZONE = 'America/Denver'

DEFAULT_LANG = 'en'

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Links
GITHUB_URL = "http://github.com/AstroStucky"

LINKS_WIDGET_NAME = "LINKS"
LINKS = [
    ("Resume/CV", "/documents/ThomasStucky_resume.pdf"),
    ("GitHub", GITHUB_URL),
    ("Mastodon", "http://mastodon.gamedev.place/@starry"),
    ("Itch.io", "http://starrynitegames.itch.io/"),
    ("LinkedIn", "http://linkedin.com/in/astrostucky/")
]
MENUITEMS = [
  ('Blog','/')
]

## TODO: add Mastodon icon to Graymill theme
# Social widget
# SOCIAL_WIDTH_NAME = "TEST"
# SOCIAL = [
#     ("LinkedIn", "http://linkedin.com/in/astrostucky/"),
#     # ,
#     # ("GitHub", "github.com/AstroStucky")
# ]

# Appearance
DEFAULT_PAGINATION = False
DISPLAY_CATEGORIES_ON_MENU = False
THEME = "./graymill"
## TODO: try true sometime
TYPOGRIFY = False

# Enable Pandoc
# Arguments passed into pandoc
PANDOC_ARGS = [
    "--mathjax"
]

# Non-Pandoc Extensions that are not enabled by default in pandoc
#   https://pandoc.org/MANUAL.html#non-pandoc-extensions
PANDOC_EXTENSIONS = [
    # "+backtick_code_blocks",
    "+implicit_figures"
]

## TODO: Experiment with making a page the home page instead of blog
# SITEURL = '/blog'
# OUTPUT_PATH = 'output/blog'
# PAGE_URL = '../{slug}.html'
# PAGE_SAVE_AS = '../{slug}.html'
# DISPLAY_PAGES_ON_MENU = False
# DISPLAY_CATEGORIES_ON_MENU = False
# MENUITEMS = [('Home', '/'), ('Blog', '/blog/')]

# DELETE_OUTPUT_DIRECTORY = True
