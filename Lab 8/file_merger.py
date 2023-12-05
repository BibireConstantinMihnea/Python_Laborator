def merge(input_files, output_file, order, separator):
    fout = open(output_file, 'w')
    for order in order:
        if order >= 0 and order < len(input_files):
            fin = open(input_files[order], 'r')
            fout.write(fin.read())
            fout.write(separator)
