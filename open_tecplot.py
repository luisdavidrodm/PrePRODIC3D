import sys

try:
    from paraview.simple import *
except ImportError:
    sys.exit("Este script debe ejecutarse dentro del entorno de Python de ParaView.")

tecplot_file_path = "C:/PRODIC3D/Utilidades/F90/dona/A1PLOT  .000"
reader = TecplotReader(FileNames=[tecplot_file_path])
reader.UpdatePipeline()
view = GetActiveViewOrCreate("RenderView")
display = GetDisplayProperties(reader, view=view)
display.Representation = "Surface With Edges"
point_data_info = reader.GetPointDataInformation()
point_arrays = [array_info.GetName() for array_info in point_data_info]
if "Temperat" in point_arrays:
    display.ColorArrayName = ["POINTS", "Temperat"]
    colorMap = GetColorTransferFunction("Temperat")
    try:
        colorMap.ApplyPreset("Turbo", True)
        display.LookupTable = colorMap
        display.RescaleTransferFunctionToDataRange(True, False)
        display.SetScalarBarVisibility(view, True)
    except:
        print("El preset 'Turbo' no está disponible. Verifica los presets de colores instalados.")
else:
    print("La variable 'Temperat' no se encontró en los datos.")
Render(view)
