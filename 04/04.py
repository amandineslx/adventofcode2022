INPUT_FILE = "04-input.txt"

class Team:
    def __init__(self, line_split):
        self.sections_one = line_split[0]
        self.sections_two = line_split[1]

    def to_string(self):
        return f"Team assignments: {self.sections_one},{self.sections_two}"

    def assignment_contains_other(self):
        min_max_one = self.sections_one.split('-')
        min_max_two = self.sections_two.split('-')
        min_one = int(min_max_one[0])
        max_one = int(min_max_one[1])
        min_two = int(min_max_two[0])
        max_two = int(min_max_two[1])
        return (min_one <= min_two and max_one >= max_two) or (min_two <= min_one and max_two >= max_one)

    def assignments_overlap(self):
        min_max_one = self.sections_one.split('-')
        min_max_two = self.sections_two.split('-')
        min_one = int(min_max_one[0])
        max_one = int(min_max_one[1])
        min_two = int(min_max_two[0])
        max_two = int(min_max_two[1])
        return (min_one >= min_two and min_one <= max_two) or (min_two >= min_one and min_two <= max_one) or (max_one >= min_two and max_one <= max_two) or (max_two >= min_one and max_two <= max_one)

def find_number_of_teams():
    number_of_teams = 0
    with open(INPUT_FILE) as f:
        for line in f.readlines():
            team = Team(line[:len(line)-1].split(','))
            print(team.to_string())
            # if team.assignment_contains_other():
            if team.assignments_overlap():
                print("Overlap")
                number_of_teams = number_of_teams + 1
    return number_of_teams

print(find_number_of_teams())
