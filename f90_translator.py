from datetime import datetime

# I de identacion mayor, i de identación menor, s de separador
I = "      "  # 6 espacios de indentación para el código F90
i = "  "
s = "!______________________________________________________________________"


class F90Translator:
    def __init__(self, config_manager):
        self.config_manager = config_manager
        self.f90_lines = []
        self.variables_map = {f"le_var_title{i}": i for i in range(1, 13)}
        self.volume_widgets = ["le_x_start", "le_x_end", "le_y_start", "le_y_end", "le_z_start", "le_z_end"]
        self.operator_mapping = {">": "GT", "≥": "GE", "<": "LT", "≤": "LE"}
        self.loop_mapping = {
            "X Max": ("J", "K", "M{}", "N{}", "(L{},J,K)", "L1", "ARX(J,K)"),
            "X Min": ("J", "K", "M{}", "N{}", "({},J,K)", "I1", "ARX(J,K)"),
            "Y Max": ("I", "K", "L{}", "N{}", "(I,M{},K)", "M1", "ARY(I,K)"),
            "Y Min": ("I", "K", "L{}", "N{}", "(I,{},K)", "J1", "ARY(I,K)"),
            "Z Max": ("I", "J", "L{}", "M{}", "(I,J,N{})", "N1", "ARZ(I,J)"),
            "Z Min": ("I", "J", "L{}", "M{}", "(I,J,{})", "K1", "ARZ(I,J)"),
        }
        self.corner_mapping = {
            "chb_corner_1": ("1", "1", "1"),
            "chb_corner_2": ("L1", "1", "1"),
            "chb_corner_3": ("1", "M1", "1"),
            "chb_corner_4": ("1", "1", "N1"),
            "chb_corner_5": ("L1", "M1", "1"),
            "chb_corner_6": ("1", "M1", "N1"),
            "chb_corner_7": ("L1", "1", "N1"),
            "chb_corner_8": ("L1", "M1", "N1"),
        }
        self.custom_titles = {
            1: "VEL U",
            2: "VEL V",
            3: "VEL W",
            4: "CORRECCION",
            5: "TEMPERATURA",
            11: "PRESION",
        }
        self.dimensionless = "DIMENSION  WSUM(25), TSUM(25), TB(25), WBAR(25), AREA(25)"
        self.dimensionless_common = "COMMON TW,TIN,WSUM,TSUM,TB,WBAR,AREA,FLOWIN,WMIN"
        self.dimensionless_output = """IF (ITER.EQ.LAST) THEN
        DO K=2,N2
         DO J=2,M2
           DO I=2,L2
              WSUM(K)=WSUM(K)+W(I,J,K)*ARZ(I,J)
              TSUM(K)=TSUM(K)+T(I,J,K)*W(I,J,K)*ARZ(I,J)
              AREA(K)=AREA(K)+ARZ(I,J)
              WBAR(K)=WSUM(K)/AREA(K)
           ENDDO
         ENDDO
        ENDDO
        DO K=2,N2
           TB(K)=TSUM(K)/(WSUM(K)+SMALL)
        ENDDO
        DO K=2,N2
          DO J=2,M2
            DO I=2,L2
               T(I,J,K)=(T(I,J,K)-TW)/(TB(K)-TW)
               T(I,J,N1)=T(I,J,N2)
               W(I,J,K)=W(I,J,K)/WBAR(K)
               W(I,J,N1)=W(I,J,N2)
            ENDDO
          ENDDO
        ENDDO
       ENDIF"""
        self.output_temperature = """IF (ITER.EQ.{iteration}) THEN
      DO N=1,4
      KSOLVE(N)=0
      END DO
      KSOLVE(5)=1
      END IF"""
        self.output_monitor = """DO IUNIT=IU1,IU2
         IF(ITER.EQ.0) WRITE(IUNIT,210)
  210    FORMAT({format_string})
         {write_string}
  220    FORMAT(2X,I4,2X,1P{len_format_values}E10.2)
      ENDDO"""

    def translate_grid_section(self, grid, header):
        """
        Tranduce la sección GRID del JSON a líneas de código F90, incluyendo los datos de HEADER.

        :param grid: Diccionario con la información de la sección GRID del JSON.
        :param header: Diccionario con la información de la sección HEADER del JSON.
        :return: Lista de líneas de código F90 correspondientes a la sección GRID y HEADER.
        """
        f90_lines = ["ENTRY GRID"]
        # HEADER section
        for key, f90_key in [("le_titulosimu", "HEADER"), ("le_tituloimpre", "PRINTF"), ("le_titulograf", "PLOTF")]:
            if key in header:
                f90_lines.append(f"{f90_key}='{header[key]}'")

        zone_type = grid.get("cb_zone_type", "Zona única")
        coord_type = grid.get("cb_coord_type", "Cartesianas")
        layer_index = {
            ("Zona única", "Cartesianas"): 0,
            ("Zona única", "Cilindricas"): 1,
            ("Varias zonas", "Cartesianas"): 2,
            ("Varias zonas", "Cilindricas"): 3,
        }.get((zone_type, coord_type), 0)

        mode = {"Cartesianas": 1, "Cilindricas": 2}.get(coord_type)
        kcy = 0 if grid.get("cb_system_type", "Abierto") == "Abierto" else 1
        f90_lines.append(f"MODE={mode} ; KCY={kcy}")

        coord_variables = {
            0: {"XL": "le_xlon", "YL": "le_ylon", "ZL": "le_zlon"},
            1: {"XL": "le_titalon", "R(1)": "le_rini", "YL": "le_rlon", "ZL": "le_zloncil"},
            2: {
                "XZONE({0})": "le_dirx_lon_zon{0}",
                "YZONE({0})": "le_diry_lon_zon{0}",
                "ZZONE({0})": "le_dirz_lon_zon{0}",
            },
            3: {
                "XZONE({0})": "le_dirtita_lon_zon{0}",
                "R(1)": "le_dirr_inidom",
                "YZONE({0})": "le_dirr_lon_zon{0}",
                "ZZONE({0})": "le_dirzcil_lon_zon{0}",
            },
        }
        nvc_variables = {
            0: {"NCVLX": "le_nvcx", "NCVLY": "le_nvcy", "NCVLZ": "le_nvcz"},
            1: {"NCVLX": "le_nvctita", "NCVLY": "le_nvcr", "NCVLZ": "le_nvczcil"},
            2: {
                "NCVX({0})": "le_dirx_nvcx_zon{0}",
                "NCVY({0})": "le_diry_nvcy_zon{0}",
                "NCVZ({0})": "le_dirz_nvcz_zon{0}",
            },
            3: {
                "NCVX({0})": "le_dirtita_nvctita_zon{0}",
                "NCVY({0})": "le_dirr_nvcr_zon{0}",
                "NCVZ({0})": "le_dirzcil_nvczcil_zon{0}",
            },
        }
        powr_variables = {
            0: {"POWERX": "le_potenciax", "POWERY": "le_potenciay", "POWERZ": "le_potenciaz"},
            1: {"POWERX": "le_potenciatita", "POWERY": "le_potenciar", "POWERZ": "le_potenciazcil"},
            2: {
                "POWRX({0})": "le_dirx_poten_zon{0}",
                "POWRY({0})": "le_diry_poten_zon{0}",
                "POWRZ({0})": "le_dirz_poten_zon{0}",
            },
            3: {
                "POWRX({0})": "le_dirtita_poten_zon{0}",
                "POWRY({0})": "le_dirr_poten_zon{0}",
                "POWRZ({0})": "le_dirzcil_poten_zon{0}",
            },
        }
        coord_variables = self.extend_variables(coord_variables, 1, 10)
        nvc_variables = self.extend_variables(nvc_variables, 1, 10)
        powr_variables = self.extend_variables(powr_variables, 1, 10)

        if layer_index in (2, 3):
            nz_widgets_dict = {
                2: ["sb_dirx_numz", "sb_diry_numz", "sb_dirz_numz"],
                3: ["sb_dirtita_numz", "sb_dirr_numz", "sb_dirzcil_numz"],
            }
            nz_widgets = nz_widgets_dict[layer_index]
            f90_lines.append(f"NZX={grid[nz_widgets[0]]} ; NZY={grid[nz_widgets[1]]}; NZZ={grid[nz_widgets[2]]}")

        if "le_dirr_inidom" not in grid:
            grid["le_dirr_inidom"] = "0"

        if "le_rini" not in grid:
            grid["le_rini"] = "0"

        for group in (coord_variables, nvc_variables, powr_variables):
            group_lines = []
            for var, key in group[layer_index].items():
                if key and key in grid:
                    group_lines.append(f"{var}={grid[key]}")
            if group_lines:
                for j in range(0, len(group_lines), 5):
                    segment = group_lines[j : j + 5]
                    f90_lines.append(" ; ".join(segment))

        grid_function = "ZGRID" if grid.get("cb_zone_type", "") == "Varias zonas" else "EZGRID"
        f90_lines.append(f"CALL {grid_function}")
        f90_lines.append("RETURN")
        return f90_lines

    def translate_begin_section(self, variables, dense, bound, values, output):
        f90_lines = ["ENTRY BEGIN"]

        for num in range(1, 12):
            if num in self.custom_titles:
                var_title = self.custom_titles[num]
            else:
                var_title = variables.get(f"le_var_title{num}")
            if var_title is not None and var_title != "":
                f90_lines.append(f"TITLE({num})='{var_title}'")

        for num in range(1, 11):
            if variables.get(f"chb_ksolve{num}") == 2:
                f90_lines.append(f"KSOLVE({num})=1")

        for num in range(1, 12):
            if variables.get(f"chb_kprint{num}") == 2:
                f90_lines.append(f"KPRINT({num})=1")

        if variables.get("cb_tsimu", "Permanente") == "Transitorio":
            f90_lines.append(f"IPTM={variables.get('le_iptm', '0')}")
            f90_lines.append(f"DT={variables.get('le_dt', '1.E+20')}")

        if "chb_dimensionless" in output and output["chb_dimensionless"] == 2:
            f90_lines.append("TW=1.0")

        for num in range(1, 12):
            var_name = f"le_var_title{num}"
            if var_name in values:
                num = int("".join(filter(str.isdigit, var_name)))
                if values[var_name].get("chb_iborx") == 2:
                    f90_lines.append(f"IBORX({num})=1")
                if values[var_name].get("chb_ibory") == 2:
                    f90_lines.append(f"IBORY({num})=1")
                if values[var_name].get("chb_iborz") == 2:
                    f90_lines.append(f"IBORZ({num})=1")
                if values[var_name].get("chb_ipun") == 2:
                    f90_lines.append(f"IPUN({num})=1")
                ixyz = values[var_name].get("le_ixyz")
                if ixyz is not None and ixyz != "":
                    f90_lines.append(f"IXYZ({num})={ixyz}")
                kblock = values[var_name].get("le_kblock")
                if kblock is not None and kblock != "":
                    f90_lines.append(f"KBLOC({num})={kblock}")

        for num in range(1, 12):
            relax = variables.get(f"le_relax{num}")
            if relax is not None and relax != "":
                f90_lines.append(f"RELAX({num})={relax}")
        tolerance = variables.get("le_tol")
        if tolerance is not None and tolerance != "":
            f90_lines.append(f"TOL={tolerance}")
        kord = 2 if variables.get("cb_trataborde", "Esquema de alto orden") == "Esquema de alto orden" else 1
        last = int(output.get("le_last", 5))
        f90_lines.append(f"KORD={kord}")
        f90_lines.append(f"LAST={last}")

        #### le_general_value
        for var_title, var_number in self.variables_map.items():
            if var_title in values and "le_general_value" in values[var_title]:
                cvi = 2 if values.get(var_title, {}).get("chb_ex_value", 1) == 2 else 1  # cvi: control_volume_index
                f90_lines.extend(
                    [
                        f"DO I={cvi},L{cvi}",
                        f"{i}DO J={cvi},M{cvi}",
                        f"{i}{i}DO K={cvi},N{cvi}",
                        f"{I}F(I,J,K,{var_number})={values[var_title]['le_general_value']}",
                        f"{i}{i}ENDDO",
                        f"{i}ENDDO",
                        "ENDDO",
                    ]
                )

        #### le_local_value in values
        for var_title, var_number in self.variables_map.items():
            if var_title in values:
                regions = {key: value for key, value in values[var_title].items() if isinstance(value, dict)}
                for region, region_values in regions.items():
                    if "le_local_value" in region_values:
                        volumes = {key: value for key, value in region_values.items() if isinstance(value, dict)}
                        for volume, volume_values in volumes.items():
                            cvi = (
                                2 if volume_values.get("chb_exclude_borders", 1) == 2 else 1
                            )  # cvi: control_volume_index

                            condition_str = self.volume_operator_conditions(volume_values)

                            f90_lines.extend(
                                [
                                    f"DO I={cvi},L{cvi}",
                                    f"{i}DO J={cvi},M{cvi}",
                                    f"{i}{i}DO K={cvi},N{cvi}",
                                    f"{I}IF({condition_str}) F(I,J,K,{var_number})={region_values['le_local_value']}",
                                    f"{i}{i}ENDDO",
                                    f"{i}ENDDO",
                                    "ENDDO",
                                ]
                            )

        #### le_local_value in dense
        for region, region_values in dense.items():
            if any(value in region_values for value in ["le_local_value", "le_ref_rho", "le_ref_temp"]):
                volumes = {key: value for key, value in region_values.items() if isinstance(value, dict)}
                for volume, volume_values in volumes.items():
                    cvi = 2 if volume_values.get("chb_exclude_borders", 1) == 2 else 1  # cvi: control_volume_index
                    condition_str = self.volume_operator_conditions(volume_values)
                    f90_lines.extend(
                        [
                            f"DO I={cvi},L{cvi}",
                            f"{i}DO J={cvi},M{cvi}",
                            f"{i}{i}DO K={cvi},N{cvi}",
                        ]
                    )
                    if region_values.get("cb_condition", "Valor constante") == "Valor constante":
                        f90_lines.append(f"{I}IF({condition_str}) RHO(I,J,K)={region_values['le_local_value']}")
                    else:
                        ref_value = float(region_values.get("le_ref_rho", 1)) * float(
                            region_values.get("le_ref_temp", 1)
                        )
                        f90_lines.append(f"{I}IF({condition_str}) RHO(I,J,K)={ref_value}/F(I,J,K,5)")
                    f90_lines.extend(
                        [
                            f"{i}{i}ENDDO",
                            f"{i}ENDDO",
                            "ENDDO",
                        ]
                    )

        for boundary, patchs in bound.items():
            for patch, patch_values in patchs.items():
                transversal_var, vertical_var, transversal_end, vertical_end, indexes, _, _ = self.loop_mapping[
                    boundary
                ]
                cvi = 2 if patch_values.get("chb_exclude_borders", 1) == 2 else 1  # cvi: control_volume_index

                condition_str = self.border_operator_conditions(patch_values, transversal_var, vertical_var)

                variables = {key: value for key, value in patch_values.items() if isinstance(value, dict)}
                for variable, variable_values in variables.items():
                    value_condition = variable_values.get("chb_value", None)
                    border_value = variable_values.get("le_value", None)
                    if value_condition == 2 and border_value:
                        f90_lines.extend(
                            [
                                f"DO {transversal_var}={cvi},{transversal_end.format(cvi)}",
                                f"{i}DO {vertical_var}={cvi},{vertical_end.format(cvi)}",
                            ]
                        )
                        vcvi = 2 if variable_values.get("chb_ex_value", 1) == 2 else 1
                        var_number = "".join(filter(str.isdigit, variable))
                        formatted_indexes = indexes.format(vcvi).rstrip(")") + f",{var_number})"
                        if patch == "Borde base":
                            f90_lines.append(f"{i}{i}F{formatted_indexes}={border_value}")
                        else:
                            f90_lines.append(f"{i}{i}IF({condition_str}) F{formatted_indexes}={border_value}")
                        f90_lines.extend(
                            [
                                f"{i}ENDDO",
                                "ENDDO",
                            ]
                        )
        f90_lines.append("RETURN")
        return f90_lines

    def translate_dense_section(self):
        f90_lines = ["ENTRY DENSE"]
        f90_lines.append("RETURN")
        return f90_lines

    def translate_bound_section(self, bound):
        f90_lines = ["ENTRY BOUND"]
        if self.config_manager.has_out_mass and self.config_manager.has_in_mass:
            f90_lines.append("IF(ITER.NE.0) GO TO 350")
            f90_lines.append("FLOWIN=0.")
            for boundary, patches in bound.items():
                for patch, patch_values in patches.items():
                    if patch_values.get("chb_inmass") == 2:
                        transversal_var, vertical_var, transversal_end, vertical_end, indexes, _, arv = (
                            self.loop_mapping[boundary]
                        )
                        cvi = 2 if patch_values.get("chb_exclude_borders", 1) == 2 else 1  # cvi: control_volume_index
                        velocities = {
                            key: value
                            for key, value in patch_values.items()
                            if key in [f"le_var_title{i}" for i in range(1, 4)]
                        }
                        for velocity, velocity_values in velocities.items():
                            value_condition = velocity_values.get("chb_value", None)
                            border_value = velocity_values.get("le_value", None)
                            if value_condition == 2 and border_value:
                                f90_lines.extend(
                                    [
                                        f"DO {transversal_var}={cvi},{transversal_end.format(cvi)}",
                                        f"{i}DO {vertical_var}={cvi},{vertical_end.format(cvi)}",
                                    ]
                                )
                                vcvi = 2 if velocity_values.get("chb_ex_value", 1) == 2 else 1
                                var_number = "".join(filter(str.isdigit, velocity))
                                formatted_indexes = indexes.format(vcvi).rstrip(")") + f",{var_number})"
                                f90_lines.append(
                                    f"{i}{i}FLOWIN=FLOWIN+RHO{indexes.format(1)}*F{formatted_indexes}*{arv}"
                                )
                                f90_lines.extend(
                                    [
                                        f"{i}ENDDO",
                                        "ENDDO",
                                    ]
                                )
            f90_lines.append("  350 FL=0.")
            f90_lines.append("AFL=0.")
            f90_lines.append("WMIN=0.")
            for boundary, patches in bound.items():
                for patch, patch_values in patches.items():
                    if patch_values.get("chb_outmass") == 2:
                        transversal_var, vertical_var, transversal_end, vertical_end, indexes, _, arv = (
                            self.loop_mapping[boundary]
                        )
                        cvi = 2 if patch_values.get("chb_exclude_borders", 1) == 2 else 1  # cvi: control_volume_index
                        f90_lines.extend(
                            [
                                f"DO {transversal_var}={cvi},{transversal_end.format(cvi)}",
                                f"{i}DO {vertical_var}={cvi},{vertical_end.format(cvi)}",
                            ]
                        )
                        if "X" in boundary:
                            var_number = 1
                        if "Y" in boundary:
                            var_number = 2
                        if "Z" in boundary:
                            var_number = 3
                        formatted_indexes = indexes.format(2).rstrip(")") + f",{var_number})"
                        f90_lines.append(f"{i}{i}IF(F{formatted_indexes}.LT.0) WMIN=AMAX1(WMIN,-F{formatted_indexes})")
                        f90_lines.append(f"{i}{i}AFL=AFL+RHO{indexes.format(1)}*{arv}")
                        f90_lines.append(f"{i}{i}FL=FL+RHO{indexes.format(1)}*F{formatted_indexes}*{arv}")
                        f90_lines.extend(
                            [
                                f"{i}ENDDO",
                                "ENDDO",
                            ]
                        )
            f90_lines.append("FACTOR=FLOWIN/(FL+AFL*WMIN+SMALL)")
            for boundary, patches in bound.items():
                for patch, patch_values in patches.items():
                    if patch_values.get("chb_outmass") == 2:
                        transversal_var, vertical_var, transversal_end, vertical_end, indexes, _, _ = self.loop_mapping[
                            boundary
                        ]
                        cvi = 2 if patch_values.get("chb_exclude_borders", 1) == 2 else 1  # cvi: control_volume_index
                        condition_str = self.border_operator_conditions(patch_values, transversal_var, vertical_var)
                        f90_lines.extend(
                            [
                                f"DO {transversal_var}={cvi},{transversal_end.format(cvi)}",
                                f"{i}DO {vertical_var}={cvi},{vertical_end.format(cvi)}",
                            ]
                        )
                        if "X" in boundary:
                            var_number = 1
                        if "Y" in boundary:
                            var_number = 2
                        if "Z" in boundary:
                            var_number = 3
                        formatted_indexes = indexes.format(2).rstrip(")") + f",{var_number})"
                        border_indexes = indexes.format(1).rstrip(")") + f",{var_number})"
                        if patch == "Borde base":
                            f90_lines.append(f"{i}{i}F{border_indexes}=(F{formatted_indexes}+WMIN)*FACTOR")
                        else:
                            f90_lines.append(
                                f"{i}{i}IF({condition_str}) F{border_indexes}=(F{formatted_indexes}+WMIN)*FACTOR"
                            )
                        f90_lines.extend(
                            [
                                f"{i}ENDDO",
                                "ENDDO",
                            ]
                        )
        f90_lines.append("RETURN")
        return f90_lines

    def translate_output_section(self, output):
        f90_lines = ["ENTRY OUTPUT"]
        monitored_variables = {}
        for key, value in output.items():
            if key in self.variables_map and all(k in value for k in ["le_x", "le_y", "le_z"]):
                var_number = self.variables_map[key]
                coords = f"({value['le_x']},{value['le_y']},{value['le_z']},{var_number})"
                monitored_variables[var_number] = coords

        if monitored_variables:
            standard_space = "2X"
            format_string = "4X,'ITER',"
            format_values = ["ITER"]
            for _, coords in monitored_variables.items():
                format_string += f"{standard_space},'F{coords}',"
                format_values.append(f"F{coords}")

            format_string += f"{standard_space},'SMAX',{standard_space},'SSUM'"
            format_values.extend(["SMAX", "SSUM"])
            format_string = format_string.rstrip(",")
            write_string = "WRITE(IUNIT,220) " + ",".join(format_values)

            if "le_temp_last" in output:
                iteration = int(output.get("le_last", 5)) - int(float(output.get("le_temp_last")))
                if iteration > 0:
                    f90_lines.append(self.output_temperature.format(iteration=iteration))

            f90_lines.append(
                self.output_monitor.format(
                    format_string=format_string,
                    write_string=write_string,
                    len_format_values=len(format_values) - 1,
                )
            )

        if "chb_dimensionless" in output and output["chb_dimensionless"] == 2:
            f90_lines.append(self.dimensionless_output)

        for key, value in output.items():
            if key in self.variables_map:
                for variable, variable_value in value.items():
                    if variable in [f"chb_corner_{i}" for i in range(1, 9)] and variable_value == 2:
                        var_number = self.variables_map[key]
                        x, y, z = self.corner_mapping[variable]
                        f90_lines.append(self.generate_corner_equation(x, y, z, var_number))

        f90_lines.append("RETURN")
        return f90_lines

    def translate_phi_section(self, bound, values):
        f90_lines = ["ENTRY PHI"]
        added_if = False

        for var, nf_value in self.variables_map.items():

            #### GAM(I,J,K)=le_k
            if var in values and "le_k" in values[var]:
                if not added_if:
                    f90_lines.append(f"IF (NF.EQ.{nf_value}) THEN")
                    added_if = True
                cvi = 2 if values[var].get("chb_ex_k", 1) == 2 else 1  # cvi: control_volume_index
                f90_lines.extend(
                    [
                        f"{i}DO I={cvi},L{cvi}",
                        f"{i}{i}DO J={cvi},M{cvi}",
                        f"{I}DO K={cvi},N{cvi}",
                        f"{I}{i}GAM(I,J,K)={values[var]['le_k']}",
                        f"{I}ENDDO",
                        f"{i}{i}ENDDO",
                        f"{i}ENDDO",
                    ]
                )

            #### SC(I,J,K)=le_local_sc y GAM(I,J,K)=le_local_k
            if var in values and "chb_local_value" in values[var]:
                regions = {key: value for key, value in values[var].items() if isinstance(value, dict)}
                for region, region_values in regions.items():
                    if any(key in region_values for key in ("le_local_sc", "le_local_sp", "le_local_k")):
                        volumes = {key: value for key, value in region_values.items() if isinstance(value, dict)}
                        for volume, volume_values in volumes.items():
                            if not added_if:
                                f90_lines.append(f"IF (NF.EQ.{nf_value}) THEN")
                                added_if = True
                            cvi = (
                                2 if volume_values.get("chb_exclude_borders", 1) == 2 else 1
                            )  # cvi: control_volume_index
                            condition_str = self.volume_operator_conditions(volume_values)
                            f90_lines.append(f"{i}DO I={cvi},L{cvi}")
                            f90_lines.append(f"{i}{i}DO J={cvi},M{cvi}")
                            f90_lines.append(f"{I}DO K={cvi},N{cvi}")
                            if "le_local_sc" in region_values:
                                f90_lines.append(f"{I}{i}IF({condition_str}) SC(I,J,K)={region_values['le_local_sc']}")
                            if "le_local_sp" in region_values:
                                f90_lines.append(f"{I}{i}IF({condition_str}) SP(I,J,K)={region_values['le_local_sp']}")
                            if "le_local_k" in region_values:
                                f90_lines.append(f"{I}{i}IF({condition_str}) GAM(I,J,K)={region_values['le_local_k']}")
                            f90_lines.append(f"{I}ENDDO")
                            f90_lines.append(f"{i}{i}ENDDO")
                            f90_lines.append(f"{i}ENDDO")

            #### chb_flux, FLXC=le_value, FLXP=le_tempamb y GAM=le_k
            for boundary, patches in bound.items():
                for patch, patch_values in patches.items():
                    transversal_var, vertical_var, transversal_end, vertical_end, indexes, phi_var, arv = (
                        self.loop_mapping[boundary]
                    )
                    cvi = 2 if patch_values.get("chb_exclude_borders", 1) == 2 else 1  # cvi: control_volume_index
                    condition_str = self.border_operator_conditions(patch_values, transversal_var, vertical_var)

                    #### chb_flux
                    if var in patch_values and "chb_flux" in patch_values[var] and patch_values[var]["chb_flux"] == 2:
                        if not added_if:
                            f90_lines.append(f"IF (NF.EQ.{nf_value}) THEN")
                            added_if = True
                        f90_lines.extend(
                            [
                                f"{i}DO {transversal_var}={cvi},{transversal_end.format(cvi)}",
                                f"{i}{i}DO {vertical_var}={cvi},{vertical_end.format(cvi)}",
                            ]
                        )
                        if patch == "Borde base":
                            f90_lines.append(f"{I}KBC{phi_var}({transversal_var},{vertical_var})=2")
                        else:
                            f90_lines.append(f"{I}IF({condition_str}) KBC{phi_var}({transversal_var},{vertical_var})=2")
                        if "le_value" in patch_values[var]:
                            le_value = patch_values[var]["le_value"]
                            if patch == "Borde base":
                                f90_lines.append(f"{I}FLXC{phi_var}({transversal_var},{vertical_var})={le_value}")
                            else:
                                f90_lines.append(
                                    f"{I}IF({condition_str}) FLXC{phi_var}({transversal_var},{vertical_var})={le_value}"
                                )
                        if "le_tempamb" in patch_values[var]:
                            le_tempamb = patch_values[var]["le_tempamb"]
                            if patch == "Borde base":
                                f90_lines.append(f"{I}FLXP{phi_var}({transversal_var},{vertical_var})={le_tempamb}")
                            else:
                                f90_lines.append(
                                    f"{I}IF({condition_str}) FLXP{phi_var}({transversal_var},{vertical_var})={le_tempamb}"
                                )
                        f90_lines.extend(
                            [
                                f"{i}{i}ENDDO",
                                f"{i}ENDDO",
                            ]
                        )

                    #### chb_convec
                    if (
                        var in patch_values
                        and "chb_convec" in patch_values[var]
                        and patch_values[var]["chb_convec"] == 2
                    ):
                        if not added_if:
                            f90_lines.append(f"IF (NF.EQ.{nf_value}) THEN")
                            added_if = True
                        f90_lines.extend(
                            [
                                f"{i}DO {transversal_var}={cvi},{transversal_end.format(cvi)}",
                                f"{i}{i}DO {vertical_var}={cvi},{vertical_end.format(cvi)}",
                            ]
                        )
                        if patch == "Borde base":
                            f90_lines.append(f"{I}KBC{phi_var}({transversal_var},{vertical_var})=2")
                        else:
                            f90_lines.append(f"{I}IF({condition_str}) KBC{phi_var}({transversal_var},{vertical_var})=2")
                        if "le_value" in patch_values[var]:
                            le_value = patch_values[var]["le_value"]
                            le_tempamb = patch_values[var].get("le_tempamb", "1")
                            if patch == "Borde base":
                                f90_lines.append(
                                    f"{I}FLXC{phi_var}({transversal_var},{vertical_var})={le_value}*{le_tempamb}*{arv}"
                                )
                            else:
                                f90_lines.append(
                                    f"{I}IF({condition_str}) FLXC{phi_var}({transversal_var},{vertical_var})={le_value}*{le_tempamb}*{arv}"
                                )
                        if "le_tempamb" in patch_values[var]:
                            le_tempamb = patch_values[var]["le_tempamb"]
                            if patch == "Borde base":
                                f90_lines.append(
                                    f"{I}FLXP{phi_var}({transversal_var},{vertical_var})=-{le_tempamb}*{arv}"
                                )
                            else:
                                f90_lines.append(
                                    f"{I}IF({condition_str}) FLXP{phi_var}({transversal_var},{vertical_var})=-{le_tempamb}*{arv}"
                                )
                        f90_lines.extend(
                            [
                                f"{i}{i}ENDDO",
                                f"{i}ENDDO",
                            ]
                        )

                    ##### GAM=le_k
                    if var in patch_values and "le_k" in patch_values[var]:
                        if not added_if:
                            f90_lines.append(f"IF (NF.EQ.{nf_value}) THEN")
                            added_if = True
                        f90_lines.extend(
                            [
                                f"{i}DO {transversal_var}={cvi},{transversal_end.format(cvi)}",
                                f"{i}{i}DO {vertical_var}={cvi},{vertical_end.format(cvi)}",
                            ]
                        )
                        le_k = patch_values[var]["le_k"]
                        vcvi = 2 if patch_values[var].get("chb_ex_k", 1) == 2 else 1
                        if patch == "Borde base":
                            f90_lines.append(f"{I}GAM{indexes.format(vcvi)}={le_k}")
                        else:
                            f90_lines.append(f"{I}IF({condition_str}) GAM{indexes.format(vcvi)}={le_k}")
                        f90_lines.extend(
                            [
                                f"{i}{i}ENDDO",
                                f"{i}ENDDO",
                            ]
                        )
            if added_if:
                f90_lines.append("ENDIF")
                added_if = False

        f90_lines.append("RETURN")
        f90_lines.append("END")
        return f90_lines

    ################################################################################
    ##
    ## Funciones auxiliares
    ##
    ################################################################################

    def border_operator_conditions(self, patch_values, transversal_var, vertical_var):
        transversal_start = patch_values.get("le_transversal_start", None)
        transversal_start_op = patch_values.get("cb_ex_transversal_start", "GE")
        transversal_start_op = self.operator_mapping.get(transversal_start_op, transversal_start_op)

        transversal_end = patch_values.get("le_transversal_end", None)
        transversal_end_op = patch_values.get("cb_ex_transversal_end", "LE")
        transversal_end_op = self.operator_mapping.get(transversal_end_op, transversal_end_op)

        vertical_start = patch_values.get("le_vertical_start", None)
        vertical_start_op = patch_values.get("cb_ex_vertical_start", "GE")
        vertical_start_op = self.operator_mapping.get(vertical_start_op, vertical_start_op)

        vertical_end = patch_values.get("le_vertical_end", None)
        vertical_end_op = patch_values.get("cb_ex_vertical_end", "LE")
        vertical_end_op = self.operator_mapping.get(vertical_end_op, vertical_end_op)

        conditions = []
        var_map = {"I": "X", "J": "Y", "K": "Z"}
        if transversal_start is not None:
            conditions.append(
                f"{var_map[transversal_var]}({transversal_var}).{transversal_start_op}.{transversal_start}"
            )
        if transversal_end is not None:
            conditions.append(f"{var_map[transversal_var]}({transversal_var}).{transversal_end_op}.{transversal_end}")
        if vertical_start is not None:
            conditions.append(f"{var_map[vertical_var]}({vertical_var}).{vertical_start_op}.{vertical_start}")
        if vertical_end is not None:
            conditions.append(f"{var_map[vertical_var]}({vertical_var}).{vertical_end_op}.{vertical_end}")

        return " .AND. ".join(conditions) if conditions else "1 .EQ. 1"

    def volume_operator_conditions(self, volume_values):
        x_start = volume_values.get("le_x_start", None)
        x_start_op = volume_values.get("cb_ex_x_start", "GE")
        x_start_op = self.operator_mapping.get(x_start_op, x_start_op)

        x_end = volume_values.get("le_x_end", None)
        x_end_op = volume_values.get("cb_ex_x_end", "LE")
        x_end_op = self.operator_mapping.get(x_end_op, x_end_op)

        y_start = volume_values.get("le_y_start", None)
        y_start_op = volume_values.get("cb_ex_y_start", "GE")
        y_start_op = self.operator_mapping.get(y_start_op, y_start_op)

        y_end = volume_values.get("le_y_end", None)
        y_end_op = volume_values.get("cb_ex_y_end", "LE")
        y_end_op = self.operator_mapping.get(y_end_op, y_end_op)

        z_start = volume_values.get("le_z_start", None)
        z_start_op = volume_values.get("cb_ex_z_start", "GE")
        z_start_op = self.operator_mapping.get(z_start_op, z_start_op)

        z_end = volume_values.get("le_z_end", None)
        z_end_op = volume_values.get("cb_ex_z_end", "LE")
        z_end_op = self.operator_mapping.get(z_end_op, z_end_op)

        conditions = []
        if x_start is not None:
            conditions.append(f"X(I).{x_start_op}.{x_start}")
        if x_end is not None:
            conditions.append(f"X(I).{x_end_op}.{x_end}")
        if y_start is not None:
            conditions.append(f"Y(J).{y_start_op}.{y_start}")
        if y_end is not None:
            conditions.append(f"Y(J).{y_end_op}.{y_end}")
        if z_start is not None:
            conditions.append(f"Z(K).{z_start_op}.{z_start}")
        if z_end is not None:
            conditions.append(f"Z(K).{z_end_op}.{z_end}")

        return " .AND. ".join(conditions) if conditions else "1 .EQ. 1"

    def extend_variables(self, variables, start, end):
        extended_variables = variables.copy()
        for key in [2, 3]:
            new_entries = {}
            for j in range(start, end + 1):
                for var_key, value in variables[key].items():
                    if "{0}" in var_key:
                        new_entries[var_key.format(j)] = value.format(j)
                    else:
                        new_entries[var_key] = value
                extended_variables[key] = new_entries
        return extended_variables

    def generate_corner_equation(self, x, y, z, var_index):
        adj_i = "2" if x == "1" else "L2"
        adj_j = "2" if y == "1" else "M2"
        adj_k = "2" if z == "1" else "N2"
        adjacents = [(x, adj_j, z), (adj_i, y, z), (x, y, adj_k)]
        opposites = [(adj_i, adj_j, z), (adj_i, y, adj_k), (x, adj_j, adj_k)]
        corner_opposite = (adj_i, adj_j, adj_k)
        equation_parts = [f"F({x},{y},{z},{var_index}) = "]
        equation_parts.append(f"F({adjacents[0][0]},{adjacents[0][1]},{adjacents[0][2]},{var_index}) ")
        equation_parts.append(f"+ F({adjacents[1][0]},{adjacents[1][1]},{adjacents[1][2]},{var_index}) ")
        equation_parts.append(f"+ F({adjacents[2][0]},{adjacents[2][1]},{adjacents[2][2]},{var_index}) ")
        equation_parts.append(f"- F({opposites[0][0]},{opposites[0][1]},{opposites[0][2]},{var_index}) ")
        equation_parts.append(f"- F({opposites[1][0]},{opposites[1][1]},{opposites[1][2]},{var_index}) ")
        equation_parts.append(f"- F({opposites[2][0]},{opposites[2][1]},{opposites[2][2]},{var_index}) ")
        equation_parts.append(f"+ F({corner_opposite[0]},{corner_opposite[1]},{corner_opposite[2]},{var_index})")
        equation = "".join(equation_parts)
        return equation

    def generate_f90(self):
        self.f90_lines.append(f"! Generado por PrePRODIC3D en fecha: {datetime.now().isoformat()}")
        self.extend_f90(["SUBROUTINE ADAPT"])
        self.extend_f90(["INCLUDE '3DCOMMON.F90'", self.dimensionless_common])

        if "chb_dimensionless" in self.config_manager.output and self.config_manager.output["chb_dimensionless"] == 2:
            self.extend_f90([self.dimensionless])

        # GRID
        grid_section_lines = self.translate_grid_section(self.config_manager.grid, self.config_manager.header)
        self.extend_f90(grid_section_lines)

        # BEGIN
        begin_section_lines = self.translate_begin_section(
            self.config_manager.variables,
            self.config_manager.dense,
            self.config_manager.bound,
            self.config_manager.values,
            self.config_manager.output,
        )
        self.extend_f90(begin_section_lines)

        # DENSE
        dense_section_lines = self.translate_dense_section()
        self.extend_f90(dense_section_lines)

        # BOUND
        bound_section_lines = self.translate_bound_section(
            self.config_manager.bound,
        )
        self.extend_f90(bound_section_lines)

        # OUTPUT
        output_section_lines = self.translate_output_section(self.config_manager.output)
        self.extend_f90(output_section_lines)

        # PHI
        phi_section_lines = self.translate_phi_section(self.config_manager.bound, self.config_manager.values)
        self.extend_f90(phi_section_lines)

        return "\n".join(self.f90_lines)

    def extend_f90(self, new_f90_lines):
        processed_lines = []
        for line in new_f90_lines:
            stripped_line = line.lstrip()
            if stripped_line and stripped_line.split()[0].isdigit():
                processed_lines.append(line)
            else:
                processed_lines.append(f"{I}{line}")
        self.f90_lines.extend([s] + processed_lines)
