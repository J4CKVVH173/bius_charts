from log_parser import LogParser
import matplotlib.pyplot as plt


if __name__ == '__main__':
    logs = LogParser('text.log')
    for mode in logs.get_mods_values():
        plt.title(mode)
        plt.xlabel('time')
        plt.ylabel('speed')
        plt.grid()
        x = [i*200 for i in range(len(logs.get_mods_values()[mode][logs.get_values_name()[-1]]))]
        for value in logs.get_mods_values()[mode]:
            plt.plot(x, logs.get_mods_values()[mode][value], label=value)
        plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
        plt.show()

