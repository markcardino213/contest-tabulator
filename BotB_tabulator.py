# Define constants
CRITERIA_WEIGHTS = {'musicality': 0.35, 'performance': 0.2, 'voice_quality': 0.2, 'song_choice': 0.15, 'audience_impact': 0.1}
NUM_JUDGES = 3
NUM_CONTESTANTS = 8

# Initialize scores dictionary
scores = {}
print("\n\t\t\t\t     **BATTLE OF THE BANDS**")
print("\t\t\t\t\t    (tabulator)")
print("\n\t\t\t\t\tCriteria for Judging")
print("\n'musicality': 35%, 'performance': 20%, 'voice quality': 20%, 'song choice': 15%, 'audience impact': 10%")
print("\n\t\t\t\t\t   press q to quit")
while True:
    # Get scores from judges
    for i in range(NUM_CONTESTANTS):
        scores[i+1] = {'musicality': 0, 'performance': 0, 'voice_quality': 0, 'song_choice': 0, 'audience_impact': 0}
        print(f"\nContestant {i+1}")
        for j in range(NUM_JUDGES):
            print(f"\nJudge {j+1}")
            for criteria in CRITERIA_WEIGHTS:
                score = input(f"\t{criteria} score: ")
                if score == 'q':
                    print("\tThank you for using!")
                    quit()
                while not score.isdigit() or int(score) < 0 or int(score) > 10:
                    print("\t*Only accepts Integer inputs or scores from 0-10*")
                    score = input(f"\t{criteria} score: ")
                    if score == 'q':
                        print("\tThank you for using!")
                        quit()
                scores[i+1][criteria] += int(score)

    # Calculate total scores
    for i in range(NUM_CONTESTANTS):
        total_score = 0
        for criteria, weight in CRITERIA_WEIGHTS.items():
            total_score += scores[i+1][criteria] * weight
        scores[i+1]['total'] = total_score

    # Sort scores in descending order
    sorted_scores = sorted(scores.items(), key=lambda x: x[1]['total'], reverse=True)

    # Print results
    print("\nResults:")
    for i, (contestant, score) in enumerate(sorted_scores):
        print(f"\t{i+1}. Contestant {contestant} - Total score: {score['total']}")
    

    # Ask user if they want to run the program again
    run_again = input("Do you want to run the program again? (y/n): ")
    while run_again.lower() not in ['y', 'n']:
        run_again = input("Invalid input. Do you want to run the program again? (y/n): ")
    if run_again.lower() == 'n':
         break
         
print("\n\tThank you for using!")