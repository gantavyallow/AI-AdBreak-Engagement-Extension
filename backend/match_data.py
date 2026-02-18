# Simulated ball-by-ball data
# Each over has 6 legal balls

MATCH_OVERS = [
    {
        "over": 1,
        "balls": [0, 1, 0, 1, 0, 1],
        "wicket": False,
        "rr_before": 7.2,
        "rr_after": 7.0
    },
    {
        "over": 2,
        "balls": [4, 1, 0, 4, 1, 0],
        "wicket": False,
        "rr_before": 7.0,
        "rr_after": 7.8
    },
    {
        "over": 3,
        "balls": [0, 0, 0, 1, 0, 0],
        "wicket": False,
        "rr_before": 7.8,
        "rr_after": 7.3
    },
    {
        "over": 4,
        "balls": [0, 0, 0, 1, 0, "W"],
        "wicket": True,
        "rr_before": 7.3,
        "rr_after": 6.9
    },
    {
        "over": 5,
        "balls": [6, 4, 1, 4, 0, 1],
        "wicket": False,
        "rr_before": 6.9,
        "rr_after": 8.2
    }
]
