import minimal_validator_file as mvf

def calc_runs(events):
    runs_per_event = {}
    tot_runs = 0
    for event in events:
        event_runs = 0

        if "Runner Batter" in event:
            if event["Runner Batter"].get("Runner Result Base", None) == 4:
                event_runs += 1
                tot_runs += 1
        if "Runner 1B" in event:
            if event["Runner 1B"].get("Runner Result Base", None) == 4:
                event_runs += 1
                tot_runs += 1
        if "Runner 2B" in event:
            if event["Runner 2B"].get("Runner Result Base", None) == 4:
                event_runs += 1
                tot_runs += 1
        if "Runner 3B" in event:
            if event["Runner 3B"].get("Runner Result Base", None) == 4:
                event_runs += 1
                tot_runs += 1
        runs_per_event[event["Event Num"]] = {}
        runs_per_event[event["Event Num"]] = event_runs
    print(runs_per_event)
    print(tot_runs)

calc_runs(mvf.events)