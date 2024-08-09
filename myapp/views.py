from django.http import JsonResponse
from django.views.decorators.http import require_GET
from sympy import symbols, solve, integrate, sympify, SympifyError

@require_GET
def solve_equation(request):
    try:
        equation = request.GET.get('equation', '')
        if not equation:
            return JsonResponse({'error': 'No equation provided.'}, status=400)

        # Parse the equation
        x = symbols('x')
        lhs, rhs = equation.split('=')
        expr = sympify(lhs) - sympify(rhs)

        # Solve the equation
        solution = solve(expr)

        return JsonResponse({'operation': 'equation solving', 'equation': equation, 'solution': str(solution)})
    except (SympifyError, ValueError) as e:
        return JsonResponse({'error': f'Invalid input: {str(e)}'}, status=400)

@require_GET
def symbolic_integration(request):
    try:
        expression = request.GET.get('expression', '')
        variable = request.GET.get('variable', 'x')
        if not expression:
            return JsonResponse({'error': 'No expression provided.'}, status=400)

        # Parse the expression and perform integration
        x = symbols(variable)
        expr = sympify(expression)
        result = integrate(expr, x)

        return JsonResponse({'operation': 'integration', 'expression': expression, 'variable': variable, 'result': str(result)})
    except (SympifyError, ValueError) as e:
        return JsonResponse({'error': f'Invalid input: {str(e)}'}, status=400)

@require_GET
def add(request):
    try:
        a = float(request.GET.get('a', 0))
        b = float(request.GET.get('b', 0))
        result = a + b
        return JsonResponse({'operation': 'addition', 'result': result})
    except ValueError:
        return JsonResponse({'error': 'Invalid input. Please provide numeric values.'}, status=400)

@require_GET
def subtract(request):
    try:
        a = float(request.GET.get('a', 0))
        b = float(request.GET.get('b', 0))
        result = a - b
        return JsonResponse({'operation': 'subtraction', 'result': result})
    except ValueError:
        return JsonResponse({'error': 'Invalid input. Please provide numeric values.'}, status=400)

@require_GET
def multiply(request):
    try:
        a = float(request.GET.get('a', 1))
        b = float(request.GET.get('b', 1))
        result = a * b
        return JsonResponse({'operation': 'multiplication', 'result': result})
    except ValueError:
        return JsonResponse({'error': 'Invalid input. Please provide numeric values.'}, status=400)

@require_GET
def divide(request):
    try:
        a = float(request.GET.get('a', 0))
        b = float(request.GET.get('b', 1))
        if b == 0:
            return JsonResponse({'error': 'Division by zero is not allowed.'}, status=400)
        result = a / b
        return JsonResponse({'operation': 'division', 'result': result})
    except ValueError:
        return JsonResponse({'error': 'Invalid input. Please provide numeric values.'}, status=400)