from flask import Flask, request, jsonify, render_template
import math

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/basic")
def basic_calculator():
    return render_template("basic.html")

@app.route("/scientific")
def scientific_calculator():
    return render_template("scientific.html")

@app.route("/area")
def area_calculator():
    return render_template("area.html")

@app.route("/converter")
def unit_converter():
    return render_template("converter.html")

@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.get_json()
    expression = data.get("expression", "")
    try:
        result = eval(expression)
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/calculate_scientific", methods=["POST"])
def calculate_scientific():
    data = request.get_json()
    expression = data.get("expression", "")
    try:
        # Replace common scientific functions
        expression = expression.replace("sin(", "math.sin(")
        expression = expression.replace("cos(", "math.cos(")
        expression = expression.replace("tan(", "math.tan(")
        expression = expression.replace("log(", "math.log(")
        expression = expression.replace("sqrt(", "math.sqrt(")
        expression = expression.replace("pi", str(math.pi))
        expression = expression.replace("e", str(math.e))
        
        result = eval(expression)
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/calculate_area", methods=["POST"])
def calculate_area():
    data = request.get_json()
    shape = data.get("shape", "")
    dimensions = data.get("dimensions", {})
    
    try:
        if shape == "rectangle":
            length = float(dimensions.get("length", 0))
            width = float(dimensions.get("width", 0))
            area = length * width
            return jsonify({"result": area, "unit": "square units"})
        
        elif shape == "circle":
            radius = float(dimensions.get("radius", 0))
            area = math.pi * radius * radius
            return jsonify({"result": area, "unit": "square units"})
        
        elif shape == "triangle":
            base = float(dimensions.get("base", 0))
            height = float(dimensions.get("height", 0))
            area = 0.5 * base * height
            return jsonify({"result": area, "unit": "square units"})
        
        elif shape == "square":
            side = float(dimensions.get("side", 0))
            area = side * side
            return jsonify({"result": area, "unit": "square units"})
        
        else:
            return jsonify({"error": "Invalid shape"}), 400
            
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/convert_unit", methods=["POST"])
def convert_unit():
    data = request.get_json()
    value = float(data.get("value", 0))
    from_unit = data.get("from_unit", "")
    to_unit = data.get("to_unit", "")
    unit_type = data.get("unit_type", "")
    
    try:
        # Length conversions
        if unit_type == "length":
            length_conversions = {
                "mm": 0.001, "cm": 0.01, "m": 1, "km": 1000,
                "in": 0.0254, "ft": 0.3048, "yd": 0.9144, "mi": 1609.34
            }
            meters = value * length_conversions.get(from_unit, 1)
            result = meters / length_conversions.get(to_unit, 1)
            return jsonify({"result": result})
        
        # Area conversions
        elif unit_type == "area":
            area_conversions = {
                "mm²": 0.000001, "cm²": 0.0001, "m²": 1, "km²": 1000000,
                "in²": 0.00064516, "ft²": 0.092903, "yd²": 0.836127, "ac": 4046.86
            }
            square_meters = value * area_conversions.get(from_unit, 1)
            result = square_meters / area_conversions.get(to_unit, 1)
            return jsonify({"result": result})
        
        # Weight conversions
        elif unit_type == "weight":
            weight_conversions = {
                "mg": 0.001, "g": 1, "kg": 1000, "lb": 453.592, "oz": 28.3495
            }
            grams = value * weight_conversions.get(from_unit, 1)
            result = grams / weight_conversions.get(to_unit, 1)
            return jsonify({"result": result})
        
        else:
            return jsonify({"error": "Invalid unit type"}), 400
            
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)
