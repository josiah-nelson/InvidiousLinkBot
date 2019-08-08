# InvidiousLinkBot

This is a Reddit bot that uses PRAW and the Reddit API to convert youtube video links on the subreddit r/Privacy to invidio.us links. The idea came from u/CryoxicOCE on [this thread](https://www.reddit.com/r/privacy/comments/cnbcow/in_the_movie_snowden_phones_are_put_in_microwaves)


The bot simply scans all new comments on the subreddit for "youtube.com" or "youtu.be" and if they are found, it sppends the path to "insidio.us" and makes a comment saying:

```"Hey, I noticed you linked a YouTube video in your comment. For privacy, here are your links converted to invidio.us: 

link
link

I am a bot. This comment was performed automatically."```
