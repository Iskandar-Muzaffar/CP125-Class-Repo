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
    def manage_roster(enrolled, drop_requests, waitlist):

        enrolled -= set(drop_requests)

    if len(enrolled) < 5:
        while len(enrolled) < 7 and waitlist:
            enrolled.add(waitlist.pop())

    return len(enrolled)


        