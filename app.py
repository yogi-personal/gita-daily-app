import smtplib
import os
import random
from datetime import date
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# 1. DATABASE: Verses, Meanings, and Practical Advice
gita_quotes = [
    {
        "verse": "Chapter 2, Verse 47",
        "sanskrit": "कर्मण्येवाधिकारस्ते मा फलेषु कदाचन।",
        "transliteration": "karmaṇy-evādhikāras te mā phaleṣhu kadācana",
        "meaning": "You have a right to perform your prescribed duties, but you are not entitled to the fruits of your actions.",
        "practical_advice": "Focus on the process, not the outcome. If you are working or studying today, do it with 100% intensity and let go of the result. It reduces anxiety instantly."
    },
    {
        "verse": "Chapter 6, Verse 5",
        "sanskrit": "उद्धरेदात्मनात्मानं नात्मानमवसादयेत्।",
        "transliteration": "uddhared ātmanātmānaṃ nātmānam avasādayet",
        "meaning": "Elevate yourself through the power of your mind, and do not degrade yourself.",
        "practical_advice": "You are your own best friend. Today, catch your negative self-talk and replace it with one constructive thought. Don't be your own enemy."
    },
    {
        "verse": "Chapter 2, Verse 14",
        "sanskrit": "मात्रास्पर्शास्तु कौन्तेय शीतोष्णसुखदु:खदा:।",
        "transliteration": "mātrā-sparśhās tu kaunteya śhītoṣhṇa-sukha-duḥkha-dāḥ",
        "meaning": "The fleeting feelings of pleasure and pain are temporary; learn to endure them.",
        "practical_advice": "If you feel stressed or annoyed today, remind yourself: 'This too shall pass.' Like weather changes, your current mood is not your permanent identity."
    }
    # You can add more verses here following the same format
]

def send_gita_card():
    # 2. GET CREDENTIALS FROM GITHUB SECRETS
    sender_email = os.getenv('SENDER_EMAIL')
    app_password = os.getenv('APP_PASSWORD')
    receiver_email = os.getenv('RECEIVER_EMAIL')

    # 3. SELECTION LOGIC (Changes daily)
    random.seed(date.today().toordinal())
    today_pick = random.choice(gita_quotes)

    # 4. CREATE THE DIGITAL CARD (HTML)
    msg = MIMEMultipart("alternative")
    msg['Subject'] = f"🪔 Daily Wisdom: {today_pick['verse']}"
    msg['From'] = f"Sanatan Daily <{sender_email}>"
    msg['To'] = receiver_email

    html_content = f"""
    <html>
      <body style="font-family: Arial, sans-serif; background-color: #fdf2e9; padding: 20px;">
        <div style="max-width: 400px; margin: auto; background-color: #ffffff; border-radius: 15px; border-top: 8px solid #ff9933; box-shadow: 0 4px 8px rgba(0,0,0,0.1); padding: 25px;">
          <h2 style="color: #bf360c; text-align: center;">{today_pick['verse']}</h2>
          <hr style="border: 0; height: 1px; background: #eee;">
          <p style="font-style: italic; color: #5d4037; text-align: center; font-size: 1.1em;">"{today_pick['sanskrit']}"</p>
          <p style="color: #795548; font-size: 0.8em; text-align: center;">{today_pick['transliteration']}</p>
          <div style="margin-top: 20px;">
            <b style="color: #e65100;">Meaning:</b>
            <p style="color: #3e2723;">{today_pick['meaning']}</p>
          </div>
          <div style="background-color: #fff3e0; padding: 15px; border-radius: 10px; border-left: 5px solid #ff9933; margin-top: 20px;">
            <b style="color: #e65100;">💡 Today's Practice:</b>
            <p style="color: #3e2723;">{today_pick['practical_advice']}</p>
          </div>
        </div>
      </body>
    </html>
    """

    msg.attach(MIMEText(html_content, "html"))

    # 5. SENDING LOGIC
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, app_password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
        print("Success: Wisdom card sent!")
    except Exception as e:
        print(f"Failed to send: {e}")

if __name__ == "__main__":
    send_gita_card()
