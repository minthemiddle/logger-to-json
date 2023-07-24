import sqlite3
import json

# Connect to the SQLite database
conn = sqlite3.connect('logger.sqlite')
cursor = conn.cursor()

# Execute the query and fetch all meditation sittings
cursor.execute('SELECT id, created_at, value, comment FROM logs WHERE key = "Meditation";')
meditation_sittings = cursor.fetchall()

# Close the database connection
conn.close()

# Convert the data to the desired JSON format
output_data = []
for sitting in meditation_sittings:
    output_data.append({
        "id": sitting[0],
        "timestamp": sitting[1] + "Z",  # Add "Z" to indicate UTC time
        "duration": sitting[2],
        "type": "Sitting",
        "comment": sitting[3] if sitting[3] else ""
    })

# Export the data to a JSON file
with open('meditation_sittings.json', 'w') as file:
    json.dump(output_data, file, indent=2)

print("Export completed. Check 'meditation_sittings.json' in the current directory.")
