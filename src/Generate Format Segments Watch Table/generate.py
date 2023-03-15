def generate(segments:int)-> str:
    data = ''
    for i in range(segments):
        data += f'"ADP_Gateway_Interface.Data".format_segments[{i}].foreground_color\n"ADP_Gateway_Interface.Data".format_segments[{i}].background_color\n"ADP_Gateway_Interface.Data".format_segments[{i}].flash\n"ADP_Gateway_Interface.Data".format_segments[{i}].line_number\n"ADP_Gateway_Interface.Data".format_segments[{i}].text\n\n'
    return data[:-2]

def write(data:str, path:str)-> None:
    with open(path, 'w') as file_:
        file_.write(data)
    return

write(generate(18), 'output.txt')