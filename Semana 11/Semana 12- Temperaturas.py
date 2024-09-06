# Crear una matriz 3D para almacenar datos de temperatura
# Primera dimensión: Ciudades (3 ciudades)
# Segunda dimensión: Semanas (4 semanas)
# Tercera dimensión: Días de la semana (7 días)
temperaturas = [
    [   # Ciudad 1
        [   # Semana 1
            {"day": "Lunes", "temp": 65},
            {"day": "Martes", "temp": 67},
            {"day": "Miércoles", "temp": 70},
            {"day": "Jue    ves", "temp": 68},
            {"day": "Viernes", "temp": 72},
            {"day": "Sábado", "temp": 75},
            {"day": "Domingo", "temp": 78}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 66},
            {"day": "Martes", "temp": 68},
            {"day": "Miércoles", "temp": 71},
            {"day": "Jueves", "temp": 69},
            {"day": "Viernes", "temp": 73},
            {"day": "Sábado", "temp": 76},
            {"day": "Domingo", "temp": 79}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 64},
            {"day": "Martes", "temp": 66},
            {"day": "Miércoles", "temp": 69},
            {"day": "Jueves", "temp": 67},
            {"day": "Viernes", "temp": 71},
            {"day": "Sábado", "temp": 74},
            {"day": "Domingo", "temp": 77}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 63},
            {"day": "Martes", "temp": 65},
            {"day": "Miércoles", "temp": 68},
            {"day": "Jueves", "temp": 66},
            {"day": "Viernes", "temp": 70},
            {"day": "Sábado", "temp": 73},
            {"day": "Domingo", "temp": 76}
        ]
    ],
    [   # Ciudad 2
        [   # Semana 1
            {"day": "Lunes", "temp": 55},
            {"day": "Martes", "temp": 57},
            {"day": "Miércoles", "temp": 60},
            {"day": "Jueves", "temp": 58},
            {"day": "Viernes", "temp": 62},
            {"day": "Sábado", "temp": 65},
            {"day": "Domingo", "temp": 68}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 56},
            {"day": "Martes", "temp": 58},
            {"day": "Miércoles", "temp": 61},
            {"day": "Jueves", "temp": 59},
            {"day": "Viernes", "temp": 63},
            {"day": "Sábado", "temp": 66},
            {"day": "Domingo", "temp": 69}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 54},
            {"day": "Martes", "temp": 56},
            {"day": "Miércoles", "temp": 59},
            {"day": "Jueves", "temp": 57},
            {"day": "Viernes", "temp": 61},
            {"day": "Sábado", "temp": 64},
            {"day": "Domingo", "temp": 67}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 53},
            {"day": "Martes", "temp": 55},
            {"day": "Miércoles", "temp": 58},
            {"day": "Jueves", "temp": 56},
            {"day": "Viernes", "temp": 60},
            {"day": "Sábado", "temp": 63},
            {"day": "Domingo", "temp": 66}
        ]
    ],
    [   # Ciudad 3
        [   # Semana 1
            {"day": "Lunes", "temp": 75},
            {"day": "Martes", "temp": 77},
            {"day": "Miércoles", "temp": 80},
            {"day": "Jueves", "temp": 78},
            {"day": "Viernes", "temp": 82},
            {"day": "Sábado", "temp": 85},
            {"day": "Domingo", "temp": 88}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 76},
            {"day": "Martes", "temp": 78},
            {"day": "Miércoles", "temp": 81},
            {"day": "Jueves", "temp": 79},
            {"day": "Viernes", "temp": 83},
            {"day": "Sábado", "temp": 86},
            {"day": "Domingo", "temp": 89}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 74},
            {"day": "Martes", "temp": 76},
            {"day": "Miércoles", "temp": 79},
            {"day": "Jueves", "temp": 77},
            {"day": "Viernes", "temp": 81},
            {"day": "Sábado", "temp": 84},
            {"day": "Domingo", "temp": 87}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 73},
            {"day": "Martes", "temp": 75},
            {"day": "Miércoles", "temp": 78},
            {"day": "Jueves", "temp": 76},
            {"day": "Viernes", "temp": 80},
            {"day": "Sábado", "temp": 83},
            {"day": "Domingo", "temp": 86}
        ]
    ]
]

# Calcular y mostrar el promedio de temperaturas  para cada ciudad y semana
for i, ciudad in enumerate(temperaturas, start=1):
    print(f"Promedio de temperatura para Ciudad {i}:")
    for j, semana in enumerate(ciudad, start=1):
        suma = sum(dia["temp"] for dia in semana)
        promedio = suma / len(semana)
        print(f"  Semana {j}: {promedio:.2f}°c")
    print()