import os
import json
import time

from ateneodecebutk.settings.base import BASE_DIR

SUBJECT_CODES = [
    ('CHI', 'Chinese'),
    ('CLF', 'CLF'),
    ('FIL', 'Filipino'),
    ('LAN', 'Language'),
    ('MAT', 'Mathematics'),
    ('RDG', 'Reading'),
    ('SCI', 'Science'),
    ('SOC', 'Social Studies'),
    ('MUS', 'Music'),
    ('ART', 'Arts'),
    ('PE', 'PE'),
    ('HE', 'HE'),
    ('COM', 'Computer')
]

SECTION_CODES = [
    [
        ('G1A', '1-Sales'),
        ('G1B', '1-Azevedo'),
        ('G1C', '1-Imbert'),
        ('G1D', '1-Andrade'),
        ('G1E', '1-Mayer'),
        ('G1F', '1-Hoyos'),
        ('G1G', '1-Pro')
    ],
    [
        ('G2A', '2-De Brito'),
        ('G2B', '2-Acquaviva'),
        ('G2C', '2-Pacheco'),
        ('G2D', '2-Spinola'),
        ('G2E', '2-Jerome'),
        ('G2F', '2-Ricci')
    ],
    [
        ('G3A', '3-Miki'),
        ('G3B', '3-Borgia'),
        ('G3C', '3-Rodriguez'),
        ('G3D', '3-Arrowsmith'),
        ('G3E', '3-Colombiere')
    ],
    [
        ('G4A', '4-Berchmans'),
        ('G4B', '4-Jogues'),
        ('G4C', '4-Campion'),
        ('G4D', '4-Pignatelli'),
        ('G4E', '4-Del Castillo')
    ],
    [
        ('G5A', '5-Xavier'),
        ('G5B', '5-Faber'),
        ('G5C', '5-Hurtado'),
        ('G5D', '5-Garate'),
        ('G5E', '5-San Vitores')
    ],
    [
        ('G6A', '6-Loyola'),
        ('G6B', '6-Regis'),
        ('G6C', '6-Claver'),
        ('G6D', '6-Bellarmine'),
        ('G6E', '6-Canisius'),
        ('G6F', '6-Gonzaga')
    ]
]

def time_difference(timestamp):
    difference = time.time() - timestamp

    if difference < 1:
        return '0 seconds'

    time_factors = [(365 * 24 * 60 * 60, 'year'),
                    (30 * 24 * 60 * 60, 'month'),
                    (24 * 60 * 60, 'day'),
                    (60 * 60, 'hour'),
                    (60, 'minute'),
                    (1, 'second'),
    ]

    for seconds, time_string in time_factors:
        d = difference/seconds
        if d >= 1:
            r = round(d)
            if r > 1:
                plural = 's ago'
            else:
                plural = ' ago'
            return '%d %s%s' % (r, time_string, plural)

def get_subject_status(grade_level):
    subject_data = []
    subjects = list(SUBJECT_CODES)
    if grade_level < 4:
        subjects.remove(('HE', 'HE'))
        if grade_level < 3:
            subjects.remove(('SCI', 'Science'))

    grading_period = 4

    data_dir = os.path.join(BASE_DIR, 'files/gradebook/assessments/'
        + str(grading_period) + '/levels/' + str(grade_level) + '/')

    for subject in subjects:
        section_data = []
        for section in SECTION_CODES[grade_level - 1]:
            filename = "%s-%s.json" % (section[0], subject[0])
            try:
                json_file = open(os.path.join(data_dir, filename))
            except IOError:
                subject_section_status = None
            else:
                json_data = json.load(json_file)
                subject_section_status = {
                    'class_code': "%s-%s" % (section[0], subject[0]),
                    'teacher': json_data['teacher'],
                    'age': time_difference(json_data['timestamp'])
                }
            section_data.append(subject_section_status)
        subject_data.append((subject[1], section_data))

    return subject_data
