def study_schedule(permanence_period, target_time):
    """Returns the students that were still studying at given time"""
    if target_time is None:
        return None

    counter = 0

    for clock_in, clock_out in permanence_period:
        if not isinstance(clock_in, int) or not isinstance(clock_out, int):
            return None

        if int(clock_in) <= target_time and int(clock_out) >= target_time:
            counter += 1

    return counter
