// Elementos del DOM
const functionInput = document.getElementById('function-input');
const variableInput = document.getElementById('variable-input');
const lowerLimitInput = document.getElementById('lower-limit');
const upperLimitInput = document.getElementById('upper-limit');
const calculateBtn = document.getElementById('calculate-btn');
const clearBtn = document.getElementById('clear-btn');
const loading = document.getElementById('loading');
const errorMessage = document.getElementById('error-message');
const results = document.getElementById('results');
const emptyState = document.getElementById('empty-state');
const integralResult = document.getElementById('integral-result');
const definiteResult = document.getElementById('definite-result');
const definiteValue = document.getElementById('definite-value');
const plotContainer = document.getElementById('plot');

// Variable para debouncing
let debounceTimer;

// Event Listeners
functionInput.addEventListener('input', debounceCalculate);
variableInput.addEventListener('input', debounceCalculate);
lowerLimitInput.addEventListener('input', debounceCalculate);
upperLimitInput.addEventListener('input', debounceCalculate);
calculateBtn.addEventListener('click', calculate);
clearBtn.addEventListener('click', clearAll);

// Ejemplos
document.querySelectorAll('.example-btn').forEach(btn => {
    btn.addEventListener('click', () => {
        functionInput.value = btn.dataset.function;
        calculate();
    });
});

// Debouncing para actualización en tiempo real
function debounceCalculate() {
    clearTimeout(debounceTimer);
    debounceTimer = setTimeout(() => {
        if (functionInput.value.trim()) {
            calculate();
        }
    }, 500);
}

// Función principal de cálculo
async function calculate() {
    const functionStr = functionInput.value.trim();

    if (!functionStr) {
        showEmptyState();
        return;
    }

    showLoading();

    const data = {
        function: functionStr,
        variable: variableInput.value || 'x',
        lower_limit: lowerLimitInput.value || null,
        upper_limit: upperLimitInput.value || null
    };

    try {
        const response = await fetch('/calculate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });

        const result = await response.json();

        if (result.success) {
            displayResults(result);
            plotGraph(result);
        } else {
            showError(result.error);
        }
    } catch (error) {
        showError('Error de conexión: ' + error.message);
    }
}

// Mostrar resultados
function displayResults(result) {
    hideLoading();
    hideError();
    hideEmptyState();

    // Mostrar integral
    integralResult.textContent = result.integral_text;

    // Mostrar valor definido si existe
    if (result.definite_value !== null) {
        definiteValue.textContent = result.definite_value.toFixed(6);
        definiteResult.classList.remove('hidden');
    } else {
        definiteResult.classList.add('hidden');
    }

    results.classList.remove('hidden');
}

// Graficar con Plotly
function plotGraph(result) {
    const traces = [];

    // Función original
    if (result.function_points) {
        traces.push({
            x: result.function_points.x,
            y: result.function_points.y,
            type: 'scatter',
            mode: 'lines',
            name: 'f(x)',
            line: {
                color: '#4facfe',
                width: 3
            }
        });
    }

    // Integral
    if (result.integral_points) {
        traces.push({
            x: result.integral_points.x,
            y: result.integral_points.y,
            type: 'scatter',
            mode: 'lines',
            name: '∫f(x)dx',
            line: {
                color: '#00f2fe',
                width: 3,
                dash: 'dash'
            }
        });
    }

    // Área sombreada para integral definida
    if (result.area_points) {
        traces.push({
            x: result.area_points.x,
            y: result.area_points.y,
            fill: 'tozeroy',
            type: 'scatter',
            mode: 'lines',
            name: 'Área',
            fillcolor: 'rgba(102, 126, 234, 0.2)',
            line: {
                color: '#667eea',
                width: 2
            }
        });
    }

    const layout = {
        paper_bgcolor: 'rgba(0,0,0,0)',
        plot_bgcolor: 'rgba(255,255,255,0.02)',
        font: {
            family: 'Inter, sans-serif',
            color: '#a0a8d4'
        },
        xaxis: {
            title: variableInput.value || 'x',
            gridcolor: 'rgba(255,255,255,0.1)',
            zerolinecolor: 'rgba(255,255,255,0.2)'
        },
        yaxis: {
            title: 'y',
            gridcolor: 'rgba(255,255,255,0.1)',
            zerolinecolor: 'rgba(255,255,255,0.2)'
        },
        margin: {
            l: 60,
            r: 40,
            t: 40,
            b: 60
        },
        hovermode: 'x unified',
        legend: {
            bgcolor: 'rgba(17, 21, 48, 0.8)',
            bordercolor: 'rgba(255,255,255,0.1)',
            borderwidth: 1
        }
    };

    const config = {
        responsive: true,
        displayModeBar: true,
        displaylogo: false,
        modeBarButtonsToRemove: ['lasso2d', 'select2d']
    };

    Plotly.newPlot(plotContainer, traces, layout, config);
}

// Funciones de UI
function showLoading() {
    loading.classList.remove('hidden');
    results.classList.add('hidden');
    errorMessage.classList.add('hidden');
    emptyState.classList.add('hidden');
}

function hideLoading() {
    loading.classList.add('hidden');
}

function showError(error) {
    hideLoading();
    hideEmptyState();
    errorMessage.textContent = 'Error: ' + error;
    errorMessage.classList.remove('hidden');
    results.classList.add('hidden');
}

function hideError() {
    errorMessage.classList.add('hidden');
}

function showEmptyState() {
    hideLoading();
    hideError();
    results.classList.add('hidden');
    emptyState.classList.remove('hidden');

    // Limpiar gráfica
    Plotly.purge(plotContainer);
}

function hideEmptyState() {
    emptyState.classList.add('hidden');
}

function clearAll() {
    functionInput.value = '';
    lowerLimitInput.value = '';
    upperLimitInput.value = '';
    variableInput.value = 'x';
    showEmptyState();
}

// Inicialización
showEmptyState();
