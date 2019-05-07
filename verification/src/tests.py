"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": ["A simple string"],
            "answer": False
        },
        {
            "input": ["this string has a key"],
            "answer": True
        },
        {
            "input": ["this string has a better KEY"],
            "answer": True
        }
    ],
    "Extra": [
        {
            "input": ["every ke inside key"],
            "answer": True
        },
        {
            "input": ["it is not a k e y"],
            "answer": False
        },
        {
            "input": ["Weird KeY"],
            "answer": True
        }
    ]
}
