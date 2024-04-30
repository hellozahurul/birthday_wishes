from datetime import date, timedelta
from .models import Customer
from django.conf import settings

def send_birthday_wishes():
    today = date.today()
    birthdays = Customer.objects.filter(birthday__month=today.month, birthday__day=today.day)
    for customer in birthdays:
        # Simulate email sending (replace with actual email sending logic)
        print(f"Sending birthday wish email to {customer.name} at {customer.email}")

# Schedule the task to run daily at midnight
from django.utils.timezone import utcnow
schedule = settings.SCHEDULER
schedule.every().day.do(send_birthday_wishes).run_at(utcnow().replace(hour=0, minute=0, second=0, microsecond=0))
