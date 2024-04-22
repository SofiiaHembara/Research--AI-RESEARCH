import sys

def memory_usage(filename):
    try:
        with open(filename, 'rb') as file:
            content = file.read()
            memory = sys.getsizeof(content)
            return memory
    except FileNotFoundError:
        print("Файл не знайдено.")
        return None

filename = 'shal_dmytro_gemini2.py'

memory = memory_usage(filename)
if memory is not None:
    print(f"Використана пам'ять для файлу '{filename}': {memory} байт")
