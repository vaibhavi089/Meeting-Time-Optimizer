from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime, timedelta

app = Flask(__name__)
CORS(app)


def find_optimal_time(availabilities):
    time_slots = {}

    
    for availability in availabilities:
        try:
            start_time = datetime.strptime(availability["start"], "%H:%M")
            end_time = datetime.strptime(availability["end"], "%H:%M")
        except (KeyError, ValueError):
            raise ValueError("Invalid availability format. Use 'start' and 'end' in HH:MM format.")
        
        while start_time < end_time:
            slot = start_time.strftime("%H:%M")
            time_slots[slot] = time_slots.get(slot, 0) + 1
            start_time += timedelta(minutes=30)  

    if not time_slots:
        raise ValueError("No valid time slots found.")
    
    
    optimal_time = max(time_slots, key=time_slots.get)
    return optimal_time

@app.route("/api/optimal_time", methods=["POST"])
def get_optimal_time():
    data = request.json
    availabilities = data.get("availabilities", [])
    
    if not availabilities:
        return jsonify({"error": "No availabilities provided"}), 400

    try:
        optimal_time = find_optimal_time(availabilities)
        return jsonify({"optimal_time": optimal_time}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred: " + str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
