import requests
import string

def send_message(class_data):
    teacher = class_data['teacher']
    level = class_data['level']
    subject = class_data['subject']

    html_body = '''
        <!doctype html>
        <html>
        <body>
        <p>
            <strong>Mr. Noel Martin Llevares </strong>
            has updated his Gradebook for <strong>Computer 6</strong>.
        </p>
        <p>
            You may see the updates at
             <a href="http://ateneodecebu.tk/gradebook">http://ateneodecebu.tk/gradebook</a>.
        </p>
        </body>
        </html>
    '''

    tmpl = string.Template('''
        <!doctype html>
        <html>
        <body>
        <p>
            <strong>$teacher </strong>
            has updated his Gradebook for <strong>$subject $level</strong>.
        </p>
        <p>
            You may see the updates at
             <a href="http://ateneodecebu.tk/gradebook">http://ateneodecebu.tk/gradebook</a>.
        </p>
        </body>
        </html>
    ''')
    html_body = tmpl.substitute(teacher=teacher, level=level, subject=subject)


    endpoint = 'https://api.mailgun.net/v2/sandbox53636.mailgun.org/messages'
    credentials = ('api', 'key-0o543t46p791fhsd2ou3cu4m7vjphj40')
    email_data = {
        'from': 'SHS-AdC Gradebook <gradebook@sandbox53636.mailgun.org>',
        'h:Reply-To': 'noelmartin@gmail.com',
        'to': ['dashmug@gmail.com'],
        'subject': '[SHS-AdC Gradebook] ' + teacher + ' has updated the Gradebook.',
        'html': html_body}

    return requests.post(endpoint, auth=credentials, data=email_data)
