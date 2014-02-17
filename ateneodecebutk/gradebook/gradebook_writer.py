import json
import os

from datetime import datetime
from xlrd import open_workbook
from xlrd import XL_CELL_NUMBER
from xlrd import xldate_as_tuple

from ateneodecebutk.settings.base import BASE_DIR

SUBJECT_CODES = {
    "Arts": "ART",
    "Chinese": "CHI",
    "CLF": "CLF",
    "Computer": "COM",
    "Filipino": "FIL",
    "HE": "HE",
    "Language": "LAN",
    "Mathematics": "MAT",
    "Music": "MUS",
    "PE": "PE",
    "Reading": "RDG",
    "Science": "SCI",
    "Social Studies": "SOC"
}

SECTION_CODES = {
    "1-Sales": "G1A",
    "1-Azevedo": "G1B",
    "1-Imbert": "G1C",
    "1-Andrade": "G1D" ,
    "1-Mayer": "G1E",
    "1-Hoyos": "G1F",
    "1-Pro": "G1G",
    "2-De Brito": "G2A",
    "2-Acquaviva": "G2B",
    "2-Pacheco": "G2C",
    "2-Spinola": "G2D",
    "2-Jerome": "G2E",
    "2-Ricci": "G2F",
    "3-Miki": "G3A",
    "3-Borgia": "G3B",
    "3-Rodriguez": "G3C",
    "3-Arrowsmith": "G3D",
    "3-Colombiere": "G3E",
    "4-Berchmans": "G4A",
    "4-Jogues": "G4B",
    "4-Campion": "G4C",
    "4-Pignatelli": "G4D",
    "4-Del Castillo": "G4E",
    "5-Xavier": "G5A",
    "5-Faber": "G5B",
    "5-Hurtado": "G5C",
    "5-Garate": "G5D",
    "5-San Vitores": "G5E",
    "6-Loyola": "G6A",
    "6-Regis": "G6B",
    "6-Claver": "G6C",
    "6-Bellarmine": "G6D",
    "6-Canisius": "G6E",
    "6-Gonzaga": "G6F"
}

NON_GRADESHEETS = (
    "Management",
    "Status",
    "Curriculum",
    "_lists",
    "_template",
    "_blank",
    "_components",
)

COMPONENT_COLUMNS = [5, 28, 51, 74]

GRADEBOOK_DATA_DIR_PREFIX = 'files/gradebook/assessments/Q'

def convert_excel_date(excel_date, workbook):

    """ Converts Excel dates to Unix timestamp format """

    result = datetime(*xldate_as_tuple(excel_date, workbook.datemode))
    return int(result.strftime("%s"))


def get_activity_data(section, column, workbook):

    """ Gets data from a specific column """
    excel_date = section.cell_value(1, column)

    if excel_date != '':
        activity_date = convert_excel_date(excel_date, workbook)
    else:
        activity_date = None

    description = section.cell_value(2, column).strip()
    points = section.cell_value(3, column)

    competencies = section.cell_value(59, column)

    average_score = round(section.cell_value(61, column), 2)
    average_percent_score = round(section.cell_value(62, column), 4)

    activity_average = {
        "average_score": average_score,
        "average_percent_score": average_percent_score
    }

    scored_90_and_above = round(section.cell_value(64, column), 4)
    scored_85_to_90 = round(section.cell_value(65, column), 4)
    scored_80_to_85 = round(section.cell_value(66, column), 4)
    scored_75_to_80 = round(section.cell_value(67, column), 4)
    scored_60_to_75 = round(section.cell_value(68, column), 4)
    scored_below_60 = round(section.cell_value(69, column), 4)

    activity_histogram = {
        "scored_90_and_above": scored_90_and_above,
        "scored_85_to_90": scored_85_to_90,
        "scored_80_to_85": scored_80_to_85,
        "scored_75_to_80": scored_75_to_80,
        "scored_60_to_75": scored_60_to_75,
        "scored_below_60": scored_below_60
    }

    passing_rate = round(section.cell_value(71, column), 4)

    activity = {
        "date": activity_date,
        "description": description,
        "points": points,
        "competencies": competencies.split(" "),
        "activity_average": activity_average,
        "activity_histogram": activity_histogram,
        "passing_rate": passing_rate
    }

    return activity


def get_component_data(sheet, component, workbook):

    """ Gets data for a specific grading component """

    column_start = COMPONENT_COLUMNS[component - 1]
    column_end = column_start + 19

    # check to see if component is being used
    if sheet.cell_value(3, column_start + 20) != 0:
        activities = []

        for column in range(column_start, column_end):
            if sheet.cell_type(3, column) is XL_CELL_NUMBER:
                activity = get_activity_data(sheet, column, workbook)
                activities.append(activity)

        component_name = sheet.cell_value(0, column_start)
        component_weight = sheet.cell_value(1, column_start + 20)
        component_perfect_score = sheet.cell_value(3, column_start + 20)
        component_average_score = sheet.cell_value(57, column_start + 20)
        component_average_score = round(component_average_score, 2)
        component_average_grade = sheet.cell_value(57, column_start + 21)
        component_average_grade = round(component_average_grade, 2)

        component = {
            "component_name": component_name,
            "component_weight": component_weight,
            "component_perfect_score": component_perfect_score,
            "component_average_score": component_average_score,
            "component_average_grade": component_average_grade,
            "activities": activities
        }

        return component
    else:
        return None


def get_periodical_test_data(sheet, workbook):
    """ Gets data for the periodical test """
    if sheet.cell_type(3, 99) is XL_CELL_NUMBER:

        points = sheet.cell_value(3, 99)

        average_score = round(sheet.cell_value(61, 99), 2)
        average_percent_score = round(sheet.cell_value(62, 99), 4)

        pt_average = {
            "average_score": average_score,
            "average_percent_score": average_percent_score
        }

        scored_90_and_above = round(sheet.cell_value(64, 99), 4)
        scored_85_to_90 = round(sheet.cell_value(65, 99), 4)
        scored_80_to_85 = round(sheet.cell_value(66, 99), 4)
        scored_75_to_80 = round(sheet.cell_value(67, 99), 4)
        scored_60_to_75 = round(sheet.cell_value(68, 99), 4)
        scored_below_60 = round(sheet.cell_value(69, 99), 4)

        pt_histogram = {
            "scored_90_and_above": scored_90_and_above,
            "scored_85_to_90": scored_85_to_90,
            "scored_80_to_85": scored_80_to_85,
            "scored_75_to_80": scored_75_to_80,
            "scored_60_to_75": scored_60_to_75,
            "scored_below_60": scored_below_60
        }

        passing_rate = round(sheet.cell_value(71, 99), 4)

        periodical_test_data  = {
            "points": points,
            "pt_average": pt_average,
            "pt_histogram": pt_histogram,
            "passing_rate": passing_rate
        }

        periodical_test_perfect_score = sheet.cell_value(3, 99)
        periodical_test_average_score = round(sheet.cell_value(57, 99), 2)
        periodical_test_average_grade = round(sheet.cell_value(57, 100), 2)

        periodical_test = {
            "periodical_test_name": "Periodical Test",
            "periodical_test_weight": 0.25,
            "periodical_test_perfect_score": periodical_test_perfect_score,
            "periodical_test_average_score": periodical_test_average_score,
            "periodical_test_average_grade": periodical_test_average_grade,
            "periodical_test_data": periodical_test_data
        }

        return periodical_test
    else:
        return None


def get_section_data(sheet, workbook):

    """ Gets data for a specific sheet """

    components = []
    for component in range(1, 5):
        components.append(get_component_data(sheet, component, workbook))

    periodical_test = get_periodical_test_data(sheet, workbook)

    section_average = round(sheet.cell_value(57, 2), 2)

    range_95_and_above = int(sheet.cell_value(60, 102))
    range_90_to_95 = int(sheet.cell_value(61, 102))
    range_85_to_90 = int(sheet.cell_value(62, 102))
    range_80_to_85 = int(sheet.cell_value(63, 102))
    range_75_to_80 = int(sheet.cell_value(64, 102))
    range_below_75 = int(sheet.cell_value(65, 102))

    section_histogram = {
        "range_95_and_above": range_95_and_above,
        "range_90_to_95": range_90_to_95,
        "range_85_to_90": range_85_to_90,
        "range_80_to_85": range_80_to_85,
        "range_75_to_80": range_75_to_80,
        "range_below_75": range_below_75
    }

    management_sheet = workbook.sheet_by_name('Management')
    teacher = management_sheet.cell_value(4, 5).strip()
    subject = management_sheet.cell_value(4, 2).strip()

    level =  int(sheet.name.split("-")[0].strip())
    section_name =  sheet.name.split("-")[1].strip()

    section_data = {
        "section": section_name,
        "components": components,
        "section_average_grade": section_average,
        "section_histogram": section_histogram,
        "teacher": teacher,
        "level": level,
        "subject": subject,
        "periodical_test": periodical_test
    }

    return section_data


def get_competency_codes(workbook):
    curriculum_sheet = workbook.sheet_by_name('Curriculum')
    competency_codes = []
    for row in range(3, 24):
        if curriculum_sheet.cell_value(row, 0) != "":
            code = curriculum_sheet.cell_value(row, 0).strip()
            competency = curriculum_sheet.cell_value(row, 1).strip()
            competency_codes.append({
                "code": code,
                "competency": competency
            })

    return competency_codes


def write_gradebook_data(grading_period, filename):
    workbook_filename = filename
    workbook = open_workbook(workbook_filename)
    management_sheet = workbook.sheet_by_name('Management')
    subject = management_sheet.cell_value(4, 2).strip()

    for sheet in workbook.sheets():
        if sheet.name not in NON_GRADESHEETS:
            class_data = get_section_data(sheet, workbook)

            class_data["timestamp"] = int(datetime.today().strftime("%s"))
            class_data["date_created"] = datetime.today().strftime("%D")

            competency_codes = get_competency_codes(workbook)
            class_data["competency_codes"] = competency_codes

            assessment_json = json.dumps(class_data, separators=(',', ':'))

            levels_dir = os.path.join(BASE_DIR, GRADEBOOK_DATA_DIR_PREFIX
                + str(grading_period) + '/levels/'
                + str(class_data["level"]) + '/')

            subjects_dir = os.path.join(BASE_DIR, GRADEBOOK_DATA_DIR_PREFIX
                + str(grading_period) + '/subjects/'
                + SUBJECT_CODES[subject] + '/')

            filepaths = (levels_dir, subjects_dir)

            filename = (SECTION_CODES[sheet.name] + "-"
                            + SUBJECT_CODES[subject] + ".json")

            for path in filepaths:
                assessment_file = open(path + filename, "w")
                assessment_file.write(assessment_json)

            assessment_file.close()

            return {
                'teacher': class_data['teacher'],
                'level': class_data['level'],
                'subject': class_data['subject'],
            }
