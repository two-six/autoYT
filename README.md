# autoYT

autoYT is a Python program designed to automate the process of watching videos out of YouTube, without using YouTube. It's functions include searching YouTube for videos, searching channels for a new videos, but also to download, delete and group videos into folders based on their upload date both automatically and manually.

# Usage
To search for a video, use the `-s` or `--search` argument.

To search for new videos on a channel, use `-S` or `--searchchannel` argument.

You can use `-c` or `--cap` argument with both of the above arguments to limit the number of results.
## example:
```
$ autoyt -S "nocopyrightsounds" -c 5
Channel Name: NoCopyrightSounds
Channel Link: https://youtube.com/channel/UC_aEa8K-EOJ3D6gOs7HcyNg
-------------------------------------------

Title: ASHWOOD - Maria (ft. Blooom & Ghost’n’Ghost) [NCS Release]
Link: https://www.youtube.com/watch?v=FsnluXPC6s0
Upload Date: 2023-06-22
-------------------------------------------

Title: jeonghyeon & Noisy Choice - Too Far [NCS Release]
Link: https://www.youtube.com/watch?v=kI4usARVdaU
Upload Date: 2023-06-20
-------------------------------------------

Title: Daniel Levi - Clown Around [NCS Release]
Link: https://www.youtube.com/watch?v=iPyg-QknNeY
Upload Date: 2023-06-17
-------------------------------------------

Title: Coopex, Afterfab, Heleen - EX [NCS Release]
Link: https://www.youtube.com/watch?v=rpPiFMcjF6M
Upload Date: 2023-06-16
-------------------------------------------

Title: Anyone remember these? #nocopyrightsounds #ncs #music #nostalgia #childhoodmemories
Link: https://www.youtube.com/watch?v=kC8LvAqhPtE
Upload Date: 2023-06-15
-------------------------------------------
```

To add a channel to cache use `-a` or `--add` argument with a channel's ID or channel's name after. You can also add multiple channels at once.

In the same way you can remove channels from cache using `-r` or `--remove` argument with a channel's ID or channel's name after.

To list added channels use `-l` or `--list` argument.
## example
```
$ autoyt -a "nocopyrightsounds" "UCsBjURrPoezykLs9EqgamOA"
$ autoyt -l
Name: NoCopyrightSounds
Link: https://www.youtube.com/channel/UC_aEa8K-EOJ3D6gOs7HcyNg
Channel ID: UC_aEa8K-EOJ3D6gOs7HcyNg
-------------------------------------------

Name: Fireship
Link: https://www.youtube.com/channel/UCsBjURrPoezykLs9EqgamOA
Channel ID: UCsBjURrPoezykLs9EqgamOA
-------------------------------------------


$ autoyt -r "UC_aEa8K-EOJ3D6gOs7HcyNg"
$ autoyt -l
Name: Fireship
Link: https://www.youtube.com/channel/UCsBjURrPoezykLs9EqgamOA
Channel ID: UCsBjURrPoezykLs9EqgamOA
-------------------------------------------
```
You can download videos from the saved channels using `-d` or `--download` argument. You can supply this argument with the number of days - this indicates how old videos are allowed to be downloaded.

In a similar way you can use a ``--removevideos` argument with the number N of days after it. It'll delete all videos older than N days.

You can also use `--find` argument with a channel's name after it. It will list location of all of the downloaded videos from a selected channel

## example
```
$ autoyt -d 5
2023_06_21/Fireship/PHP will make you poor StackOverflow 2023 Results: Downloading...
2023_06_20/Fireship/SST in 100 seconds: Downloading...
2023_06_16/Fireship/RIP Google Domains… and 5 big tech stories this week: Downloading...
2023_06_13/Fireship/Nuxt in 100 Seconds: Downloading...
2023_06_12/Fireship/Reddit’s API rug pull: Downloading...
$ autoyt --find fireship
./videos/2023_06_12/Fireship/Reddit’s API rug pull.webm
./videos/2023_06_13/Fireship/Nuxt in 100 Seconds.webm
./videos/2023_06_16/Fireship/RIP Google Domains… and 5 big tech stories this week.webm
./videos/2023_06_20/Fireship/SST in 100 seconds.webm
./videos/2023_06_21/Fireship/PHP will make you poor StackOverflow 2023 Results.webm   

$ autoyt --removevideos 3
$ autoyt --find fireship 
./videos/2023_06_21/Fireship/PHP will make you poor StackOverflow 2023 Results.webm
```

And finally you can use an `endless` mode - `-e`. It'll download and remove videos automatically by running in a loop. It takes all of it's arguments from the config file.

You can do more using autoYT. To list all of the available options use `-h` argument - `autoyt -h`

# Config

Config is stored in the `autoYT/src/config/config.toml` file(soon to change). Configuration contains all of the preferences regarding the usage of this program.
## Sample `config.toml`
```toml
# The directory where program will put all of the downloaded videos.
download_dir = "./videos"
# The directory where program will put the cache file with all of the saved channels
cache_dir = "./cache"
# The quality used to download all of the videos(see yt-dlp -f option)
quality = "ba+bv[height<=?1080]"
# Describes how old downloaded videos can be(in days). 0 means no limit.
max_video_age = 0
# How many videos are allowed to be downloaded from a channel. 0 means no limit.
max_downloaded_channel_videos = 0
# Automatically delete videos older than this number of days(endless mode). 0 means never.
delete_videos_age = 0 
# Wait this many seconds before checking channels for new videos again(endless mode).
channels_check_break = 0

# ID of a channel
[UC_aEa8K-EOJ3D6gOs7HcyNg]
# Quality setting just for this channel
quality = "x"
```