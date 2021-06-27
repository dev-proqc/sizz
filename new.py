import settings
from instapy import InstaPy

session = InstaPy(username=humouretdelire, password=note2345, headless_browser=True)
session.login()

session.set_do_follow(enabled=True, percentage=70, times=5)
session.set_user_interact(amount=3, randomize=True, percentage=70, media='Photo')
session.like_by_tags(['humour'], amount=40, interact=True)