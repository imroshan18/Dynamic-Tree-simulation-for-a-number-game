class QuestionNode:
    def __init__(self, question=None, yes=None, no=None, result=None):
        self.question = question
        self.yes = yes
        self.no = no
        self.result = result


def build_tree():
    # Leaf nodes
    n1 = QuestionNode(result=1)
    n2 = QuestionNode(result=2)
    n3 = QuestionNode(result=3)
    n4 = QuestionNode(result=4)
    n5 = QuestionNode(result=5)
    n6 = QuestionNode(result=6)
    n7 = QuestionNode(result=7)
    n8 = QuestionNode(result=8)
    n9 = QuestionNode(result=9)
    n10 = QuestionNode(result=10)

    # Level 3
    q_even_small = QuestionNode("Is it even?", yes=n2, no=n1)
    q_even_3_4 = QuestionNode("Is it even?", yes=n4, no=n3)
    q_even_6_7 = QuestionNode("Is it even?", yes=n6, no=n7)
    q_even_9_10 = QuestionNode("Is it even?", yes=n10, no=n9)

    # Level 2
    q_above3 = QuestionNode("Is it greater than 3?", yes=q_even_3_4, no=q_even_small)
    q_above7 = QuestionNode("Is it greater than 7?", yes=q_even_9_10, no=q_even_6_7)

    # Root
    root = QuestionNode("Is it greater than 5?", yes=q_above7, no=q_above3)

    return root