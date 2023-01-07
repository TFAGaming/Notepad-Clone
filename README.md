# Notepad-Clone v1.0.0
This is not a 100% clone, but a similar one! This all made in Python and can be turned into an executable file (.exe) using [pyinstaller](https://pyinstaller.org/en/stable/)!

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
pyinstaller --onefile main.py
```

If you see some folders that has been created automatically, congrats! Go to **dist** folder, drag the .exe file into the folder where it can read the icon.

> If you want to set the icon into the .exe file, use then:
> ```shell
> pyinstaller --onefile --icon=icon.ico main.py
> ```

Enjoy! :)

## Credits:
All credits to T.F.A#7524. If I see any copies without my credits will be taken down by me.
