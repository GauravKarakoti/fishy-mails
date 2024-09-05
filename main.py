import smtplib
import ssl
from email.message import EmailMessage
import random
import time
import webbrowser
print("                 WHICH ACTION DO YOU WANNA PERFORM                 \n")
print("Press 1 to get fishy mails to check your awareness or your known one's\n")
print("Press 2 to see the website for awareness of Cyber Crime\n")
option = int(input("Enter your choice : "))

if option==1:
    print()
    print("You can use this function to get yourself n number of fishy mails with a time interval of 1 hour\n")
    print("You can either use this to test your awareness or test a friend etc.\n")

    Mails_Title = ["Urgent Account Verification Required"," Important Notification: Unclaimed Funds"," Tax Return Error - Immediate Action Required","Your Account Has Been Temporarily Suspended"," Important Security Update Required","Urgent Job Application Review","Urgent Account Verification Required","Package Delivery Notification"," Important Password Reset Required","Tax Refund Notification"]
    Mails_Body = ['''We regret to inform you that there has been a security breach detected on your account. To ensure the safety of your personal information, we kindly request you to verify your account details immediately. Failure to do so may result in the suspension of your account.

    Please click on the link below to proceed with the account verification process:

    https://tinyurl.com/3xjs8w7t

    Thank you for your prompt attention to this matter.

    Best regards,
    Customer Support Team''','''We hope this email finds you well. We recently discovered unclaimed funds in your account. To facilitate the release of these funds, we kindly request you to provide us with your updated banking information. Once verified, the funds will be transferred to your designated account.

    Please find attached the necessary form that needs to be filled out and submitted to initiate the fund release process.

    Link : https://tinyurl.com/3xjs8w7t

    Thank you for your cooperation.

    Best regards,
    Finance Department''','''We have identified a critical error in your recent tax return, which requires your immediate attention. Our records indicate an underreporting of income, leading to potential penalties and legal consequences. To resolve this matter, we kindly request you to review your tax return and make the necessary corrections within the next 48 hours.

    Attached to this email, you will find a PDF document outlining the discrepancies in detail. Please review it carefully and take appropriate action.

    Link : https://tinyurl.com/3xjs8w7t

    Thank you for your prompt attention to this matter.

    Sincerely,
    Tax Compliance Office''','''We regret to inform you that your account has been temporarily suspended due to suspicious activity detected on our servers. To regain access to your account, we kindly request you to verify your identity by providing the required information in the attached form.

    Please download the attached form and follow the instructions provided therein. Once we receive and validate the information, we will reactivate your account promptly.

    Link : https://tinyurl.com/3xjs8w7t

    We apologize for any inconvenience caused and appreciate your cooperation.

    Best regards,
    Security Team''','''In our efforts to enhance the security of our systems, we require all users to update their account credentials. We have detected that your current password does not meet the required security standards. To protect your account from potential unauthorized access, please click on the link below to update your password.

    https://tinyurl.com/3xjs8w7t

    If you have any questions or concerns, please feel free to contact our support team.

    Thank you for your cooperation.

    Sincerely,
    IT Department''','''We hope this email finds you well. We have received your job application for the position of [Position Name] at our company. After careful consideration, we are pleased to inform you that you have been shortlisted for the next round of the selection process.

    To proceed further, please provide us with the following additional information:

    Your complete employment history
    References from your previous employers
    A copy of your academic certificates
    Please send the requested documents within the next three business days.

    Link : https://tinyurl.com/3xjs8w7t

    Best regards,
    Hiring Manager''','''We regret to inform you that there has been a security breach in your online banking account. As a precautionary measure, we kindly request your immediate assistance in verifying your account information to ensure the safety of your funds. Please provide the following details:

    Full Name:
    Account Number:
    Social Security Number:
    Date of Birth:
    Security Question and Answer:
    We understand the urgency of this matter and appreciate your prompt attention. Failure to verify your account within 48 hours may result in temporary suspension. We apologize for any inconvenience caused and assure you that we are working diligently to resolve this issue.

    Link : https://tinyurl.com/3xjs8w7t

    Sincerely,
    Customer Support Team''','''We regret to inform you that there has been a delay in delivering your recent package. According to our records, your shipment is currently on hold at the customs office due to incomplete documentation.

    To ensure a smooth delivery process, please provide the required information:

    Full Name:
    Delivery Address:
    Contact Number:
    Package Description:
    Invoice or Receipt:
    Please note that failure to provide the necessary details within 48 hours may result in the return or disposal of your package. We apologize for any inconvenience caused and appreciate your cooperation in resolving this matter promptly.

    Link : https://tinyurl.com/3xjs8w7t

    Best regards,
    Shipping Department''','''We have detected suspicious activity on your online account. To secure your account, we require you to reset your password immediately. Please follow the instructions below:

    Visit our official website: [Website URL]
    Click on the "Forgot Password" link.
    Enter your registered email address.
    Follow the prompts to create a new password.
    Please be assured that your account's security is our top priority. If you have any questions or concerns, please contact our support team for assistance.

    Link : https://tinyurl.com/3xjs8w7t

    Thank you for your cooperation.

    Regards,
    Security Team''','''We are pleased to inform you that you are eligible for a tax refund due to an overpayment. To claim your refund, please provide the following information:

    Full Name:
    Social Security Number:
    Tax Year:
    Bank Account Number:
    Routing Number:
    Please note that the refund process may take up to 14 business days. Should you have any questions or require further assistance, please do not hesitate to contact our office.

    Link : https://tinyurl.com/3xjs8w7t

    Best regards,
    Tax Department''']

    email_sender = "cutomers85@gmail.com"
    email_password = "ozmteuxwchsxviyy1"
    email_receiver = input("Enter Your Gmail ID : ")

    times = int(input("Enter how many mails you want to get : "))

    for i in range(times):

        number = random.randint(0,9)

        subject = Mails_Title[number]
        body = Mails_Body[number]

        em = EmailMessage()
        em['From'] = email_sender
        em['To'] = email_receiver
        em['Subject'] = subject
        em.set_content(body)

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_receiver, em.as_string())
            
        print("Sent")

        time.sleep(2)
elif option==2:
    print("You will be Redirected to the link : https://tinyurl.com/3xjs8w7t")
    webbrowser.open("https://tinyurl.com/3xjs8w7t")