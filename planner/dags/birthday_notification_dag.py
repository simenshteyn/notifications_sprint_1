import logging

from airflow.models import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago

from operators.birthday_check_operator import BirthdayCheckOperator
from operators.send_notifications import NotificationSender

log = logging.getLogger(__name__)

args = {"owner": "team_2", "start_date": days_ago(1)}

dag = DAG(dag_id="birthday_notification_dag", default_args=args, schedule_interval="00 12 * * *")


def get_birthdays():
    NotificationSender().send_notifications()


def send_notifications():
    print("I am coming last")


with dag:
    get_birthdays_task = BirthdayCheckOperator(
        task_id="get_birthdays_task",
        correct_way="send_notifications_task",
        wrong_way="no_birthdays_op",
    )

    send_notifications_task = PythonOperator(
        task_id="send_notifications_task", python_callable=send_notifications
    )
    no_birthdays_op = DummyOperator(task_id="no_birthdays_op")

    get_birthdays_task >> [no_birthdays_op, send_notifications_task]
