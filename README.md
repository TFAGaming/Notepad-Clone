# Notepad-Clone v1.0.0
This is not a 100% clone, but a similar one! This all made in Python and can be turned into an executable file (.exe) using [pyinstaller](https://pyinstaller.org/en/stable/)!

# Updates:
1. Added scrollbar.<br>
2. Sets automatically the default font of editor in "Set font" Top level app.<br>
3. Webbrowser support.

## Preview
Main: <br>
![2023-01-08 12_23_57-Window](https://user-images.githubusercontent.com/92172698/211193486-efe5f778-6440-42b5-bdc0-6c9fc161b98d.png)

Set font: <br>
![2023-01-07 20_58_20- Noname  - MyNoteBook](https://user-images.githubusercontent.com/92172698/211168349-af1b5177-873e-4fcc-85c1-5e41570f5186.png)

## Change icon
Create firstly or download an image with .png or .jpeg extension, visit a site that converts .png or .jpeg to **.ico**. Here is the site that I used to convert my image: [Convertico](https://convertico.com/).

## Turn the project into .exe
Install **pyinstaller** using command prompt:

```shell
pip install pyinstaller
```

Use **cd** command to navigate into the folder that your project contain the program file, which is **main.py**.<br>
Then, use the command below to turn the **main.py** to an executable file:

```shell
pyinstaller --onefile --icon=icon.ico main.py
```

If you see some folders that has been created automatically, congrats! Go to **dist** folder, drag the .exe file into the folder where it can read the icon. You can delete the **dist** folder and other folders that were created.

Enjoy! :)

## Credits:
All credits to T.F.A#7524.
