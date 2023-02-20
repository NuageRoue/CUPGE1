import matplotlib.pyplot as plt


#ex 44, dessin à partir d'un fichier

def draw_from_file(file_name):
    file = open(f"{file_name}.txt",'r')
    file_line = file.readlines()
    x_list, y_list = [],[]
    print(file_line)
    for line in file_line:
        x,y = (line[:-1:].split(' '))
        x_list.append(float(x))
        y_list.append(float(y))
    plt.plot(x_list,y_list)
    plt.show()
    file.close()
print(draw_from_file("points"))