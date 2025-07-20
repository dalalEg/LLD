class StackOverflowSystem:
    users = {}
    questions = {}
    answers = {}
    next_question_id = 1
    next_answer_id = 1

    @staticmethod
    def create_user(name):
        StackOverflowSystem.users[name] = {
            'name': name,
            'reputation': 0,
            'questions': [],
            'answers': []
        }
        return StackOverflowSystem.users[name]

    @staticmethod
    def ask_question(username, title, body, tags):
        qid = StackOverflowSystem.next_question_id
        StackOverflowSystem.next_question_id += 1
        question = {
            'id': qid,
            'title': title,
            'body': body,
            'author': username,
            'tags': list(set(tags)),
            'votes': 0,
            'comments': [],
            'answers': [],
            'accepted': None
        }
        StackOverflowSystem.questions[qid] = question
        StackOverflowSystem.users[username]['questions'].append(qid)
        return question

    @staticmethod
    def answer_question(username, question_id, body):
        aid = StackOverflowSystem.next_answer_id
        StackOverflowSystem.next_answer_id += 1
        answer = {
            'id': aid,
            'body': body,
            'author': username,
            'votes': 0,
            'comments': [],
            'accepted': False
        }
        StackOverflowSystem.answers[aid] = answer
        StackOverflowSystem.questions[question_id]['answers'].append(aid)
        StackOverflowSystem.users[username]['answers'].append(aid)
        return answer

    @staticmethod
    def vote_answer(voter, answer_id, direction):
        answer = StackOverflowSystem.answers[answer_id]
        if voter == answer['author']:
            print("Self-voting is not allowed.")
            return
        if direction == 'upvote':
            answer['votes'] += 1
            StackOverflowSystem.users[answer['author']]['reputation'] += 10
        elif direction == 'downvote':
            answer['votes'] -= 1
            StackOverflowSystem.users[answer['author']]['reputation'] -= 2

    @staticmethod
    def vote_question(voter, question_id, direction):
        question = StackOverflowSystem.questions[question_id]
        if voter == question['author']:
            print("Self-voting is not allowed.")
            return
        if direction == 'upvote':
            question['votes'] += 1
            StackOverflowSystem.users[question['author']]['reputation'] += 5
        elif direction == 'downvote':
            question['votes'] -= 1
            StackOverflowSystem.users[question['author']]['reputation'] -= 2

    @staticmethod
    def accept_answer(username, question_id, answer_id):
        question = StackOverflowSystem.questions[question_id]
        if question['author'] != username:
            print("Only the question author can accept an answer.")
            return
        prev = question['accepted']
        if prev:
            StackOverflowSystem.answers[prev]['accepted'] = False
        question['accepted'] = answer_id
        StackOverflowSystem.answers[answer_id]['accepted'] = True

    @staticmethod
    def comment_on_answer(username, answer_id, comment):
        StackOverflowSystem.answers[answer_id]['comments'].append((username, comment))

    @staticmethod
    def search_questions_by_tag(tag):
        print(f"Search Results for '{tag}':")
        for q in StackOverflowSystem.questions.values():
            if tag in q['tags']:
                print(f"- {q['title']}")

    @staticmethod
    def print_question(qid):
        q = StackOverflowSystem.questions[qid]
        print(f"\nQuestion: {q['title']}\nAuthor: {q['author']}\nTags: {', '.join(q['tags'])}\nVotes: {q['votes']}\nComments: {len(q['comments'])}\nAnswers:")
        for aid in q['answers']:
            a = StackOverflowSystem.answers[aid]
            print(f" - By {a['author']} | Votes: {a['votes']} | Accepted: {a['accepted']} | Comments: {len(a['comments'])}")

    @staticmethod
    def print_user_reputations():
        print("\nUser Reputations:")
        for user in StackOverflowSystem.users.values():
            print(f"{user['name']}: {user['reputation']}")

    @staticmethod
    def print_questions_by_user(username):
        print(f"\nQuestions by {username}:")
        for qid in StackOverflowSystem.users[username]['questions']:
            print(StackOverflowSystem.questions[qid]['title'])

    @staticmethod
    def run():
        alice = StackOverflowSystem.create_user("Alice")
        bob = StackOverflowSystem.create_user("Bob")
        carol = StackOverflowSystem.create_user("Carol")
        dave = StackOverflowSystem.create_user("Dave")

        q1 = StackOverflowSystem.ask_question("Alice", "How to reverse a binary tree?", "Use recursion or iteration", ["binary-tree", "tree", "recursion", "tree", "recursion"])

        a1 = StackOverflowSystem.answer_question("Carol", q1['id'], "Use post-order traversal")
        a2 = StackOverflowSystem.answer_question("Bob", q1['id'], "Iterative solution is better")
        a3 = StackOverflowSystem.answer_question("Alice", q1['id'], "Here's my recursive solution")

        StackOverflowSystem.vote_answer("Bob", a2['id'], "upvote")
        StackOverflowSystem.vote_answer("Carol", a2['id'], "upvote")
        StackOverflowSystem.accept_answer("Alice", q1['id'], a1['id'])
        StackOverflowSystem.accept_answer("Alice", q1['id'], a2['id'])

        StackOverflowSystem.comment_on_answer("Alice", a2['id'], "Why iterative?")
        StackOverflowSystem.comment_on_answer("Dave", a2['id'], "Agreed, iterative is safer.")
        StackOverflowSystem.comment_on_answer("Carol", a2['id'], "Nice explanation!")
        StackOverflowSystem.comment_on_answer("Alice", a3['id'], "I tested this on LeetCode")

        q2 = StackOverflowSystem.ask_question("Dave", "How to write a thread-safe queue?", "Need it in C++", ["concurrency", "multithreading", "cpp"])

        StackOverflowSystem.vote_question("Dave", q1['id'], "upvote")

        StackOverflowSystem.search_questions_by_tag("kubernetes")
        StackOverflowSystem.search_questions_by_tag("tree")

        StackOverflowSystem.print_questions_by_user("Bob")

        StackOverflowSystem.print_question(q1['id'])
        StackOverflowSystem.print_question(q2['id'])
        StackOverflowSystem.print_user_reputations()


# Run all scenarios
StackOverflowSystem.run()