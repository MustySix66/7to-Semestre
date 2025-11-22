from flask import Flask, render_template, request, jsonify
import sympy as sp
import numpy as np
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application

app = Flask(__name__, static_folder='static', static_url_path='')

# Transformaciones para parsing más flexible
transformations = standard_transformations + (implicit_multiplication_application,)

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        data = request.json
        function_str = data.get('function', '')
        variable_str = data.get('variable', 'x')
        lower_limit = data.get('lower_limit', None)
        upper_limit = data.get('upper_limit', None)
        
        # Parsear la función
        x = sp.Symbol(variable_str)
        function = parse_expr(function_str, local_dict={variable_str: x}, transformations=transformations)
        
        # Calcular la integral
        integral = sp.integrate(function, x)
        
        # Generar puntos para graficar
        x_vals = np.linspace(-10, 10, 200)
        
        # Evaluar la función original
        f_lambdified = sp.lambdify(x, function, modules=['numpy'])
        try:
            y_vals = f_lambdified(x_vals)
            # Filtrar valores infinitos o muy grandes
            y_vals = np.where(np.abs(y_vals) > 1e6, np.nan, y_vals)
            function_points = {
                'x': x_vals.tolist(),
                'y': y_vals.tolist()
            }
        except:
            function_points = None
        
        # Evaluar la integral
        integral_lambdified = sp.lambdify(x, integral, modules=['numpy'])
        try:
            y_integral_vals = integral_lambdified(x_vals)
            # Filtrar valores infinitos o muy grandes
            y_integral_vals = np.where(np.abs(y_integral_vals) > 1e6, np.nan, y_integral_vals)
            integral_points = {
                'x': x_vals.tolist(),
                'y': y_integral_vals.tolist()
            }
        except:
            integral_points = None
        
        # Calcular integral definida si hay límites
        definite_value = None
        area_points = None
        if lower_limit is not None and upper_limit is not None:
            try:
                lower = float(lower_limit)
                upper = float(upper_limit)
                definite_value = float(sp.integrate(function, (x, lower, upper)))
                
                # Puntos para el área sombreada
                x_area = np.linspace(lower, upper, 100)
                y_area = f_lambdified(x_area)
                y_area = np.where(np.abs(y_area) > 1e6, np.nan, y_area)
                area_points = {
                    'x': x_area.tolist(),
                    'y': y_area.tolist()
                }
            except Exception as e:
                pass
        
        response = {
            'success': True,
            'integral': sp.latex(integral),
            'integral_text': str(integral),
            'function_points': function_points,
            'integral_points': integral_points,
            'definite_value': definite_value,
            'area_points': area_points
        }
        
        return jsonify(response)
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
