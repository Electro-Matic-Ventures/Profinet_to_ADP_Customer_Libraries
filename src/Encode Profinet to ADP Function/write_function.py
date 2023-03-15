class WriteFunction:
    
    __LABELS = [
        "middle_hold",
        "fill_hold",
        "bottom_hold",
        "top_hold",
        "bottom_scroll",
        "fill_scroll",
        "middle_scroll",
        "top_scroll"
    ]
    
    def write(self)-> None:
        text = ''
        for label in self.__LABELS:
            region_label = label.upper().replace('_', ' ')
            variable_name = label.lower()
            text += f'REGION "{region_label}"\n\tIF #line.vertical_alignment = #profinet_encoding.{variable_name} THEN\n\t\t#"Profinet_to_ADP_Encoding.Vertical_Alignment" := CONCAT(IN1 := #to_sign,\n\t\tIN2:= #ADP_ENCODING.{variable_name});\n\t\tRETURN;\n\tEND_IF;\nEND_REGION\n\n\n'
        with open('output.txt', 'w') as file_:
            file_.write(text)
        return
    
WriteFunction().write()