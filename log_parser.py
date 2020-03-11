class LogParser:
    def __init__(self, log_path):
        self.LOG_PATH = log_path
        self._VALUES_MAP = None
        self._PARSED_DATA = dict()
        self._parse_data()

    def _parse_data(self) -> None:
        """
        Метод парсит данные из файла.

        Он достается строку со списком значений из файла и достает все режимы работы и значения для них.
        :return: None
        """
        with open(self.LOG_PATH, 'r') as log:
            self._VALUES_MAP = log.readline().strip().split(' ')
            for line in log:
                line_values = line.strip().split(' ')
                mode_values = self._PARSED_DATA.get(line_values[0], dict())
                for i, value in enumerate(line_values[1:], 1):
                    mode_value = mode_values.get(self._VALUES_MAP[i], list())
                    mode_value.append(float(value))
                    mode_values[self._VALUES_MAP[i]] = mode_value
                self._PARSED_DATA[line_values[0]] = mode_values

    def get_values_name(self) -> tuple:
        """
        Метод для получения названия значений.

        Каждое значение имеет фиксированное положение в массиве, для получения названия значения используется
        массив содержащий эти названия.
        """
        return tuple(self._VALUES_MAP)

    def get_mods_values(self) -> dict:
        """
        Метод возвращает режимы и все их значения.

        :return: Словарь где ключ - это режим, а значение это массив сигналов на двигатель в этом режиме
        """

        return self._PARSED_DATA
