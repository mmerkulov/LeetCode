# Генератор для batch-обработки данных
# Проблема: Нужно обрабатывать большой объем данных батчами (пакетами) для оптимизации памяти.

def batch_processor(data_stream, batch_size=1000, processor_func=None):
    """
    Генератор для batch-обработки данных.
    """
    batch = []

    for item in data_stream:
        batch.append(item)

        if len(batch) >= batch_size:
            # Обрабатываем полный батч
            processed_batch = processor_func(batch) if processor_func else batch
            yield processed_batch
            batch = []  # Сбрасываем батч

    # Обрабатываем оставшиеся данные
    if batch:
        processed_batch = processor_func(batch) if processor_func else batch
        yield processed_batch


def simulate_data_stream(count=2500):
    """Генератор для симуляции потока данных"""
    for i in range(count):
        yield f"data_item_{i}"


def process_batch(batch):
    """Функция для обработки батча"""
    return [f"processed_{item}" for item in batch]


print("Batch processing:")
for i, batch in enumerate(batch_processor(data_stream=simulate_data_stream(2500),
                                          batch_size=500,
                                          processor_func=process_batch)):
    print(f"Батч {i + 1}: {len(batch)} элементов, пример: {batch[0]}")