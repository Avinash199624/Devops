import http.client
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
from rest_framework import request
from twilio.rest import Client
from post_office import mail
from communication_template.models import CommunicationMaster
from job_posting.models import JobPosting
from neeri_recruitment_portal import settings
from neeri_recruitment_portal.settings import BASE_QA_URL


@csrf_exempt
def send_otp(mobile, otp):   # /verify_mobile/
    conn = http.client.HTTPSConnection("api.msg91.com")
    authkey = "186966AR7yG91ts5a27b827"
    senderid = "FNDGPI"
    print("senderid---->", senderid)
    otp = str(otp)
    route = "default"
    countrycode = "+91"
    mobile = str(mobile)
    #DLT_TE_ID = "1207163894804676269"
    DLT_TE_ID = "1207164025166408885"
    #message = "Your%20OTP%20for%20verification%20of%20NEERI%20Registration%20is%20" + otp + ".%20Thanks%20FNDGPI"
    message = "Your%20OTP%20for%20verification%20of%20NEERI%20Recruitment%20Portal%20registration%20is%20" + otp + ".%20Thanks,%20FNDGPI"
    headers = {'content-type': "application/json"}
    url = "/api/sendotp.php?authkey=" + authkey + "&message=" + message + "&sender=" + senderid + "&mobile=91" + mobile + "&otp=" + otp + "&DLT_TE_ID=" + DLT_TE_ID
    print("url---->", url)
    conn.request("GET", url, headers=headers)
    res = conn.getresponse()
    data = res.read()
    print(data)
    print("OTP sent")
    return None


# def send_otp(mobile, otp):  # /verify_mobile/
#     # import ipdb;ipdb.set_trace()
#     client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
#     countrycode = settings.COUNTRY_CODE
#     senderid = "NEERIC"
#     message = client.messages \
#         .create(
#         body="Your OTP for Verification is  "+str(otp)+" &sender="+senderid,
#         from_=settings.MOBILE_OTP_FROM,
#         to=countrycode+mobile
#     )
#
#     print(message.sid)
#     print("OTP sent")
#     return None

# conn = http.client.HTTPSConnection("api.msg91.com")
# authkey = settings.AUTH_KEY
# senderid = "NEERIC"
# print("senderid---->", senderid)
#
# route = settings.ROUTE
# countrycode = settings.COUNTRY_CODE
# headers = {'content-type': "application/json"}
# # url = "http://control.msg91.com/api/sendotp.php?otp="+otp+"&message="+"Your otp is "+otp +"&mobile="+mobile+"&authkey="+authkey+"&country=91"
# url = "/api/v2/sendsms?authkey="+authkey+"&mobiles="+mobile+"&message=Your OTP for Verification is "+ otp +"&sender="+senderid+"&route="+route+"&country="+countrycode+""
# print("url---->", url)
# conn.request("GET", url, headers=headers)
# res = conn.getresponse()
# data = res.read()
# print(data)
# print("OTP sent")
# return None


def send_verification_mail(email, email_token):
    template = CommunicationMaster.objects.filter(comm_type__communication_type='EMAIL',
                                                  action_type__comm_action_type='VERIFY EMAIL', is_active=True).first()
    subject = template.subject
    message = template.body + "\n" + BASE_QA_URL + f'/verify_email/{email_token}/\n\n' \
                                                   f'Regards,\nNEERI Recruitment Team'
    email_from = settings.EMAIL_SEND_FROM
    recipient_list = [email]
    mail.send(
        recipient_list,  # List of email addresses also accepted
        email_from,
        context=None,
        subject=subject,
        message=message,
        priority='now',
    )
    print("email sent")
    return None


def send_update_jobpost_mail(email, user_name, job_posting):

    """Send mail to job-pist editable-user and management role users """
    template = CommunicationMaster.objects.filter(comm_type__communication_type='EMAIL',
                                                  action_type__comm_action_type='UPDATED JOBPOST', is_active=True).first()
    subject = template.subject
    job_post = JobPosting.objects.get(job_posting_id=job_posting.job_posting_id)
    if job_post:
        notification_id = job_posting.notification_id
        notification_title = job_posting.notification_title
        publication_date = job_posting.publication_date
        end_date = job_posting.end_date
        job_type = job_posting.job_type
        message = "Dear "+str(user_name)+"\n"+"\n"+template.body +"\n"+"\n"+"Notification ID : "+str(notification_id)+"\n"+"Notification Title : "+str(notification_title)+"\n"+"Notification Type : "+str(job_type)+"\n"+"Start Date : "+str(publication_date)+"\n"+"End Date : "+str(end_date)+"\n"+"\n"\
                                                                                +"\n"+"You can also view the updated job post using link below :"+"\n"+"\n"+BASE_QA_URL + f'/update_jobpost/{job_post}/\n\n'+f'Kindly Regards,\nNEERI Recruitment Team'
        email_from = settings.EMAIL_SEND_FROM
        recipient_list = email
        mail.send(
            recipient_list,  # List of email addresses also accepted
            email_from,
            context=None,
            subject=subject,
            message=message,
            priority='now',
        )

    print("email sent")
    return None



def send_forget_password_mail(email , token ):
    template = CommunicationMaster.objects.filter(comm_type__communication_type='EMAIL',
                                                  action_type__comm_action_type='FORGOT PASSWORD', is_active=True).first()
    subject = template.subject
    message = template.body+" " + BASE_QA_URL + f'/reset_password/{token}/'
    email_from = settings.EMAIL_SEND_FROM

    recipient_list = [email]
    mail.send(
        recipient_list,  # List of email addresses also accepted
        email_from,
        context=None,
        subject=subject,
        message=message,
        priority='now',
    )
    return True


def send_password_mail(email, password):
    template = CommunicationMaster.objects.filter(comm_type__communication_type='EMAIL',
                                                  action_type__comm_action_type='CHANGE PASSWORD',
                                                  is_active=True).first()
    subject = template.subject
    message = template.body + f' {password}.\n' + BASE_QA_URL + f'/admin/'
    email_from = settings.EMAIL_SEND_FROM

    recipient_list = [email]
    mail.send(
        recipient_list,  # List of email addresses also accepted
        email_from,
        context=None,
        subject=subject,
        message=message,
        priority='now',
    )
    print("email sent")
    return None
