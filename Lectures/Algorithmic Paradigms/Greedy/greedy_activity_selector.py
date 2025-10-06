def recursive_activity_selector(s, f, i, n):
    """
    Recursive Activity Selector
    s: list of start times
    f: list of finish times (assumed sorted in non-decreasing order)
    i: index of the last selected activity
    n: total number of activities
    """
    m = i + 1
    # Find the next activity that starts after activity i finishes
    while m <= n and s[m] < f[i]:
        m += 1
    
    if m <= n:
        return [m] + recursive_activity_selector(s, f, m, n)
    else:
        return []


# Example usage
if __name__ == "__main__":
    # Example activities (including dummy 0 at index 0)
    s = [0, 1, 3, 0, 5, 8, 5]   # start times
    f = [0, 2, 4, 6, 7, 9, 9]   # finish times
    
    n = len(s) - 1
    selected = recursive_activity_selector(s, f, 0, n)
    
    print("Selected activities:", selected)
