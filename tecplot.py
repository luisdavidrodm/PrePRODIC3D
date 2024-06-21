import sys
import os

try:
    from paraview.simple import *
except ImportError:
    sys.exit("Este script debe ejecutarse dentro del entorno de Python de ParaView.")

tecplot_file_path = os.getenv("PREPRODIC3D_TECPLOT_FILE_PATH")
if tecplot_file_path is None:
    print("Error: No se proporcionó la ruta del archivo tecplot.")
    sys.exit(1)

reader = TecplotReader(FileNames=[tecplot_file_path])
reader.UpdatePipeline()

view = GetActiveViewOrCreate("RenderView")

# Fondo blanco
colorPalette = GetSettingsProxy("ColorPalette")
colorPalette.SetPropertyWithName("Background", [1.0, 1.0, 1.0])
colorPalette.SetPropertyWithName("Background2", [1.0, 1.0, 1.0])

display = GetDisplayProperties(reader, view=view)
display.Representation = "Surface With Edges"

point_data_info = reader.GetPointDataInformation()
point_arrays = [array_info.GetName() for array_info in point_data_info]

if " TEMPERA" in point_arrays:
    display.ColorArrayName = ["POINTS", " TEMPERA"]
    colorMap = GetColorTransferFunction(" TEMPERA")
    try:
        colorMap.ApplyPreset("Turbo", True)
        display.LookupTable = colorMap
        display.RescaleTransferFunctionToDataRange(True, False)
        display.SetScalarBarVisibility(view, True)

        # Anotaciones en negro
        scalarBar = GetScalarBar(colorMap, view)
        scalarBar.TitleColor = [0.0, 0.0, 0.0]
        scalarBar.LabelColor = [0.0, 0.0, 0.0]

    except Exception as e:
        print("El preset 'Turbo' no está disponible. Verifica los presets de colores instalados.")
else:
    print("La variable ' TEMPERA' no se encontró en los datos.")

view.OrientationAxesLabelColor = [0.0, 0.0, 0.0]  # Ejes en negro
Render(view)
