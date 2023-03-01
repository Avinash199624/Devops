from django.utils.translation import gettext_lazy as _

"""
File used to keep messages used in views. Idea is to centralize the messages
used. All messages should be written using the _() function to allow it to be
translatable on the future.
"""

INVALID_EMAIL = _("Invalid Email")
ACCOUNT_LOCKED_DUE_TO_MULTIPLE_WRONG_ATTEMPTS = _("Account has been locked due to multiple invalid attempts")
WRONG_PASSWORD = _("Incorrect Password")
YOU_ARE_NOT_AUTHORIZED_TO_LOGIN = _("You are not authorized to login")
INVALID_MOBILE_NUMBER = _("Invalid mobile number")
WRONG_OTP = _("Incorrect OTP")
OTP_HAS_BEEN_EXPIRED = _("OTP has expired. Please request again")
LINK_EXPIRED = _("The link has expired. Please request again")
YOUR_MOBILE_IS_ALREADY_VERIFIED = _("Your mobile is already verified")
YOUR_MOBILE_HAS_BEEN_VERIFIED= _("Your mobile has been verified")
YOUR_ACCOUNT_HAS_BEEN_VERIFIED = _("Your account has been verified")
TOKEN_IS_INVALID = _("Token is invalid, request again to verify")
YOUR_EMAIL_IS_ALREADY_VERIFIED = _("Your email is already verified")
EMAIL_ALREADY_EXIST = _("Email already exists")
EMAIL_SEND_SUCCESS = _("Email send successfully on registered email ID")
MOBILE_ALREADY_EXIST = _("Mobile Number already exists")
NEERI_USER_DELETE_SUCCESS = _("User deleted successfully")
NEERI_USER_NOT_FOUND = _("User not found")
OTP_SEND_TO_REGISTERED_MOBILE_NUMBER = _("OTP has been sent to your registered mobile number")
PASSWORD_RESET_SUCCESS = _("Password reset successfully")
TOKEN_HAS_BEEN_EXPIRED = _("Token has expired. Please request again")
PASSWORD_CHANGED_SUCCESS = _("Password changed successfully")
PLEASE_ENTER_CURRENT_PASSWORD_CORRECTLY = _("Please enter the current password correctly")
USER_NOT_FOUND = _("User not found")
MOBILE_NUMBER_ALREADY_EXIST = _("Mobile Number already exists. Please try with another number")
MOBILE_NUMBER_MISMATCH = _("Old and New Mobile Number cannot be same")
USER_DELETE_SUCCESS = _("User deleted successfully")
DETAIL_NOT_FOUND = _("Information not available")
USER_PROFILE_NOT_EXIST = _("User Profile does not exist")
NEERI_USER_NOT_FOUND_FOR_GIVEN_USER = _("Please contact Admin for further details")
RECORD_DELETED_SUCCESS = _("Record deleted successfully")
USER_EXPERIENCES_NOT_FOUND = _("User Experience details could not be found")
LANGUAGES_NOT_FOUND = _("Language details could not be found")
JOB_APPLICATION_SUCCESS = _("Job application successful")
FEE_NOT_REQUIRED = _("Fee not required")
USER_SUBSCRIPTION_EXPIRED = _("User subscription expired")
PAYMENT_PENDING = _("Payment pending")
APPLICATION_ALREADY_SUBMITTED = _("Application already submitted")
DOCUMENTS_ADDED_SUCCESSFULLY = _("Documents added successfully")
DOCUMENTS_DELETED_SUCESSFUL = _("Documents deleted successfully")
STATUS_ALREADY_UPDATED = _("Status already updated")
INVALID_DOCUMENTS = _("Invalid documents")
TRAINEE_DELETED_SUCCESS = _("Trainee deleted successfully")
RELAXATION_DELETED_SUCCESS = _("Relaxation Rule deleted successfully")
USER_FELLOWSHIP_NOT_FOUND = _("Fellowship details not found")
AMOUNT_NOT_VALID = _("Amount is not valid")
FILE_UPLOADED_SUCCESSFULLY = _("File uploaded successfully")

# User management messages
ACCOUNT_ACTIVATION_SUCCESS = _("Account successfully activated")
ACCOUNT_ACTIVATION_RESEND = _(
    "If the email address is valid, a new link to activate your account will be sent"
)
ACCOUNT_CREATION_COMPLETED = _(
    "A link to activate your account has been sent to {email}"
)
CANNOT_CREATE_USER_ERROR = _("Unable to create account")
EMAIL_NOT_FOUND = _("User with given email does not exist")
INACTIVE_ACCOUNT_ERROR = _("User account is disabled")
INACTIVE_MOBILE_ERROR = _("User mobile is not verified")
INACTIVE_EMAIL_ERROR = _("User email is not verified")
INACTIVE_SUSPENDED_ERROR = _("User is suspended")
INACTIVE_LOCKED_ERROR = _("User is locked")
INACTIVE_EMAIL_MOBILE_ERROR = _("User email and mobile number are not verified")
INVALID_CREDENTIALS_ERROR = _("Unable to log in with provided credentials")
INVALID_PASSWORD_ERROR = _("Invalid password")
INVALID_TOKEN_ERROR = _("Invalid token for given user")
INVALID_UID_ERROR = _("Invalid user id or user doesn't exist")
LOGOUT_SUCCESSFUL = _("Logout successful")
PASSWORD_MISMATCH_ERROR = _("The Current and Confirm Password fields do not match")
PASSWORD_RESET_REQUESTED = _(
    "If the email address is valid, an email will be sent to reset your password"
)
STALE_TOKEN_ERROR = _("Stale token for given user")
USERNAME_MISMATCH_ERROR = _("The two {0} fields didn't match")
USERNAME_ALREADY_USED_ERROR = _("A user with that username already exists")
USERNAME_EMAIL_ALREADY_USED_ERROR = _(
    "A user with that username and email already exists"
)
USER_SESSION_ACTIVE = _("Session active")

# Pro user management messages
PRO_USER_ESTA_LINK_SUCCESSFUL = _("Pro user successfully linked with Establishment")
NOT_PRO_USER_ACCOUNT_ERROR = _("Not a pro user")

# Permissions
AUTHENTICATED_USER_PERMISSION_DENIED = _(
    "Operation not allowed for authenticated users"
)

# Generics
COOKIES_DISABLED_ERROR = _("Please enable cookies and try again")
NOT_FOUND_ERROR = _("Not found")
RECORD_SOFT_DELETED = _("Data deleted successfully")
TEMPLATE_DELETED_SOFT_DELETE = _("Template saved successfully")
NOT_VALID_JOB_POST = _("Please select a job status")
PERMANENT_POSITION_SOFT_DELETED = _("Permanent Position deleted successfully")
TEMPORARY_POSITION_SOFT_DELETED = _("Application Position deleted successfully")
SUCCESSFULLY_REJECTED = _("Applicant successfully rejected")
INVALID_REQUEST = _("Invalid Request")
DATA_ADDED_SUCCESSFULLY = _("Data added successfully")
