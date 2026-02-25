def get_unique_attendees(attendance_logs):
    """Extract set of all unique attendee IDs."""
    all_attendees = []
    for attendee_id in attendance_logs:
        if attendee_id not in all_attendees:
            all_attendees.append(attendee_id)

    return all_attendees

def count_unique_events(attendance_logs, attendee_id):
    """Count how many unique events this attendee attended."""
    events_attended = []
    for att_id, event_name in attendance_logs:
        if att_id == attendee_id and event_name not in events_attended:
            events_attended.append(event_name)
            
    return events_attended
    

def filter_by_threshold(attendees, attendance_logs, min_events):
    """Return sorted list of attendees who attended >= min_events."""

    qualified = []
    
    for attendee_id in attendees:
        if count_unique_events(attendance_logs, attendee_id) >= min_events:
            qualified.append(attendee_id)

    return sorted(qualified)
    

def find_frequent_attendees(attendance_logs, min_events):
    """Find attendees who attended at least min_events unique events."""

    filter_by_threshold(attendees, attendance_logs, min_events)