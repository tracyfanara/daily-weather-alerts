import requests
import smtplib
from email.message import EmailMessage
from datetime import date

EMAIL_SENDER = os.getenv("EMAIL_SENDER")
EMAIL_RECEIVER = os.getenv("EMAIL_RECEIVER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

def download_maps(MAPS):
files = []
for label, url in MAPS.items():
try:
r = requests.get(url, timeout=15)
if r.status_code == 200:
filename = f"{label}.gif"
with open(filename, "wb") as f:
f.write(r.content)
files.append((filename, label))
except Exception as e:
print(f"Failed to download {label}: {e}")
return files

def send_email(files):
msg = EmailMessage()
today = date.today().strftime("%B %d, %Y")
msg["Subject"] = f"🛰️ Daily Weather Maps – {today}"
msg["From"] = EMAIL_SENDER
msg["To"] = EMAIL_RECEIVER
msg.set_content("Attached are today's weather and hazard outlook maps.")

for path, desc in files:
with open(path, "rb") as f:
msg.add_attachment(f.read(), maintype="image", subtype="gif", filename=f"{desc}.gif")

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
smtp.login(EMAIL_SENDER, EMAIL_PASSWORD)
smtp.send_message(msg)
