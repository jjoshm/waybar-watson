#!/usr/bin/env python3
import watson
import time
import json
import arrow
import datetime

def main():
    while True:
        wat = watson.Watson()
        if wat.is_started:
            project = wat.current.get('project')
            tags = wat.current.get('tags')
            started = arrow.now() - wat.current.get('start')
            started -= datetime.timedelta(microseconds=started.microseconds)
            task = project + ': ' + ', '.join(tags)
            task_short = (task[:30] + '..') if len(task) > 30 else task
            out = {'text': task_short + ' - ' + str(started), 'tooltip': task, 'class': 'start'}
            print(json.dumps(out), flush=True)
            time.sleep(1)
            continue
        print(json.dumps({'text': 'Time logger not started!', 'class': 'stop'}), flush=True)
        time.sleep(5)

if __name__ == "__main__":
    main()
