import pandas as pd


class DataLoader:
    def load_data(self, file_path):
        """
        Завантаження даних з CSV файлу.

        Parameters:
            file_path (str): Шлях до CSV файлу.

        Returns:
            pd.DataFrame: Таблиця даних.

        Raises:
            FileNotFoundError: Якщо файл не знайдено.
            pd.errors.ParserError: Якщо файл має некоректний формат.
        """
        try:
            data = pd.read_csv(file_path)
            print(f"Файл успішно завантажено: {file_path}")
            return data
        except FileNotFoundError:
            raise FileNotFoundError(f"Файл не знайдено за шляхом: {file_path}")
        except pd.errors.ParserError as e:
            raise ValueError(f"Помилка під час розбору CSV файлу: {e}")
