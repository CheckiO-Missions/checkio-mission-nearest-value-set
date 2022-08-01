"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [{4, 7, 10, 11, 12, 17}, 9],
            "answer": 10
        },
        {
            "input": [{4, 7, 10, 11, 12, 17}, 8],
            "answer": 7
        },
        {
            "input": [{4, 8, 10, 11, 12, 17}, 9],
            "answer": 8
        },
        {
            "input": [{4, 9, 10, 11, 12, 17}, 9],
            "answer": 9
        },
        {
            "input": [{4, 7, 10, 11, 12, 17}, 0],
            "answer": 4
        },
        {
            "input": [{4, 7, 10, 11, 12, 17}, 100],
            "answer": 17
        },
        {
            "input": [{5, 10, 8, 12, 89, 100}, 7],
            "answer": 8
        },
        {
            "input": [{-1, 2, 3}, 0],
            "answer": -1
        },
        {
            "input": [{5}, 5],
            "answer": 5
        },
        {
            "input": [{5}, 7],
            "answer": 5
        }
    ],
    "Extra": [
        {
            "input": [{1,2,3,4,5,6,7}, 2],
            "answer": 2
        },
        {
            "input": [{1,3,4,5,6,7}, 2],
            "answer": 1
        },
        {
            "input": [{0,-2}, -1],
            "answer": -2
        },
        {
            "input": [{-6, -2, 4, 7, 12, 17}, -4],
            "answer": -6
        },
        {
            "input": [{1,2,3,4,5,6,7}, 20],
            "answer": 7
        }
    ]
}
