from instapy import InstaPy
from instapy import smart_run

insta_username = 'humouretdelire'
insta_password= 'note2345'

session=InstaPy(username=insta_username,
				password=insta_password,
                  headless_browser=True,
                  split_db=True,
                  multi_logs=True)

with smart_run(session):
	session.set_relationship_bounds(enabled=True,
			    potency_ratio=None,
			    delimit_by_numbers=True,
			    max_followers=6000,
				max_following=3000,
				min_followers=30,
				min_following=30)
	session.set_do_like(enabled=True, percentage=100)
	session.set_do_comment(enabled=False, percentage=0)
	session.set_do_follow(enabled=False, percentage=0, times=1)
	session.set_user_interact(amount=1, randomize=True, percentage=35, media='Photo')
	session.follow_user_followers(['xyz'], amount=amount_number, randomize=False, interact=True, sleep_delay=300)