

OMNIA_FILE_NAME = "Omnia.xls"

OPERATORS = [ # código do operador não aparece no arquivo do omnia novo
    (1, "Adriana.Bernardeli"),
    (2, "Erica.Santos"),
    (3, "Guilherme.Romanholi"),
    (4, "Luiz.Melo"),
    (5, "Maria.Goncalves"),
    (6, "Marilene.Juste"),
    (7, "Maria.Cavichioli"),
    (8, "Julio.Torre"),
    (9, "Anderson.Augusto"),
]

CONFIG_TESTS = {
    'TheraLaseSurgery2016.Omnia':
        ("TheraLaseSurgery", range(1, 10)),
    'TheraLaseSurgery_6-INSP-493_rev03.Omnia':
        ("TheraLaseSurgery", range(1, 10)),
    'FamiliaTheraLase_6-INSP-493_rev04.Omnia':
        ("FamiliaTheraLase", range(1, 10)),
    'FamiliaTheraLase_6-INSP-493_rev05.Omnia':
        ("FamiliaTheraLase", range(1, 10)),
    'Therapy.Omnia':
        ("Therapy", range(1, 8)),
    'MediLaserDual_6-INSP-495_rev.04':
        ("MedilaserDual", range(1, 15)),
    'EmeraldGreenLaser_6-INSP-657_rev.00.Omnia':
        ("EmeraldGreenLaser", range(1, 10)),

    # novos
    'THE_R9':
        ("Therapy", range(1, 8)),
    'THERA_R4':
        ("FamiliaTheraLase", range(1, 10)),
    'EASYL_R5':
        ("Easy Laser", range(1, 14)),
    'ELIB-R4':
        ("e-lib", range(1, 9)),

    "D2000_R3": (
        "D-2000", range(1, 7)
        ),
    "ELIGH_R5": (
        "e-light", range(1, 9)
        ),
    "ELITE_R5": (
        "FamiliaElite", range(1, 26)
        ),
    "MED_AT": (
        "Medilaser", range(1, 14)
        ),
    "MED_D_R4": (
        "MediLaser-Dual", range(1, 14)
        ),
    "WPLUS_R6": (
        "WhiteningPlus", range(1, 27)
        ),
    "WPREM_R4": (
        "WhiteningPremium", range(1, 22)
        ),

    # vulcan e triplet novos (2023)
    'Vulcan_6-INSP-0583_rev.00.Omnia':
        ("Vulcan", range(1, 17)),
    'Triplet_6-INSP-526_rev.02.Omnia':
        ("FamiliaTriplet", range(1, 24)),

    'e-light_6-INSP-0548_rev05.Omnia':
        ("e-light", range(1, 10)),
    'EasyLaser.Omnia':
        ("EasyLaser", range(1, 15)),


    "D-2000.Omnia":
        ("D-2000", range(1, 7)),
    "MediLaserDual_6-INSP-495_rev.04.Omnia":
        ("MediLaser-Dual", range(1, 14)),
    "FamiliaMedilaser OS - AT.Omnia":
        ("Medilaser", range(1, 14)),
}
