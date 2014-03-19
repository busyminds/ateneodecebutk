import requests
import string


def send_message(request, class_data):
    teacher = class_data['teacher']
    level = class_data['level']
    subject = class_data['subject']

    if 'ateneodecebu.tk' in request.get_host():
        recipients = [
            'noelmartin@gmail.com',
            'annieabucay13@yahoo.com',
            'lepamores@yahoo.com',
            'jonasemile@gmail.com'
        ]
    else:
        recipients = [
            'dashmug@gmail.com'
        ]

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
             <a href="http://ateneodecebu.tk/gradebook">
                http://ateneodecebu.tk/gradebook
             </a>.
        </p>
        </body>
        </html>
    '''

    tmpl = string.Template('''
        <!doctype html>
        <html>
        <body>
        <p>
            <em>Note: This is an automated message.</em>
        </p>
        <p>
            <em class="text-success">$teacher </em>
            has updated his/her Gradebook for
            <em class="text-success">$subject $level</em>.
        </p>
        <p>
            You may see the updates at
             <a href="http://ateneodecebu.tk/gradebook">
                http://ateneodecebu.tk/gradebook
             </a>.
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
        'to': recipients,
        'subject': '[SHS-AdC Gradebook] ' + teacher
                   + ' has updated the Gradebook.',
        'html': html_body}

    return requests.post(endpoint, auth=credentials, data=email_data)
