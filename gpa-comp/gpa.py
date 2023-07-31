"""
A helper script to compute the Grade Point Avarage
"""

import argparse

parser = argparse.ArgumentParser(
    prog="gpa", description="A simple GPA Computing Script. This script computes GPA of tertiary modules loaded from a text file.",
    
)

parser.add_argument("-f", "--file", help="""This specifies path to the text file being loaded.
                    The sample file format is as follows:
                    Module-Name,Credits,Final-Mark, i.e.,
                    Module-C,12,76""", required=True)

args = parser.parse_args()

if __name__ == "__main__":
    print("GPA Computing...")

    marks = []
    credits = 0

    with open(args.file) as _marks:
        _all_marks = [x.strip('\n') for x in _marks.readlines()]

    
    compute = len(_all_marks) != 0
    if not compute:
        print("Could not load data from the provided file.")
    else:
        for mark in _all_marks:
            _mark = mark.split(',')

            if len(_mark) != 3:
                print("The input file is expected to have the following format: \nModule-Name,Credits,Final-Mark")
                exit(1)

            credits += int(_mark[1])
            _mark[1] = int(_mark[1]) * int(_mark.pop())


            marks.append(_mark)
        
        average = sum(list(map(lambda mark: mark[1], marks))) / credits

        print("\nModule Final-Mark-X-Credits")
        for _mark in marks:
            print(f"{_mark[0]:<8} {_mark[1]:>10}")

        print(f"\nSum-Final-Marks-Credits: {average * credits:.0f}, Credits-Sum: {credits}")
        print("\ngpa = Sum(Credits * Final-Mark) / Sum-Of-Credits")
        print(f"gpa = {average:.2f}%\n\nGPA Computed...")
