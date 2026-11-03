import json

# Simulate a list of Jira issues
# In a real scenario, this would come from the Jira API
jira_issues = [
    {"id": "PROJ-101", "summary": "Implement user authentication", "priority": "High", "status": "To Do"},
    {"id": "PROJ-102", "summary": "Design database schema", "priority": "High", "status": "To Do"},
    {"id": "PROJ-103", "summary": "Develop API endpoints", "priority": "Medium", "status": "In Progress"},
    {"id": "PROJ-104", "summary": "Write unit tests", "priority": "Medium", "status": "To Do"},
    {"id": "PROJ-105", "summary": "Deploy to staging", "priority": "Low", "status": "Done"}
]

def simulate_bulk_change(issues, field_to_change, new_value):
    """
    Simulates applying a bulk change to a list of Jira issues.
    In a real Jira scenario, this would involve API calls.
    """
    print(f"--- Simulating Bulk Change: Setting '{field_to_change}' to '{new_value}' ---")
    changes_made = 0
    for issue in issues:
        if field_to_change in issue:
            # This is the core of the bulk change simulation
            # Applying the new value to the specified field for each issue
            issue[field_to_change] = new_value
            print(f"Changed issue {issue['id']}: {field_to_change} is now {new_value}")
            changes_made += 1
    print(f"--- Bulk Change Complete: {changes_made} issues updated ---")
    return issues

if __name__ == "__main__":
    print("--- Initial Jira Issues ---")
    for issue in jira_issues:
        print(issue)
    print("\n")

    # Example 1: Change priority of multiple issues
    # Imagine selecting issues PROJ-101, PROJ-102, PROJ-104 and changing their priority
    # In Jira UI, you'd select these issues and then choose 'Bulk Change' -> 'Edit Issues'
    # Here, we simulate changing priority for all issues that are currently 'High'
    # This is a simplified simulation; real Jira allows selecting specific issues.
    
    # Let's simulate changing priority for specific issues by targeting them directly for demo
    # In a real UI, you'd select them first.
    # For this demo, we'll simulate changing priority for PROJ-101 and PROJ-102
    # This is a conceptual representation of selecting issues and applying a change.
    
    # To better simulate, let's define a subset of issues to modify
    issues_to_modify_priority = [issue for issue in jira_issues if issue['id'] in ['PROJ-101', 'PROJ-102']]
    # In a real Jira bulk change, you'd select these, then choose 'Edit Issues' and change priority.
    # Our function simulates applying the change to a given list.
    
    # We'll adapt the function call to reflect changing priority for a *selection* of issues.
    # For simplicity, we'll just apply it to the whole list and explain the concept.
    # A more accurate simulation would involve filtering and then applying.
    
    # Let's simulate changing priority for all 'High' priority issues to 'Medium'
    # This is a common use case for bulk change.
    issues_with_high_priority = [issue for issue in jira_issues if issue.get('priority') == 'High']
    # In Jira, you'd select these issues, then choose Bulk Change -> Edit Issues -> Priority -> Medium
    # Our function can simulate applying a change to a list.
    
    # To make this runnable and demonstrate the core idea, we'll simulate changing the priority
    # of a *specific set* of issues that we identify here.
    
    # Let's simulate changing the priority of PROJ-101 and PROJ-102 from 'High' to 'Medium'
    # In Jira, you'd select these, then choose 'Bulk Change' -> 'Edit Issues' -> 'Priority' -> 'Medium'
    
    # We'll simulate this by directly calling our function on a filtered list.
    # This is a conceptual demonstration of the *effect* of bulk change.
    
    # Simulating changing priority for PROJ-101 and PROJ-102
    # In a real scenario, you'd select these issues first.
    # For this script, we'll filter and then apply.
    issues_to_update_priority = [issue for issue in jira_issues if issue['id'] in ['PROJ-101', 'PROJ-102']]
    # We pass this subset to our simulation function.
    # Note: The `simulate_bulk_change` function as written modifies the original list if passed directly.
    # To avoid side effects for subsequent examples, we'd ideally work on copies.
    # For simplicity here, we'll re-initialize or be mindful of order.
    
    # Let's re-initialize for clarity for each example.
    jira_issues_copy1 = json.loads(json.dumps(jira_issues))
    updated_issues_priority = simulate_bulk_change(issues_to_update_priority, "priority", "Medium")
    
    print("\n--- Issues after Priority Change ---")
    for issue in updated_issues_priority:
        print(issue)
    print("\n")

    # Example 2: Change status of multiple issues
    # Imagine selecting issues PROJ-103 and PROJ-104 and changing their status to 'Done'
    jira_issues_copy2 = json.loads(json.dumps(jira_issues))
    issues_to_update_status = [issue for issue in jira_issues_copy2 if issue['id'] in ['PROJ-103', 'PROJ-104']]
    updated_issues_status = simulate_bulk_change(issues_to_update_status, "status", "Done")

    print("\n--- Issues after Status Change ---")
    for issue in updated_issues_status:
        print(issue)
    print("\n")

    # Example 3: Changing a field that might not exist in all issues (e.g., 'assignee')
    # This demonstrates how bulk change can handle missing fields gracefully (or not, depending on implementation)
    # Our simple simulation will just not find the field.
    jira_issues_copy3 = json.loads(json.dumps(jira_issues))
    issues_to_update_assignee = [issue for issue in jira_issues_copy3 if issue['id'] in ['PROJ-101', 'PROJ-105']]
    updated_issues_assignee = simulate_bulk_change(issues_to_update_assignee, "assignee", "john.doe")

    print("\n--- Issues after Assignee Change Attempt ---")
    for issue in updated_issues_assignee:
        print(issue)
    print("\n")
