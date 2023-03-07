# EzMusic v1.0.0
A MacOS spotify clone for youtube videos.

## Requirements
- MacOS Sierra (10.12+)
- Requirements.txt
- Xcode CLT
```
pip(3) install -r requirements.txt
xcode-select --install
```

## Installation & Usage
Download and run the installer file to get started.\
\
You can launch the app by typing `ezmusic` into a terminal.

## Roadmap
- Support for Windows and Linux systems
- Rewriting garbled code for efficiency
- Less packages required

## Info
- Project maintained by `ebots#6157`([Discord](https://discord.com/app/))
- License: [MIT](https://choosealicense.com/licenses/mit/)

## Credits
### Playing sound with NSSound
  - [Constructing a delegate for NSSound](https://stackoverflow.com/a/69981505/)
  - [Building the player (Borrowed a bit of code)](https://pypi.org/project/audioplayer/)

### Accessing MPNowPlayingInfoCenter utilising PyObjC
  - [Building basic information and icon](https://stackoverflow.com/questions/69965175/pyobjc-accessing-mpnowplayinginfocenter)
  - [Clearing up information and mislead data](https://py4u.org/questions/69965175/)

This would not be possible without these answers because I cannot be asked to read the apple developer docs
