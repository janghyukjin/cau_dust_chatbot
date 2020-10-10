# cau_dust_chatbot


공공 api를 활용하여 중앙대학교 미세먼지 농도를 크롤링 후, 사용자에게 메시지 창을 띄워줍니다. <br>
aws ec2에 배포 후 중앙대학교 학생들을 대상으로 운영하고 있습니다.

# Kakao Chatbot main page
<img width="549" alt="Screen Shot 2020-10-11 at 12 05 05 AM" src="https://user-images.githubusercontent.com/38303729/95658465-91badb80-0b55-11eb-8ea2-5ade58af6f83.png">

cau_dust_chatbot Server installation

====================================

We also support Windows OS, but we recommend Ubuntu OS.

Set up python
----------------------------------
********************************

    To set up python: http://www.python.org
    $ sudo apt-get install python3


How to install
--------------------------------
**************************

    $ git clone https://github.com/janghyukjin/cau_dust_chatbot.git
    $ cd cau_dust_chatbot
        
    ## Please create a virtual environment and install Python package. ##
    
    $ virtualenv -p python3 myvenv
    $ . myvenv/bin/activate
    $ pip install -r requirements.txt
    
How to run in local
--------------------------------
***************************

    $ cd cau_dust_chatbot/cau_dust_chatbot
    $ python manage.py runserver
    
Contribute
----------------
* Issue Tracker: https://github.com/janghyukjin/cau_dust_chatbot/issues
* Source Code: https://github.com/janghyukjin/cau_dust_chatbot

Contribution guidelines
-----------------------
If you want to contribute to HML, be sure to review the [contribution guideline](https://github.com/janghyukjin/cau_dust_chatbot). This project adheres to HML's code of conduct. By participating, you are expected to uphold this code.

We use GitHub issues for tracking requests and bugs.

License
------------------------
MIT license
