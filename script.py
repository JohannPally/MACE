import praw

reddit = praw.Reddit(
    user_agent = "Reddit: MACE:1.0 (by u/<uwukungfuwu>)",
    client_id = "d-7c-MSgBBHA0Mirq5Z3cw",
    client_secret = "EZzaLo5N0p-jmXJYdSF74j7Z7er1VQ",
    username = "mace_user_account",
    password = "macebot123"
)

title = "Test Post"
body = "This is a test post for MACE"
reddit.subreddit('antisocialcs_UIUC').submit(title=title, selftext=body)