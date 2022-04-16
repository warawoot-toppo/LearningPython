questions = [
    '5 x 5 = ?', 
    '2 + 3 = ?  '
]

answers = ['25', '5']

q_and_a = list(zip(questions, answers))
print(q_and_a)

#cleaned_questions = list(map(lambda q: q.strip().capitalize(), questions))
#print(cleaned_questions)

cleaned_questions = [q.strip().capitalize() for q in questions]
print(cleaned_questions)

#filtered_questions = list(filter(lambda q: len(q) >= 6, cleaned_questions))
#print(filtered_questions)

filtered_questions = [q for q in cleaned_questions if len(q) >= 6]
print(filtered_questions)