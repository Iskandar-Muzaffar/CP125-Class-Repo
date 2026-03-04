# WRONG — list as key
# Run this to see the crash, then fix it using tuples

# CORRECT — tuple as key
config = {
    (192, 168, 1, 1): "Router"
}

menu = {"coffee": 5.00}

menu["coffee"] = 6.00         # Update existing
menu["latte"] = 7.50          # Add new

# Batch update
menu.update({"tea": 4.00, "juice": 3.00})

del menu["tea"]               # Remove (KeyError if missing)
removed = menu.pop("latte")   # Remove and capture the value
menu.clear()                  # Remove everything

print(menu)