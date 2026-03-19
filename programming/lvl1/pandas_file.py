import pandas as pd


def work_with_pandas():
    """Тот же функционал с использованием pandas"""
    # Чтение
    df = pd.read_csv('products.csv')

    # Фильтрация
    filtered_df = df[
        (df['price'] >= 500) &
        (df['price'] <= 5000) &
        (df['amount'] >= 5)
        ].copy()

    # Добавляем столбец с общей стоимостью
    filtered_df['total_value'] = filtered_df['price'] * filtered_df['amount']

    # Сортировка
    filtered_df = filtered_df.sort_values('total_value', ascending=False)

    # Сохранение
    filtered_df.to_csv('filtered_pandas.csv', index=False)

    # Отчет
    report = f"""
ОТЧЕТ (Pandas)
==============
Всего товаров: {len(filtered_df)}
Общая стоимость: {filtered_df['total_value'].sum():,}
Средняя цена: {filtered_df['price'].mean():.2f}
Максимальная цена: {filtered_df['price'].max()}
    """

    with open('report_pandas.txt', 'w', encoding='utf-8') as f:
        f.write(report)

    return filtered_df



work_with_pandas()