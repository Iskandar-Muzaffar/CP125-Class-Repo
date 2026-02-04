def manage_roster(enrolled, drop_requests, waitlist):
    """
    Processes student drop requests and adds from waitlist if needed.
    
    Args:
        enrolled: Set of currently enrolled student names
        drop_requests: List of student names requesting to drop
        waitlist: Set of students on the waitlist
    
    Returns:
        int: Count of final enrolled students
    """
    enrollment = set(enrolled)
    drop = set(drop_requests)
    waiting = set(waitlist)

    student_drop = enrollment ^ drop

    for student in range (7-len(student_drop)):
        if waiting <=
        student_drop.add(student)

    return student_drop
