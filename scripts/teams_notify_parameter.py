from webexteamssdk import WebexTeamsAPI
import argparse
from functools import partial

SYMBOLS = {
    'red_circle': '&#x1F534;',
    'green_circle': '&#x1F7E2;'
}
BOT_ACCESS_TOKEN = 'NjkzZWYyMTYtZGVlMS00OGJjLTkyNDAtYTY5MDgwYzRiZmFiZjY0NjJjNzEtZWYw_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f'

# Room_id = 'Y2lzY29zcGFyazovL3VzL1JPT00vMzJiYzM5OTAtMGFmZS0xMWVjLTliYjUtN2ZhNTY0Zjg5NGJi'

def on_success_teams(context):
    airflow_room_id = 'Y2lzY29zcGFyazovL3VzL1JPT00vN2RjNjA1YjAtYzE2NS0xMWVjLWE2MjItMWJkZDc5NmE0ZjFh'
    dag_info = 'Dag Completion Notify'
    on_success_task(context, airflow_room_id, dag_info)

def on_failure_teams(context):
    airflow_room_id = 'Y2lzY29zcGFyazovL3VzL1JPT00vN2RjNjA1YjAtYzE2NS0xMWVjLWE2MjItMWJkZDc5NmE0ZjFh'
    dag_info = 'Dag Failure Notify'
    on_failed_task(context, airflow_room_id, dag_info)

def on_success_eloqua(context):
    eloqua_room_id = 'Y2lzY29zcGFyazovL3VzL1JPT00vMzJiYzM5OTAtMGFmZS0xMWVjLTliYjUtN2ZhNTY0Zjg5NGJi'
    dag_info = 'Eloqua Testing'
    on_success_task(context, eloqua_room_id,dag_info)


def on_failed_eloqua(context):

    eloqua_room_id = 'Y2lzY29zcGFyazovL3VzL1JPT00vMzJiYzM5OTAtMGFmZS0xMWVjLTliYjUtN2ZhNTY0Zjg5NGJi'
    dag_info = 'Eloqua Testing'
    on_failed_task(context, eloqua_room_id,dag_info)


def on_failed_task(context, room_id,dag_info):
    message = None
    message = '''
                {symbol} Task Failed. 
                *Task*: {task} 
                *Info*: {Info} 
                *Dag*: {dag} 
                *Execution Time*: {exec_date}  
                *Log Url*: {log_url} 
                '''.format(
        symbol=SYMBOLS['red_circle'],
        task=context.get('task_instance').task_id,
        Info=dag_info,
        dag=context.get('task_instance').dag_id,
        ti=context.get('task_instance'),
        exec_date=context.get('execution_date'),
        log_url=context.get('task_instance').log_url)

    send_message(message, room_id, message_type='markdown')


def on_success_task(context, room_id,dag_info):
    message = None
    message = '''
                {symbol} Task Completed. 
                *Task*: {task}
                *Info*: {Info}   
                *Dag*: {dag} 
                *Execution Time*: {exec_date}  
                *Log Url*: {log_url} 
                '''.format(
        symbol=SYMBOLS['green_circle'],
        task=context.get('task_instance').task_id,
        Info=dag_info,
        dag=context.get('task_instance').dag_id,
        ti=context.get('task_instance'),
        exec_date=context.get('execution_date'),
        log_url=context.get('task_instance').log_url)

    send_message(message, room_id, message_type='markdown')


def send_message(message, room_id, message_type='text', files=None):
    api = WebexTeamsAPI(access_token=BOT_ACCESS_TOKEN)
    success, reason = _send_message(api, message_type, room_id, message, files)
    if success is False:
        print(f'Failed to send message , reason: {reason}')


def _send_message(api, message_type, room_id, message, files, attempts=0):
    data = {
        'roomId': room_id,
        message_type: message,
    }

    if files is not None and len(files) > 0:
        data['files'] = files

    try:
        api.messages.create(**data)
        return True, None
    except Exception as err:
        if attempts == 0:
            return _send_message(api,room_id,message_type, message, files, attempts + 1)
        else:
            return False, str(err)
