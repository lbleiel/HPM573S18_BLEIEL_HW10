import ParameterClasses as P
import MarkovModel as MarkovCls
import SupportMarkovModel as SupportMarkov
import scr.SamplePathClasses as PathCls
import scr.FigureSupport as Figs

#### PROBLEM 1 ####


# create and cohort
cohort1 = MarkovCls.Cohort(
    id=0,
    therapy=P.Therapies.NONE)

simOutputs1 = cohort1.simulate()

cohort2 = MarkovCls.Cohort(
    id=1,
    therapy=P.Therapies.ANTICOAG
)

simOutputs2 = cohort2.simulate()

# graph survival curve
PathCls.graph_sample_path(
    sample_path=simOutputs1.get_survival_curve(),
    title='Survival curve',
    x_label='Simulation time step',
    y_label='Number of alive patients'
    )

# graph histogram of survival times
Figs.graph_histogram(
    data=simOutputs1.get_survival_times(),
    title='Survival times of patients with Stroke',
    x_label='Survival time (years)',
    y_label='Counts',
    bin_width=1
)


# graph histogram of number of strokes
Figs.graph_histogram(
    data=simOutputs1.get_if_developed_stroke(),
    title='Number of Strokes per Patient',
    x_label='Strokes',
    y_label='Counts',
    bin_width=1
)
print("PROBLEM 1:")
# print outcomes (means and CIs)
SupportMarkov.print_outcomes(simOutputs1, 'No treatment:')

# graph survival curve
PathCls.graph_sample_path(
    sample_path=simOutputs2.get_survival_curve(),
    title='Survival curve',
    x_label='Simulation time step',
    y_label='Number of alive patients'
    )

# graph histogram of survival times
Figs.graph_histogram(
    data=simOutputs2.get_survival_times(),
    title='Survival times of patients with Stroke',
    x_label='Survival time (years)',
    y_label='Counts',
    bin_width=1
)


# graph histogram of number of strokes
Figs.graph_histogram(
    data=simOutputs2.get_if_developed_stroke(),
    title='Number of Strokes per Patient',
    x_label='Strokes',
    y_label='Counts',
    bin_width=1
)

# print outcomes (means and CIs)
SupportMarkov.print_outcomes(simOutputs2, 'Anticoagulation treatment:')

#-----------------------------------------------------------------------------------#
#### PROBLEM 2 ####
print("PROBLEM 2:")
SupportMarkov.print_comparative_outcomes(simOutputs1, simOutputs2)

#-----------------------------------------------------------------------------------#
#### PROBLEM 3 ####
print("PROBLEMS 3 and 4:")
SupportMarkov.report_CEA_CBA(simOutputs1, simOutputs2)
print('Answers shown in SciView')
print('I would recommend adopting this willingness-to-pay around $20,000')


