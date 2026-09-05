class School:
    avg_pass_rate = 0.8
    avg_fail_rate  = 0.2

    def __init__(self,strength,pass_rate,failure_rate):

        self.strength = strength
        self.pass_rate = pass_rate
        self.failure_rate = failure_rate

    def overall_strength(self,grade1,grade2,grade3,grade4):
         overall_strength = (grade1_strength + grade2_strength + grade3_strength + grade4_strength)
         return overall_strength

    def calculate_overall_pass_rate(self,overall_strength,avg_pass_rate):
        calculate_overall_pass_rate = (overall_strength * avg_pass_rate)
        return calculate_overall_pass_rate



    def calculate_failure_rate(self,grade1,grade2,grade3,grade4):
        calculate_failure_rate = self.overall_strength * self.fail_rate

grade1 = School(56,0.7,0.2)
grade2 = School(60,0.5,0.2)
grade3 = School(20,0.6,0.1)
grade4 = School(86,0.5,0.3)

def overall_pass_rate():
    if overall_pass_rate < overal+







