var get_subject_teachers = function (subject, grade) {
    var subjects_have_teachers = {
        "CLF": [
            ["Concepcion Agnes Sarza"],
            ["Concepcion Agnes Sarza","Prety Maloloy-on"],
            ["Marybeth Macarayan"],
            ["Nilda Torregosa","Marybeth Macarayan"],
            ["Mae Divina Velasco"],
            ["Nilda Torregosa"]
        ],
        "Chinese": [
            ["Cecilia Yap"],
            ["Nancy Uy"],
            ["Ma. Antonia Huan","Bei Yao"],
            ["Ma. Antonia Huan"],
            ["Grace Yap","Xiaoyan Zhang"],
            ["Sheng Liu","Estelita Lim"]
        ],
        "Filipino": [
            ["Jasmin Del Mar"],
            ["John Symon Bailon"],
            ["Jennifer Manatad","Jasmin Del Mar","Rachel Cabuco"],
            ["Mary Jane Rodrigo"],
            ["Jean Eleonor Velasco","Jennifer Manatad"],
            ["May Sastre","Jean Eleonor Velasco"]
        ],
        "Language": [
            ["Mildred Rios","Bernice Marsha Reyes"],
            ["Fidelis Cuay"],
            ["Bernice Marsha Reyes"],
            ["Rachel Cabuco"],
            ["Mitos Gonzales"],
            ["Ma. Elizabeth Pelen","Mitos Gonzales"]
        ],
        "Math": [
            ["Marley Arbon","Eve Vecina"],
            ["Paul John Ylanan","Vanessa Caballero","Regine Lagrimas"],
            ["Ma. Rubelyn Macion"],
            ["Susana Yap"],
            ["Anthony Hejie Suralta","Ma. Filipina Evano"],
            ["Ma. Filipina Evano","Anthony Hejie Suralta","Paul John Ylanan"]
        ],
        "Reading": [
            ["Mary Immaculate Aringay","April Dawn Dizon","Maria Lisandra Tugaoen"],
            ["Mary Immaculate Aringay","Mary Lourdes Melloria"],
            ["April Dawn Dizon"],
            ["Charlito Codizar","Mary Lourdes Melloria","Rachel Cabuco"],
            ["Charlito Codizar"],
            ["Pamela Labadan"]
        ],
        "Science": [
            [],
            [],
            ["Melanie Abello"],
            ["Regine Lagrimas","Prety Maloloy-on"],
            ["Glen Delator"],
            ["Clark Ian Pelen","Vanessa Caballero"]
        ],
        "Social Studies": [
            ["Christine Duran"],
            ["Virginia Escosora","Eve Vecina"],
            ["Virginia Escosora"],
            ["Rohaiba Radiamoda"],
            ["Marisse Paraoan","Rohaiba Radiamoda"],
            ["Alven Rey Labadan","Marisse Paraoan"]
        ],
        "Music": [
            ["Avecenna Peteros"],
            ["Avecenna Peteros"],
            ["Avecenna Peteros"],
            ["Avecenna Peteros"],
            ["Avecenna Peteros"],
            ["Avecenna Peteros"]
        ],
        "Arts": [
            ["Mylene Bersabal","Avenger Alob Jr."],
            ["Mylene Bersabal","Avenger Alob Jr."],
            ["Avenger Alob Jr.","Priscilliano Capangpangan"],
            ["Priscilliano Capangpangan","Mitos Gonzales","Avenger Alob Jr."],
            ["Priscilliano Capangpangan","Mitos Gonzales","Avenger Alob Jr."],
            ["Avenger Alob Jr.","Priscilliano Capangpangan"]
        ],
        "PE": [
            ["Priscilliano Capangpangan","Mylene Bersabal","Avenger Alob Jr."],
            ["Priscilliano Capangpangan","Mylene Bersabal","Avenger Alob Jr."],
            ["Priscilliano Capangpangan","Mylene Bersabal","Avenger Alob Jr."],
            ["Priscilliano Capangpangan","Mylene Bersabal","Avenger Alob Jr."],
            ["Priscilliano Capangpangan","Mylene Bersabal","Avenger Alob Jr."],
            ["Priscilliano Capangpangan","Mylene Bersabal","Avenger Alob Jr."]
        ],
        "HE": [
            [],
            [],
            [],
            ["John Symon Bailon"],
            ["John Symon Bailon"],
            ["John Symon Bailon"]
        ],
        "Computer": [
            ["Michael David John Abello"],
            ["Michael David John Abello"],
            ["Michael David John Abello"],
            ["Noel Martin Llevares"],
            ["Noel Martin Llevares"],
            ["Michael David John Abello","Noel Martin Llevares"]
        ]
    };
    return subjects_have_teachers[subject][grade - 1];
};

var get_subject_schedule = function (subject) {
    var schedule = {
        "CLF": [3,3,3,3,3,3],
        "Chinese": [4,4,4,4,4,4],
        "Filipino": [3,3,3,5,5,5],
        "Language": [4,4,4,3,3,3],
        "Math": [5,5,5,5,5,5],
        "Reading": [4,4,4,4,4,4],
        "Science": [0,0,5,5,5,5],
        "Social Studies": [4,4,4,4,4,4],
        "Music": [1,0,0,1,1,1],
        "Arts": [0,1,1,1,1,1],
        "PE": [1,1,1,1,1,1],
        "HE": [0,0,0,1,1,1],
        "Computer": [1,1,1,1,1,1]
    };
    return schedule[subject];
};

var get_grades_for_subject = function (subject) {
    var grade_choices = [];
    if (subject) {
        for (var i = 0; i < get_subject_schedule(subject).length; i++) {
            if (get_subject_schedule(subject)[i] > 0) {
                grade_choices.push(i + 1);
            }
        }
    }
    // return get_subject_schedule(subject);
    return grade_choices;
};