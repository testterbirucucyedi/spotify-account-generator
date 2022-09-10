<p align="center">
  <img src="https://user-images.githubusercontent.com/70216275/188632356-ed00e1e7-0734-469f-9915-2d0559643f1c.gif">
</p>

<p align="center">
  Spotify Account Generator is an educational application written in Python.
</p>

## Description

*This Python3 script instantly generates new free Spotify accounts (with random credentials) while pretending to be a Spotify app (currently v8.6.26) installed on an Android device. This is simply achieved by sending forged HTTP requests. The original requests have been intercepted from an emulator of a SM-N976N device running Android Lollipop, that is why you will find this particular model in the "User-Agent" header of the requests.*

## Disclaimer

|Spotify Account Generator was made for Educational purposes|
|-------------------------------------------------|
By using any of the files available in this repository, you understand that you are agreeing to use at your own risk.
All files available here are for education and/or research only.

## How To Install

#### Requirements
```
$ pip install requests
```

#### Installation (Manual installation)
```
$ git clone https://github.com/selim1337/spotify-account-generator
$ cd spotify-account-generator
$ python spotify_generator.py
```
## How to use
```
* Simply run it without arguments to generate one account and print its credentials to the console
$ python spotify_generator.py
```
![Example](https://user-images.githubusercontent.com/70216275/189494184-b77b8168-4e46-453a-bf03-6697948e85f1.PNG)
```
* You can also specify the amount of accounts to generate and a file where their credentials will be saved.
$ python spotify_generator.py -n AMOUNT -o OUTPUT_FILE
```
![Example - 2](https://user-images.githubusercontent.com/70216275/189494253-8fc11d9a-761d-405a-9ab1-2a3f7a5209fa.PNG)
|Amount|Output File|
|-------|----------|
|Account amount to be created|File to save accounts|

**The creadentials will be printed/saved in the following format:**
- NICKNAME:USERNAME:EMAIL:PASSWORD

## Additional Informations
- If you find any malfunction, contact me on Discord: selim#1337

## Example
![image](https://user-images.githubusercontent.com/70216275/189494325-ce3fa3c4-af6c-4a26-a5ec-8ca302ab71d2.png)



## Source

> *https://github.com/davide-acanfora/spotify-account-generator*

