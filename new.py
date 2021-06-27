import random
from instapy import InstaPy
from instapy import smart_run

# login credentials
insta_username = 'humouretdelire'
insta_password = 'note2345'

like_tag_list = ['humour', 'france', 'humourofficial', 'humourfrancais']

# get a session!
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=True)

with smart_run(session):
    # settings
    session.set_relationship_bounds(enabled=True,
                                    max_followers=15000)

    session.set_user_interact(amount=2, randomize=True, percentage=60)
    session.set_do_follow(enabled=True, percentage=40)
    session.set_do_like(enabled=True, percentage=80)

    # activity
    session.like_by_tags(random.sample(like_tag_list, 3),
                         amount=random.randint(50, 100), interact=True)



    """ Joining Engagement Pods...
    """
    photo_comments = ['Nice shot! @{}',
        'I love your profile! @{}',
        'Wonderful :thumbsup:',
        'Just incredible :open_mouth:',
        'What camera did you use @{}?',
        'Love your posts @{}',
        'Looks awesome @{}',
        'Getting inspired by you @{}',
        ':raised_hands: Yes!',
        'I can feel your passion @{} :muscle:']

    session.set_do_comment(enabled = False, percentage = 95)
    session.set_comments(photo_comments, media = 'Photo')
    session.join_pods(topic='travel')