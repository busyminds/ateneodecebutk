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

def get_subjects(grade_level):
    subjects = list(SUBJECT_CODES)
    if grade_level < 4:
        subjects.remove(('HE', 'HE'))
        if grade_level < 3:
            subjects.remove(('SCI', 'Science'))
    return subjects
