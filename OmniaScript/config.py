

OMNIA_FILE_NAME = "Omnia.xls"

CONFIG_TESTS = {
    'TheraLaseSurgery2016.Omnia': 
        ("TheraLaseSurgery", range(1,10)),
    'TheraLaseSurgery_6-INSP-493_rev03.Omnia':
        ("TheraLaseSurgery", range(1,10)),
    'FamiliaTheraLase_6-INSP-493_rev04.Omnia':
        ("FamiliaTheraLase", range(1,10)),
    'Therapy.Omnia': 
        ("Therapy", range(1,8)),
    'MediLaserDual_6-INSP-495_rev.04' :
        ("MedilaserDual", range(1,15)),
    'EmeraldGreenLaser_6-INSP-657_rev.00.Omnia' :
        ("EmeraldGreenLaser", range(1,10)),
    
    # novos
    'THE_R9': 
        ("Therapy", range(1,8)),
    'THERA_R4': 
        ("FamiliaTheraLase", range(1,10)),
    'EASYL_R5': 
        ("Easy Laser", range(1,14)),
    'ELIB-R4':
        ("e-lib", range(1,9)),

    # vulcan e triplet novos (2023)
    'Vulcan_6-INSP-0583_rev.00.Omnia':
        ("Vulcan", range(1,17)),
    'Triplet_6-INSP-526_rev.02.Omnia':
        ("FamiliaTriplet", range(1,24)),

    'e-light_6-INSP-0548_rev05.Omnia':
        ("e-light", range(1,10)),

}
