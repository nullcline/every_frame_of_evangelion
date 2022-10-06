
# Every Evangelion Frame In Order

(note: this was the first python project i ever did please do not judge me)

![image](https://user-images.githubusercontent.com/48143035/194214868-916de132-27c0-4e6c-92cf-c65862e48ea0.png)

This project consists of two python scripts that:
  1. Samples a video and saves it into individual frames
  2. Posts the frames to facebook
  
# Sampling
Sampling is done in order to not take an eternity to finish posting. Facebook ~~cucks~~ rate limits us to post every 5 minutes, which means a 24fps, 23 minute video would span 33120 frames, and take around 115 days to post. This was unacceptable as I did not think mankind would last long enough to see the end, so I opted to cut it at 6fps, with the added optimization of including side-by-side frames when a large MSE was detected.

# Posting
Posting is unoptimal as i made the genius design decision to save individual videos instead of cutting a video live. This would have saved on disk space, but harddrives are cheap. To post to Facebook the Facebook Graph API is used. Their tokens are so cringe, but following https://docs.squiz.net/funnelback/docs/latest/build/data-sources/facebook/facebook-page-access-token.html makes it pretty easy to manage.

# Automation
Automation for this project is done entirely through crontab.

*Inspiration credit goes to the botmin of [Every SpongeBob Frame In Order](https://www.facebook.com/EverySpongeInOrder)*
