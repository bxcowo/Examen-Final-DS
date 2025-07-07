#!/bin/bash

set -e

NOMBRE="Desconocido"
APELLIDO="Desconocido"
EDAD=""
CODIGO=""

while [[ $# -gt 0 ]]; do
    case "$1" in
        --nombre)
            NOMBRE="${2:-Desconocido}"
            shift 2
            ;;
        --apellido)
            APELLIDO="${2:-Desconocido}"
            shift 2
            ;;
        --edad)
            EDAD="$2"
            shift 2
            ;;
        --codigo)
            CODIGO="$2"
            shift 2
            ;;
        *)
            echo "Opcion desconocida: $1"
            exit 1
            ;;
    esac
done

if [[ -z "$CODIGO" ]]; then
    echo "Se necesita especificar al menos un código válido"
    exit 1
fi

if [[ -z "$EDAD" ]]; then
    echo "Se necesita ingresar una edad"
    exit 1
fi

if (( EDAD < 18 )); then
    echo "Se necesita que la persona sea mayor de edad"
    exit 1
fi

FACULTAD="Facultad de Ciencias de la Universidad Nacional de Ingeniería"

echo "Se tienen los siguientes datos registrados de la persona"
echo "El estudiante $NOMBRE $APELLIDO de edad $EDAD años pertenece a la $FACULTAD"

exit 0
