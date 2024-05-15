AUTHOR = 'Thomas Stucky'
SITENAME = 'AstroStucky'
SITEURL = ""

PATH = "content"
STATIC_PATHS = ['images']

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

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)
GITHUB_URL = "https://github.com/AstroStucky"

# Appearance
DEFAULT_PAGINATION = False
THEME = "graymill"
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
    "+implicit_figures",
]
