# autoYT
Updated README coming soon.
```
usage: autoyt [-h] [-d [N]] [-c N] [-l] [-a CHANNELS [CHANNELS ...]] [-r CHANNELS [CHANNELS ...]] [-x] [-s SEARCH] [-S SEARCHCHANNEL] [-e] [-u REMOVEFROMCHANNEL] [--removeall] [--removeempty] [--removevideos N] [--removeallvideos] [--removeinvalid] [--configdir] [--find CHANNEL]

Python script for quickly searching and downloading new content out of YouTube.

options:
  -h, --help            show this help message and exit
  -d [N], --download [N]
                        Download saved channels(download up to N(default 5) last videos)
  -c N, --cap N         Limit actions to N items
  -l, --list            List saved channels
  -a CHANNELS [CHANNELS ...], --add CHANNELS [CHANNELS ...]
                        Save channels
  -r CHANNELS [CHANNELS ...], --remove CHANNELS [CHANNELS ...]
                        Remove channels
  -x, --export          Export saved channels
  -s SEARCH, --search SEARCH
                        Search for YouTube videos
  -S SEARCHCHANNEL, --searchchannel SEARCHCHANNEL
                        Search for YouTube channel videos
  -e, --endless         Starts endless mode
  -u REMOVEFROMCHANNEL, --removefromchannel REMOVEFROMCHANNEL
                        Removes all videos from a specified channel
  --removeall           Removes all saved channels
  --removeempty         Removes empty directories
  --removevideos N      Removes videos older than N days
  --removeallvideos     Remove all saved videos
  --removeinvalid       Removes all saved videos which don't have a saved channel
  --configdir           Prints configuration file path
  --find CHANNEL        Finds all downloaded videos from a specified channel
  ```
