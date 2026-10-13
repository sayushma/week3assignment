# Lesson 3 Individual Assignment - In-Memory Inventory Management Tool
# Uses only: lists, dictionaries, if-elif-else, for loops, .get(), .append(), .items()

# ---------- Task 1: Data setup ----------
inventory = {"Widget": 10, "Gadget": 5, "Sensor": 0, "Cable": 15}

order_queue = [
    ["Widget", 3],
    ["Sensor", 2],
    ["Gadget", 7],
    ["Cable", 15],
    ["Battery", 4],
    ["Widget", 6],
    ["Widget", 5],
    ["Cable", 1],
]

# Tracking variables for analytics
fully_fulfilled_count = 0
unfulfilled_items = []   # each entry: [item, quantity short, reason]

print("=== PROCESSING ORDERS ===")
print("Starting inventory:", inventory)
print()

# ---------- Task 2: Order processing ----------
for order in order_queue:
    item = order[0]
    requested = order[1]
    stock = inventory.get(item)          # returns None if the key does not exist

    if stock is None:
        # Invalid item: the key is not in the inventory dictionary
        print("ALERT: '" + item + "' does not exist in inventory. Order for " + str(requested) + " cannot be filled.")
        unfulfilled_items.append([item, requested, "Item not found"])
    elif stock == 0:
        # Out of stock
        print("ALERT: '" + item + "' is out of stock. Order for " + str(requested) + " cannot be filled.")
        unfulfilled_items.append([item, requested, "Out of stock"])
    elif stock >= requested:
        # Full fulfillment
        inventory[item] = stock - requested
        fully_fulfilled_count += 1
        print("SUCCESS: Fulfilled " + str(requested) + " x " + item + ". Remaining stock: " + str(inventory[item]))
    else:
        # Partial fulfillment: stock > 0 but less than requested
        remainder = requested - stock
        print("PARTIAL: Only " + str(stock) + " of " + str(requested) + " x " + item + " available. Shipped " + str(stock) + ", short by " + str(remainder) + ".")
        inventory[item] = 0
        unfulfilled_items.append([item, remainder, "Partial fulfillment"])

# ---------- Task 3: Summary report ----------
print()
print("=== END-OF-BATCH SUMMARY ===")
print("1. Final inventory:", inventory)
print("2. Fully fulfilled orders:", fully_fulfilled_count)
print("3. Items/quantities not fully supplied:")
for entry in unfulfilled_items:
    print("   - " + entry[0] + ": short by " + str(entry[1]) + " (" + entry[2] + ")")
