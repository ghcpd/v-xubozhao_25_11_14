"""Demonstrate the intentionally buggy behavior described in the prompt."""

def buggy_score(age: int, credits: int) -> int:
    score = age + credits
    if age > 200:
        score = -1
    return score


def main() -> None:
    cases = [
        {
            "age": 20,
            "credits": 100,
            "expected": 20 * 2 + 100 // 10,
            "explanation": "Wrong formula ignores constraints",
        },
        {
            "age": -5,
            "credits": 200,
            "expected": "ValueError",
            "explanation": "Negative age is treated as valid",
        },
        {
            "age": 30,
            "credits": 9000,
            "expected": 30 * 2 + 9000 // 10,
            "explanation": "Credits are not bounded, so score blows up",
        },
    ]

    print("Demonstrating buggy score_user logic before the fix")
    for case in cases:
        computed = buggy_score(case["age"], case["credits"])
        print(
            f"Input age={case['age']}, credits={case['credits']} -> buggy output={computed}; expected={case['expected']} ({case['explanation']})"
        )


if __name__ == "__main__":
    main()
