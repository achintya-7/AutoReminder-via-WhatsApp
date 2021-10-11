# AutoReminder-via-WhatsApp

# How to setup Appwrite?
Follow this link: https://appwrite.io/

# How to setup Twilio 
Follow this link: https://www.twilio.com/whatsapp/pricing/us

# 📁 Automatic Reminder via WhatsApp
A sample Python Cloud Function that leverages Twilio to send reminder messages to all the recipients in a database made using Appwrite.

## 📝 Environment Variables
Add the following environment variables in your Cloud Function settings.

* **APPWRITE_API_KEY** - Create a key from the Appwrite console with the following scope (`files.read`. `documents.read`. `collections.read`)
* **APPWRITE_ENDPOINT** - Your Appwrite Endpoint
* **ACCOUNT_SID** - Twilio account SID
* **AUTH_TOKEN** - Twilio API  key
* **COLLECTION_ID** - Your collection ID for which you want the .csv file to be created

## 🛠 Building and Packaging

To package this example as a cloud function, follow these steps.

```bash
$ cd PATH/WHERE/YOU/DOWNLOADED/THE/REPO/Appwrite-Backup-to-Dropbox  
$ PIP_TARGET=./.appwrite pip install -r ./requirements.txt --upgrade --ignore-installed
```

* Ensure that your folder structure looks like this 
```
.
├── .appwrite/
├── main.py
└── requirements.txt
```

* Create a tarfile

```bash
$ cd ..
$ tar -zcvf code.tar.gz collection-backup
```

* Upload the tarfile to your Appwrite Console and use the following entrypoint command

```bash
python main.py
```

## 🎯 Trigger

Head over to your function in the Appwrite console and just press the excecute button.
Also you can CRON format in the swttings to send it automatically. 
