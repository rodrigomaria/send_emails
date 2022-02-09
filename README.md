# Send E-mail using HTML and CSS

This project use Python version 3 and works using STMP by Gmail. If it causes error return `smtplib.SMTPAuthenticationError: (535, b'5.7.8 Username and Password not accepted.`, this [link](https://www.google.com/settings/security/lesssecureapps) can helps you.

## Instructions:
1. Install virtual env
```bash
$ pip install virtualenv
```

2. Create virtual environment
```bash
$ virtualenv -p python3 send_email
```

3. Activate virtual environment in MacOS or Linux
```bash
$ source send_email/bin/activate
```

4. When or if necessary, deactivate the virtual enviroment
```bash
$ deactivate
```

After the virtual environment created and activated, change your informations in `constants.py` file and run the command `python send_email.py` to send an e-mail.