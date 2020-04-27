![Spam Messager](banner.png)
Spam Messager can be used to rapidly send messages word by word.
This can be very annoying to the recipients yet provide lots of fun to the sender.

## Description
The program offers two options: sending a typed out message or using a .txt file. The user must choose using a number. This is checked using a function called isInt. That function is very useful and I encourage you to keep its source file, isInt.py, for your own projects. 

Once the user has input their message, the script does a countdown. This countdown depends on the OS command "say". I haven't tested this on anything other than macOS so you may want to comment out the os.say portions of the code. It shouldn't affect anything else. Just leave the time.sleep in there to make sure you have an apt amount of time to switch the focus over to your messaging app.

I tested this out with iMessage for Mac but it should work with any messaging app that uses ENTER as a means of sending a typed message.

If you find any issues with this program, I encourage you to contact me or try to fix the error and pull request.

### Dependencies
You will need tkinter to run this, or you can get rid of the file input code. Installing tkinter can vary based on the operating system. For macOS, I installed it with Homebrew, "tk-tcl".

PyAutoGUI is also very necessary for this program! You can install it with pip.
> `pip install pyautogui`


---
If you have any questions or concerns, you can contact me by email at [dakint@icloud.com](mailto:dakint@icloud.com).

You can come back to this repo with the URL: https://tylerdakin.com/SpamMessager

#### Usage Rights
© 2020 Tyler Dakin

This work is licensed under the [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/). 
[![CC-BY License](https://i.creativecommons.org/l/by/4.0/88x31.png)](https://creativecommons.org/licenses/by/4.0/)