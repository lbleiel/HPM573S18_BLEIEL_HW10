POP_SIZE = 2000     # cohort population size
SIM_LENGTH = 50   # length of simulation (years)
ALPHA = 0.05        # significance level for calculating confidence intervals
DELTA_T = 1         # years (length of time step, how frequently you look at the patient)
DISCOUNT = 0.03

PSA_ON = False

# transition matrix
TRANS_MATRIX = [
    [0.75,  0.15,   0.0,    0.1],   # Well
    [0,     0.0,    1.0,    0.0],   # Stroke
    [0,     0.25,   0.55,   0.2],   # Post-Stroke
    [0.0,   0.0,    0.0,    1.0],   # Dead
    ]

ANNUAL_STATE_COST = [
    0,          # Well (cost of anticoagulation)
    5000,       # Stroke
    200,        # Post-stroke + annual cost of anticoagulation
    0           # Dead
]

ANNUAL_STATE_UTILITY = [
    1,      # Well
    0.8865, # Stroke
    0.9,    # Post-Stroke
    0       # Dead
    ]

# annual treatment costs
notreatment_COST = 0
anticoagulation_COST = 2000

# anticoagulation relative risk in reducing stroke incidence and stroke death while in “Post-Stroke”
RR_STROKE = 0.65
# anticoagulation relative risk in increasing mortality due to bleeding is 1.05.
RR_BLEEDING = 1.05
TREATMENT_RR_CI = 0.65, 0.65

